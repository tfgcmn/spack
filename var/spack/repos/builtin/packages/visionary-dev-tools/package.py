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
from spack import *

import os.path as osp

class VisionaryDevTools(Package):
    """Developer convenience packages common to all visionary
       development meta packages. Application specific build tools belong
       to the dedicated meta packages."""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    depends_on('ack')
    depends_on('autoconf')
    depends_on('automake')
    depends_on('bash-completion')
    depends_on('bazel')
    depends_on('bear')
    depends_on('cairo +X')
    depends_on('cloc')
    depends_on('cmake')
    depends_on('connect-proxy')
    depends_on('cppcheck +htmlreport')
    depends_on('cquery')
    depends_on('doxygen+graphviz')
    depends_on('emacs ~X')
    depends_on('gdb')
    depends_on('genpybind')
    depends_on('git+tcltk')
    depends_on('git-fat-git')
    depends_on('gtkplus')
    depends_on('jq')
    depends_on('libpcap')
    depends_on('libtool')
    depends_on('llvm+visionary+python~libcxx@7.0.0: build_type=Release')
    depends_on('mercurial')
    depends_on('mosh')
    depends_on('munge')
    depends_on('ncdu')
    depends_on('node-js')
    depends_on('openssh')
    depends_on('pkg-config')
    depends_on('py-autopep8')
    depends_on('py-black', when="^python@3.6.0:")
    depends_on('py-configargparse')
    depends_on('py-doxypypy')
    depends_on('py-flake8')
    depends_on('py-gdbgui')
    depends_on('py-git-review')
    depends_on('py-ipython')
    depends_on('py-jedi')
    depends_on('py-junit-xml')
    depends_on('py-language-server')
    depends_on('py-line-profiler')
    depends_on('py-nose')
    depends_on('py-nose2')
    depends_on('py-memory-profiler')
    depends_on('py-pudb')
    depends_on('py-pytest')
    depends_on('py-pytest-xdist')
    depends_on('py-ranger-fm')
    depends_on('py-sqlalchemy')
    depends_on('py-virtualenv')
    depends_on('py-xmlrunner')
    depends_on('py-yq')
    depends_on('rtags')
    depends_on('tar')
    depends_on('texinfo')
    depends_on('the-silver-searcher')
    depends_on('tig')
    depends_on('time')
    depends_on('tmux')
    depends_on('units')
    depends_on('valgrind')
    depends_on('verilator')
    depends_on('vim +python +ruby +perl +cscope +huge +x')
    depends_on('visionary-xilinx')
    depends_on('wget')
    depends_on('yaml-cpp+shared')
    depends_on('zsh')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        filename = osp.basename(osp.dirname(__file__)) # gives name of parent folder
        install(__file__, join_path(prefix.etc, filename + '.py'))

        # we could create some filesystem view here?
