##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
import argparse
import copy
import functools as ft
import os
import sys

import llnl.util.tty as tty
from llnl.util.filesystem import join_path

import spack
import spack.cmd
import spack.binary_distribution as bindist
from spack.binary_distribution import NoOverwriteException, NoGpgException
from spack.binary_distribution import NoKeyException, PickKeyException
from spack.binary_distribution import NoVerifyException, NoChecksumException
from spack.util.multiproc import NoDaemonPool

description = "Create, download and install build cache files."
section = "caching"
level = "long"


def setup_parser(subparser):
    setup_parser.parser = subparser
    subparsers = subparser.add_subparsers(help='buildcache sub-commands')

    create = subparsers.add_parser('create')
    create.add_argument('-r', '--rel', action='store_true',
                        help="make all rpaths relative" +
                             " before creating tarballs.")
    create.add_argument('-f', '--force', action='store_true',
                        help="overwrite tarball if it exists.")
    create.add_argument('-y', '--yes-to-all', action='store_true',
                        help="answer yes to all create unsigned " +
                             "buildcache questions")
    create.add_argument('-k', '--key', metavar='key',
                        type=str, default=None,
                        help="Key for signing.")
    create.add_argument('-j', '--jobs', type=int, default=1,
                        help="number of jobs with which to install in\ "
                             "parallel (defaults to 1)")
    create.add_argument('-d', '--directory', metavar='directory',
                        type=str, default='.',
                        help="directory in which to save the tarballs.")
    create.add_argument('-w', '--without-dependencies',
                        action='store_false', dest="dependencies",
                        help="install without dependencies")
    create.add_argument(
        'packages', nargs=argparse.REMAINDER,
        help="specs of packages to create buildcache for")
    create.set_defaults(func=createtarball)

    install = subparsers.add_parser('install')
    install.add_argument('-f', '--force', action='store_true',
                         help="overwrite install directory if it exists.")
    install.add_argument('-j', '--jobs', type=int, default=1,
                         help="number of jobs with which to install in\ "
                              "parallel (defaults to 1)")
    install.add_argument('-w', '--without-dependencies',
                         action='store_false', dest="dependencies",
                         help="install without dependencies")
    install.add_argument('-y', '--yes-to-all', action='store_true',
                         help="answer yes to all install unsigned " +
                              "buildcache questions")
    install.add_argument(
        'packages', nargs=argparse.REMAINDER,
        help="specs of packages to install biuldache for")
    install.set_defaults(func=installtarball)

    listcache = subparsers.add_parser('list')
    listcache.add_argument('-f', '--force', action='store_true',
                           help="force new download of specs")
    listcache.add_argument(
        'packages', nargs=argparse.REMAINDER,
        help="specs of packages to search for")
    listcache.set_defaults(func=listspecs)

    dlkeys = subparsers.add_parser('keys')
    dlkeys.add_argument(
        '-i', '--install', action='store_true',
        help="install Keys pulled from mirror")
    dlkeys.add_argument(
        '-y', '--yes-to-all', action='store_true',
        help="answer yes to all trust questions")
    dlkeys.add_argument('-f', '--force', action='store_true',
                        help="force new download of keys")
    dlkeys.set_defaults(func=getkeys)


def find_matching_specs(pkgs, allow_multiple_matches=False, force=False):
    """Returns a list of specs matching the not necessarily
       concretized specs given from cli

    Args:
        specs: list of specs to be matched against installed packages
        allow_multiple_matches : if True multiple matches are admitted

    Return:
        list of specs
    """
    # List of specs that match expressions given via command line
    specs_from_cli = []
    has_errors = False
    specs = spack.cmd.parse_specs(pkgs)
    for spec in specs:
        matching = spack.store.db.query(spec)
        # For each spec provided, make sure it refers to only one package.
        # Fail and ask user to be unambiguous if it doesn't
        if not allow_multiple_matches and len(matching) > 1:
            tty.error('%s matches multiple installed packages:' % spec)
            for match in matching:
                tty.msg('"%s"' % match.format())
            has_errors = True

        # No installed package matches the query
        if len(matching) == 0 and spec is not any:
            tty.error('{0} does not match any installed packages.'.format(
                spec))
            has_errors = True

        specs_from_cli.extend(matching)
    if has_errors:
        tty.die('use one of the matching specs above')

    return specs_from_cli


