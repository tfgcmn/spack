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


class BundleDevelop(Package):
    """Develop Meta Package"""

    homepage = None
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack-visions/archive/master.tar.gz'
    version('0.1', git='https://github.com/electronicvisions/spack-visions.git')

    depends_on('binutils+gold+plugins', when='@0.2.5:')

    depends_on('cmake')
    depends_on('doxygen')
    depends_on('bear')
    depends_on('rtags@dev')

    depends_on('gdb')
    depends_on('llvm')
    depends_on('nodejs', when='@0.2.2')
    depends_on('node-js', when='@0.2.3:')

    depends_on('boost@1.55.0+graph+icu+mpi+python')
    depends_on('yaml-cpp+shared')
    depends_on('tensorflow', when='@:0.2.6')
    depends_on('tensorflow', when='@0.2.7:')
    depends_on('log4cxx')
    # depends_on('libpsf')
    depends_on('googletest', when='@:0.2.8')
    depends_on('googletest', when='@0.2.9:')
    depends_on('gflags')

    depends_on('cereal', when='@0.2.1:')
    depends_on('py-pybind11', when='@0.2.9:')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-defaults.py'))

        # we could create some filesystem view here?
