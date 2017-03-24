##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
'''Produce a "view" of a Spack DAG.

A "view" is file hierarchy representing the union of a number of
Spack-installed package file hierarchies.  The union is formed from:

- specs resolved from the package names given by the user (the seeds)

- all depenencies of the seeds unless user specifies `--no-depenencies`

- less any specs with names matching the regular expressions given by
  `--exclude`

The `view` can be built and tore down via a number of methods (the "actions"):

- symlink :: a file system view which is a directory hierarchy that is
  the union of the hierarchies of the installed packages in the DAG
  where installed files are referenced via symlinks.

- hardlink :: like the symlink view but hardlinks are used.

- statlink :: a view producing a status report of a symlink or
  hardlink view.

The file system view concept is imspired by Nix, implemented by
brett.viren@gmail.com ca 2016.

'''
# Implementation notes:
#
# This is implemented as a visitor pattern on the set of package specs.
#
# The command line ACTION maps to a visitor_*() function which takes
# the set of package specs and any args which may be specific to the
# ACTION.
#
# To add a new view:
# 1. add a new cmd line args sub parser ACTION
# 2. add any action-specific options/arguments, most likely a list of specs.
# 3. add a visitor_MYACTION() function
# 4. add any visitor_MYALIAS assignments to match any command line aliases

import os
import re
import functools as ft
import shutil
import spack
import spack.cmd
import spack.spec
from spack.store import layout
from spack.directory_layout import ExtensionAlreadyInstalledError
from spack.directory_layout import ExtensionAlreadyInstalledViewError
import llnl.util.tty as tty
from llnl.util.filesystem import join_path
from llnl.util.link_tree import LinkTree

description = "produce a single-rooted directory view of a spec"


def setup_parser(sp):
    setup_parser.parser = sp

    sp.add_argument(
        '-v', '--verbose', action='store_true', default=False,
        help="display verbose output")
    sp.add_argument(
        '-e', '--exclude', action='append', default=[],
        help="exclude packages with names matching the given regex pattern")
    sp.add_argument(
        '-d', '--dependencies', choices=['true', 'false', 'yes', 'no'],
        default='true',
        help="follow dependencies")

    ssp = sp.add_subparsers(metavar='ACTION', dest='action')

    specs_opts = dict(metavar='spec', action='store',
                      help="seed specs of the packages to view")

    # The action parameterizes the command but in keeping with Spack
    # patterns we make it a subcommand.
    file_system_view_actions = {
        "symlink": ssp.add_parser(
            'symlink', aliases=['add', 'soft'],
            help='add package files to a filesystem view via symbolic links'),
        "hardlink": ssp.add_parser(
            'hardlink', aliases=['hard'],
            help='add packages files to a filesystem via via hard links'),
        "remove": ssp.add_parser(
            'remove', aliases=['rm'],
            help='remove packages from a filesystem view'),
        "statlink": ssp.add_parser(
            'statlink', aliases=['status', 'check'],
            help='check status of packages in a filesystem view')
    }

    actions_with_all_option = ["remove", "statlink"]

    # All these options and arguments are common to every action.
    for cmd, act in file_system_view_actions.iteritems():
        act.add_argument('path', nargs=1,
                         help="path to file system view directory")

        if cmd in actions_with_all_option:
            grp = act.add_mutually_exclusive_group(required=True)

            # with all option, spec is an optional argument
            so = specs_opts.copy()
            so["nargs"] = "*"
            so["default"] = []
            grp.add_argument('specs', **so)
            grp.add_argument("-a", "--all", action='store_true',
                             help="act on all specs in view")

        else:
            # without all option, spec is required
            so = specs_opts.copy()
            so["nargs"] = "+"
            act.add_argument('specs', **so)

    return


def assuredir(path):
    'Assure path exists as a directory'
    if not os.path.exists(path):
        os.makedirs(path)


def purge_empty_directories(path):
    '''Ascend up from the leaves accessible from `path`
    and remove empty directories.'''
    for dirpath, subdirs, files in os.walk(path, topdown=False):
        for sd in subdirs:
            sdp = os.path.join(dirpath, sd)
            try:
                os.rmdir(sdp)
            except OSError:
                pass