def match_downloaded_specs(pkgs, allow_multiple_matches=False, force=False):
    """Returns a list of specs matching the not necessarily
       concretized specs given from cli

    Args:
        specs: list of specs to be matched against buildcaches on mirror
        allow_multiple_matches : if True multiple matches are admitted

    Return:
        list of specs
    """
    # List of specs that match expressions given via command line
    specs_from_cli = []
    has_errors = False
    specs = bindist.get_specs(force)
    for pkg in pkgs:
        matches = []
        tty.msg("buildcache spec(s) matching %s \n" % pkg)
        for spec in sorted(specs):
            if pkg.startswith('/'):
                pkghash = pkg.replace('/', '')
                if spec.dag_hash().startswith(pkghash):
                    matches.append(spec)
            else:
                if spec.satisfies(pkg):
                    matches.append(spec)
        # For each pkg provided, make sure it refers to only one package.
        # Fail and ask user to be unambiguous if it doesn't
        if not allow_multiple_matches and len(matches) > 1:
            tty.error('%s matches multiple downloaded packages:' % pkg)
            for match in matches:
                tty.msg('"%s"' % match.format())
            has_errors = True

        # No downloaded package matches the query
        if len(matches) == 0:
            tty.error('%s does not match any downloaded packages.' % pkg)
            has_errors = True

        specs_from_cli.extend(matches)
    if has_errors:
        tty.die('use one of the matching specs above')

    return specs_from_cli


def createtarball(args):
    if not args.packages:
        tty.die("build cache file creation requires at least one" +
                " installed package argument")
    pkgs = set(args.packages)
    specs = set()
    outdir = os.getcwd()
    if args.directory:
        outdir = args.directory
    signkey = None
    if args.key:
        signkey = args.key
    yes_to_all = False
    force = False
    relative = False
    if args.yes_to_all:
        yes_to_all = True
    if args.force:
        force = True
    if args.rel:
        relative = True

    matches = find_matching_specs(pkgs, False, False)
    for match in matches:
        if match.external or match.virtual:
            tty.msg('skipping external or virtual spec %s' %
                    match.format())
        else:
            tty.msg('adding matching spec %s' % match.format())
            specs.add(match)

            if args.dependencies:
                tty.msg('recursing dependencies')
                for d, node in match.traverse(order='post',
                                              depth=True,
                                              deptype=('link', 'run')):
                    if node.external or node.virtual:
                        tty.msg('skipping external or virtual dependency %s' %
                                node.format())
                    else:
                        tty.msg('adding dependency %s' % node.format())
                        specs.add(node)

    f_create = ft.partial(create_single_tarball,
                          outdir=outdir,
                          force=force,
                          relative=relative,
                          yes_to_all=yes_to_all,
                          signkey=signkey)

    # defaul behavior (early termination) for one job
    if args.jobs <= 1:
        for spec in specs:
            rv = f_create(spec)

            if rv["error"] is not None:
                tty.die(rv["error"])
    else:
        pool = NoDaemonPool(args.jobs)
        retvals = pool.map(f_create, list(specs))
        # TODO: every f_create-call updates the index -> unnecessary
        # in order to have one consistent index, we update the indexfile once
        # afterwards
        indexfile_path = join_path(outdir, "build_cache", "index.html")
        bindist.generate_index(outdir, indexfile_path)

        errors = [rv["error"] for rv in retvals if rv["error"] is not None]
        list(map(tty.error, errors))
        if len(errors) > 0:
            sys.exit(1)


def create_single_tarball(
        spec, outdir, force, relative, yes_to_all, signkey):
    tty.msg('creating binary cache file for package %s ' % spec.format())
    retval = {"error": None}
    try:
        bindist.build_tarball(spec, outdir, force,
                              relative, yes_to_all, signkey)
    except NoOverwriteException as e:
        tty.warn("%s exists, use -f to force overwrite." % e)
    except NoGpgException:
        retval["error"] = "gpg2 is not available, use -y to create unsigned "\
                          "build caches"
    except NoKeyException:
        retval["error"] = "no default key available for signing,"\
                          " use -y to create unsigned build caches"\
                          " or spack gpg init to create a default key"
    except PickKeyException:
        retval["error"] = "multi keys available for signing,"\
                          " use -y to create unsigned build caches"\
                          " or -k <key hash> to pick a key"
    return retval


