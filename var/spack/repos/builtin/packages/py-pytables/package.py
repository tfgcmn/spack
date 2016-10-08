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


class PyPytables(PythonPackage):
    """PyTables is a package for managing hierarchical datasets and designed to
    efficiently and easily cope with extremely large amounts of data."""

    homepage = "http://www.pytables.org/"
    url      = "https://pypi.io/packages/source/t/tables/tables-3.3.0.tar.gz"

    version('3.3.0', '056c161ae0fd2d6e585b766adacf3b0b',
            url='https://github.com/PyTables/PyTables/archive/v3.3.0.tar.gz')
    version('3.2.2', '7cbb0972e4d6580f629996a5bed92441')

    depends_on('hdf5@1.8.0:1.8.999')
    depends_on('py-numpy@1.8.0:', type=('build', 'run'))
    depends_on('py-numexpr@2.5.2:', type=('build', 'run'))
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-cython', type='build')
    depends_on('py-six', type=nolink)
    depends_on('hdf5@1.8.4:1.8.99')
    depends_on('lzo')
    depends_on('bzip2')
    # depends_on('c-blosc')
    # FIXME:
    #    .../lib/python2.7/site-packages/tables-3.3.0-py2.7-linux-x86_64.egg/tables/filters.py in <module>()
    #         36
    #         37 all_complibs = ['zlib', 'lzo', 'bzip2', 'blosc']
    #    ---> 38 all_complibs += ['blosc:%s' % cname for cname in blosc_compressor_list()]
    #         39
    #         40
    #
    #    tables/utilsextension.pyx in tables.utilsextension.blosc_compressor_list (tables/utilsextension.c:6977)()
    #
    #    UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-16: ordinal not in range(128)
    #
    # => use sources bundled with pytables for now

    def setup_environment(self, spack_env, run_env):
        spack_env.set('HDF5_DIR', self.spec['hdf5'].prefix)
