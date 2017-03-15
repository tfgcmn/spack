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
import os

class Folly(Package):
    """Folly c++-library by facebook.
    """
    homepage = "https://github.com/facebook/folly"
    url      = "https://github.com/facebook/folly/archive/v2016.11.14.00.tar.gz"

    version('2016.11.14.00', '88550acdb4d4b331c0ca9922039c8727')
    version('2016.11.07.00', '2f605b20ad539bccdbfd361daa92081e')
    version('2016.10.31.00', 'ab3049302792f8470cef64f3a29eedec')
    version('2016.10.24.00', '0445efb7c16b5c32dfbb173157e54866')
    version('2016.10.17.00', 'b7e01934a45c5036fab8fdc70e9eaf4d')

    depends_on('binutils', type='build')
    depends_on('gflags')
    depends_on('glog')
    depends_on('double-conversion cppflags="-fPIC"')
    depends_on('boost')
    depends_on('zlib')
    depends_on('lzma')
    depends_on('lz4')
    depends_on('libevent')
    depends_on('openssl')

    def install(self, spec, prefix):
        autoreconf = which('autoreconf')
        with working_dir('folly/'):
            autoreconf('-ivf')
            configure('--prefix={0}'.format(prefix),
                      '--with-boost-libdir={0}'.format(spec['boost'].prefix + '/lib/'))
            make()
            make("install")
