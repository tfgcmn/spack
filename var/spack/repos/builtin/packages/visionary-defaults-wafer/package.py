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


class VisionaryDefaultsWafer(Package):
    """Visionary Meta Package"""

    # This is a meta-package.  Instructions:
    # $ cd /tmp
    # $ spack install binutils+plugins+gold
    # $ spack find binutils+plugins+gold
    # -- linux-debian8-x86_64 / gcc@4.X.X -----------------------------
    # qxd4ne6 binutils@2.27
    # $ spack install gcc@6.2.0+binutils+gold ^/qxd4ne6
    # $ spack cd -i "gcc@6.2.0+binutils+gold"
    # $ spack compiler find --scope site .
    # $ spack install visionary-defaults %gcc@6.2.0

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack-visions/archive/master.tar.gz'
    version('1.0', git='https://github.com/electronicvisions/spack-visions.git')

    depends_on('binutils+gold+plugins')

    depends_on('ncdu')
    depends_on('units')
    depends_on('ranger')
    depends_on('py-ranger')

    depends_on('mercurial')
    depends_on('git')
    depends_on('py-git-review')

    depends_on('cmake')
    depends_on('doxygen')
    depends_on('bear')
    depends_on('rtags')
    depends_on('cppcheck')

    depends_on('llvm+visionary+python~libcxx@5.0.0: build_type=Release')
    depends_on('genpybind')
    depends_on('node-js')

    depends_on('boost@1.55.0+graph+icu+mpi+python')
    depends_on('yaml-cpp+shared')
    depends_on('log4cxx')
    depends_on('googletest +gmock')
    depends_on('gflags')

    depends_on('cereal')
    depends_on('py-pybind11@2.2.0:')

    depends_on('py-bokeh')
    depends_on('py-pygtk')
    depends_on('gtkplus+X')
    depends_on('cairo+X')
    depends_on('py-pyside')

    depends_on('py-pynn @0.7.5')

    depends_on('python')
    depends_on('py-cython')
    depends_on('py-pip')
    depends_on('py-pylint')

    depends_on('py-virtualenv')

    depends_on('py-pytables @3.3.0:')
    depends_on('py-sqlalchemy')

    depends_on('py-pyyaml')

    depends_on('py-autopep8')
    depends_on('py-flake8')
    depends_on('py-jedi')

    depends_on('py-sphinx')
    depends_on('py-doxypy')
    depends_on('py-nose')
    depends_on('py-junit-xml')
    depends_on('py-xmlrunner')
    depends_on('py-pytest')
    depends_on('py-pytest-xdist')
    depends_on('py-attrs')
    depends_on('py-setuptools')

    depends_on('py-tabulate')
    depends_on('py-html5lib')
    depends_on('py-pillow')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-defaults-wafer.py'))

        # we could create some filesystem view here?