def filter_exclude(specs, exclude):
    'Filter specs given sequence of exclude regex'
    to_exclude = [re.compile(e) for e in exclude]

    def exclude(spec):
        for e in to_exclude:
            if e.match(spec.name):
                return True
        return False
    return [s for s in specs if not exclude(s)]


def flatten(seeds, descend=True):
    'Normalize and flattend seed specs and descend hiearchy'
    flat = set()
    for spec in seeds:
        if not descend:
            flat.add(spec)
            continue
        flat.update(spec.normalized().traverse())
    return flat


def metadata_dir_in_view(spec, path):
    return join_path(path, layout.metadata_dir, spec.name)


def ignore_metadata_dir(filename):
    """Ignore-function to be passed to LinkTree"""
    return filename in layout.hidden_file_paths


def is_linked(spec, path):
    """Return whether or not spec is linked in path.

    Note: Only checks on name, not hash!
    """
    dotspack = metadata_dir_in_view(spec, path)
    return os.path.exists(os.path.join(dotspack))


def spec_in_view(spec, path):
    "Get spec of package actually linked."
    dotspack = metadata_dir_in_view(spec, path)
    with open(join_path(dotspack, layout.spec_file_name)) as f:
        spec = spack.spec.Spec.from_yaml(f)
    return spec


def all_specs_in_view(path):
    "Get all specs present in view."
    dotspack = join_path(path, layout.metadata_dir)
    if os.path.exists(dotspack):
        return map(spack.cmd.disambiguate_spec, os.listdir(dotspack))
    else:
        tty.error("Not a filesystem view: %s" % path)
    return []


def check_one(spec, path, verbose=False):
    'Check status of view in path against spec'
    if is_linked(spec, path):
        linked_spec = spec_in_view(spec, path)
        if linked_spec == spec:
            pass
        else:
            tty.warn("Package in %s: %s linked but %s specified."
                     % (path, linked.short_spec, spec.short_spec))
        return
    tty.info('Package not in %s: %s' % (path, spec.name))
    return


def remove_one(spec, path, verbose=False):
    'Remove any files found in `spec` from `path` and purge empty directories.'

    if not os.path.exists(path):
        return                  # done, short circuit

    if not is_linked(spec, path):
        if verbose:
            tty.info('Skipping package not linked in view: %s' % spec.name)
        return

    if spec.package.is_extension:
        if spec.package.is_activated_in(path):
            spec.package.do_deactivate(path_view=path, verbose=verbose,
                                       remove_dependents=True)
    else:
        tree = LinkTree(spec.prefix)
        tree.unmerge(path, ignore=ignore_metadata_dir)
        if verbose:
            tty.info('Removed package in %s: "%s"' % (path, spec.name))

    remove_meta_folder(spec, path, verbose=verbose)


def link_all(specs, path, link=os.symlink, verbose=False):
    check = ft.partial(check_is_extension, path=path, verbose=verbose)
    link = ft.partial(link_one, path=path, link=link, verbose=verbose)
    activate = ft.partial(activate_one, path=path, verbose=verbose)

    specs = set(specs)

    # first check if packages to add are compatible extension-wise
    extensions = set(filter(check, specs))
    non_extensions = specs - extensions

    # link files only for non-extensions
    map(link, non_extensions)

    # activate and write extensions to filesystem view
    # (if there are any extensions)
    map(activate, extensions)


def link_one(spec, path, link=os.symlink, verbose=False):
    'Link all files in `spec` into directory `path`.'

    if is_linked(spec, path):
        tty.warn('Skipping already linked package: %s' % spec.name)
        return

    tree = LinkTree(spec.prefix)
    tree.merge(path, link=link, ignore=ignore_metadata_dir)
    link_meta_folder(spec, path, link=link)

    if verbose:
        tty.info('Linked package in %s: %s' % (path, spec.short_spec))


def check_is_extension(ext_spec, path, verbose):
    """Return whether or not ext_spec is an extension."""
    if not ext_spec.package.is_extension:
        return False

    # TODO: Update this once more than one extendee is allowed
    #  for spec in ext_spec.package.extendees:
    spec = ext_spec.package.extendee_spec

    # FIXME: spec might be !concrete if only variant-enabled
    if not spec.concrete:
        return False
    try:
        layout.check_extension_conflict(spec, ext_spec, path_view=path)
    except (ExtensionAlreadyInstalledError,
            ExtensionAlreadyInstalledViewError):
        # we print the warning here because later on the order in which
        # packages get activated is not clear (set-sorting)
        tty.warn('Skipping already activated package: %s' % ext_spec.name)
    return True


