##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
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


class Libusb(AutotoolsPackage):
    """A cross-platform library to access USB devices"""

    homepage = "https://github.com/libusb/libusb"
    url      = "https://github.com/libusb/libusb/releases/download/v1.0.22/libusb-1.0.22.tar.bz2"

    version('1.0.22', '466267889daead47674df933cea9cacb')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')

    # libudev is a host-dependency
    variant('udev', default=True, description='Enable libudev support')

    def configure_args(self):
        args = []
        if '+udev' in self.spec:
            args.append('--enable-udev')
        else:
            args.append('--disable-udev')
        return args
