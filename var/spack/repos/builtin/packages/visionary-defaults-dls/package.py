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


class VisionaryDefaultsDls(Package):
    """Visionary Meta Package"""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    depends_on('visionary-defaults-common')

    # to provide non-gccxml spack views we manually add the gccxml w/o dependencies later :)
    variant('gccxml', default=False)

    # depends_on('libusb-1.0')  external dependency
    depends_on('boost@1.66.0+graph+icu+mpi+python+numpy')
    depends_on('cereal')
    depends_on('doxygen+graphviz')
    depends_on('gccxml', when='+gccxml')
    depends_on('genpybind')
    depends_on('gflags')
    depends_on('googletest+gmock')
    depends_on('llvm')
    depends_on('log4cxx')
    depends_on('munge')
    depends_on('py-matplotlib')
    depends_on('py-nose')
    depends_on('py-numpy')
    depends_on('py-pybind11')
    depends_on('py-sqlalchemy')
    depends_on('python')
    depends_on('tar')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-defaults.py'))

        # we could create some filesystem view here?