def activate_one(ext_spec, path, verbose, link=os.symlink):
    """Return whether or not ext_spec is an extension."""
    if not ext_spec.package.is_extension:
        tty.error('Package %s is not an extension.' % spec.name)
        return

    if is_linked(ext_spec, path) or ext_spec.package.activated:
        # silent fail because the warning is already printed in
        # check_is_extension
        return

    link_meta_folder(ext_spec, path, link=link)

    # activate extensions in fileystem view
    try:
        ext_spec.package.do_activate(path_view=path, verbose=verbose)
    except ExtensionAlreadyInstalledViewError:
        # the order might be random, this spec might already have been
        # activated as dependency for another
        pass


def link_meta_folder(spec, path, link=os.symlink):
    src = layout.metadata_path(spec)
    tgt = metadata_dir_in_view(spec, path)

    tree = LinkTree(src)
    tree.merge(tgt, link=link)


def remove_meta_folder(spec, path, verbose):
    path = metadata_dir_in_view(spec, path)
    assert os.path.exists(path)
    shutil.rmtree(path)


def visitor_symlink(specs, args):
    'Symlink all files found in specs'
    path = args.path[0]
    assuredir(path)
    link_all(specs, path, link=os.symlink, verbose=args.verbose)


visitor_add = visitor_symlink
visitor_soft = visitor_symlink


def visitor_hardlink(specs, args):
    'Hardlink all files found in specs'
    path = args.path[0]
    assuredir(path)
    link_all(specs, path, link=os.link, verbose=args.verbose)


visitor_hard = visitor_hardlink


def visitor_remove(specs, args, seeds):
    'Remove all files and directories found in specs from args.path'
    path = args.path[0]
    remove = ft.partial(remove_one, path=path, verbose=args.verbose)
    specs = set(specs)
    seeds = set(seeds)

    # determine the actual subset of specs to remove:
    all_specs = set(all_specs_in_view(path))
    to_keep = all_specs - specs

    # add dependencies of specs to keep:
    to_keep = set(flatten(to_keep))
    to_delete = all_specs - to_keep

    # remove all specs that depend on the user-supplied specs
    for s in to_keep:
        for dep in s.traverse(deptype='run'):
            if dep in seeds:
                to_delete.add(s)
                continue
    del to_keep

    # deactivate extensions prior to (possibly) unlinking any extendee
    extensions = set(filter(lambda s: s.package.is_extension, to_delete))
    non_extensions = to_delete - extensions

    map(remove, extensions)
    map(remove, non_extensions)

    purge_empty_directories(path)


visitor_rm = visitor_remove


def visitor_statlink(specs, args):
    'Give status of view in args.path relative to specs'
    path = args.path[0]
    specs = sorted(specs, key=lambda s: s.name)
    for spec in specs:
        check_one(spec, path, verbose=args.verbose)

    tty.msg("Specs linked in %s:" % path)
    spack.cmd.display_specs(specs, flags=True, variants=True,
                            long=args.verbose)


visitor_status = visitor_statlink
visitor_check = visitor_statlink


def view(parser, args):
    'Produce a view of a set of packages.'

    # Process common args
    if getattr(args, "all", False):
        path = args.path[0]
        seeds = [spack.cmd.disambiguate_spec(s)
                 for s in all_specs_in_view(path)]
    else:
        seeds = [spack.cmd.disambiguate_spec(s) for s in args.specs]
    specs = flatten(seeds, args.dependencies.lower() in ['yes', 'true'])
    specs = filter_exclude(specs, args.exclude)

    # Execute the visitation.
    try:
        visitor = globals()['visitor_' + args.action]
    except KeyError:
        tty.error('Unknown action: "%s"' % args.action)

    # remove action also needs seeds
    kwargs = {}
    if visitor is visitor_remove:
        kwargs["seeds"] = seeds

    visitor(specs, args, **kwargs)
