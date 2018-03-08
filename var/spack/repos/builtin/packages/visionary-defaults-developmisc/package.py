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


class VisionaryDefaultsDevelopmisc(Package):
    """Visionary Meta Package"""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack-visions/archive/master.tar.gz'
    version('1.0', git='https://github.com/electronicvisions/spack-visions.git')

    depends_on('bear')
    depends_on('cloc')
    depends_on('cmake')
    depends_on('cppcheck')
    depends_on('doxygen')
    depends_on('emacs ~X')
    depends_on('gdb')
    depends_on('genpybind')
    depends_on('git')
    depends_on('llvm+visionary+python~libcxx@5.0.0: build_type=Release')
    depends_on('mercurial')
    depends_on('mosh')
    depends_on('ncdu')
    depends_on('node-js')
    depends_on('py-autopep8')
    depends_on('py-doxypypy')
    depends_on('py-flake8')
    depends_on('py-git-review')
    depends_on('py-jedi')
    depends_on('py-junit-xml')
    depends_on('py-nose')
    depends_on('py-pytest')
    depends_on('py-pytest-xdist')
    depends_on('py-ranger')
    depends_on('py-sqlalchemy')
    depends_on('py-virtualenv')
    depends_on('py-xmlrunner')
    depends_on('rtags')
    depends_on('tmux')
    depends_on('units')
    depends_on('vim +python +ruby +perl +cscope +huge +x')
    depends_on('yaml-cpp+shared')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-defaults.py'))

        # we could create some filesystem view here?