def installtarball(args):
    if not args.packages:
        tty.die("build cache file installation requires" +
                " at least one package spec argument")
    pkgs = set(args.packages)
    yes_to_all = False
    if args.yes_to_all:
        yes_to_all = True
    force = False
    if args.force:
        force = True
    matches = match_downloaded_specs(pkgs, yes_to_all, force)

    if args.dependencies:
        specs_cli = map(lambda spec: spack.spec.Spec(spec), matches)
        specs = copy.copy(specs_cli)
        specs_cli = filter(lambda s: not(s.external or s.virtual), specs)
        for s in specs_cli:
            for d in s.dependencies(deptype=('link', 'run')):
                tty.msg("Installing buildcache for dependency spec %s" % d)
                specs.append(d)

    f_install = ft.partial(install_tarball, args=args)

    # default behavior (early termination) for one job
    retvals = []
    if args.jobs <= 1:
        for match in matches:
            rv = f_install(match)
            if rv["error"] is not None:
                tty.die(rv["errro"])
            else:
                retvals.append(rv)
    else:
        pool = NoDaemonPool(args.jobs)
        retvals = pool.map(f_install, matches)

    if any(rv["reindex"] for rv in retvals):
        spack.store.db.reindex(spack.store.layout)

    errors = [rv["error"] for rv in retvals if rv["error"] is not None]
    list(map(tty.error, errors))

    if len(errors) > 0:
        sys.exit(1)


def install_tarball(spec, args):
    s = spack.spec.Spec(spec)
    if s.external or s.virtual:
        tty.warn("Skipping external or virtual package %s" % spec.format())
        return
    yes_to_all = False
    if args.yes_to_all:
        yes_to_all = True
    force = False
    if args.force:
        force = True
    package = spack.repo.get(spec)

    retval = {
        "reindex": False,
        "error": None,
    }

    if s.concrete and package.installed and not force:
        tty.warn("Package for spec %s already installed." % spec.format(),
                 " Use -f flag to overwrite.")
    else:
        tarball = bindist.download_tarball(spec)
        if tarball:
            tty.msg('Installing buildcache for spec %s' % spec.format())
            try:
                bindist.extract_tarball(spec, tarball, yes_to_all, force)
            except NoOverwriteException as e:
                tty.warn("%s exists. use -f to force overwrite." % e.args)
            except NoVerifyException:
                retval["error"] = "Package spec file failed signature "\
                                  "verification, use -y flag to install "\
                                  "build cache"
            except NoChecksumException:
                retval["error"] = "Package tarball failed checksum "\
                                  "verification, use -y flag to install "\
                                  "build cache"
            finally:
                retval["reindex"] = True
        else:
            retval["error"] = 'Download of binary cache file for spec %s '\
                              'failed.' % spec.format()
    return retval


def listspecs(args):
    specs = bindist.get_specs(args.force)
    if args.packages:
        pkgs = set(args.packages)
        for pkg in pkgs:
            tty.msg("buildcache spec(s) matching " +
                    "%s and commands to install them" % pkgs)
            for spec in sorted(specs):
                if spec.satisfies(pkg):
                    tty.msg('Enter\nspack buildcache install /%s\n' %
                            spec.dag_hash(7) +
                            ' to install "%s"' %
                            spec.format())
    else:
        tty.msg("buildcache specs and commands to install them")
        for spec in sorted(specs):
            tty.msg('Enter\nspack buildcache install /%s\n' %
                    spec.dag_hash(7) +
                    ' to install "%s"' %
                    spec.format())


def getkeys(args):
    install = False
    if args.install:
        install = True
    yes_to_all = False
    if args.yes_to_all:
        yes_to_all = True
    force = False
    if args.force:
        force = True
    bindist.get_keys(install, yes_to_all, force)


def buildcache(parser, args):
    if args.func:
        args.func(args)
