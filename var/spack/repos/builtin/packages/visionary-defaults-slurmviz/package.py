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


class VisionaryDefaultsSlurmviz(Package):
    """Visionary Meta Package to make sure the dependecies for slurmviz are built."""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    variant('dev', default=False)

    depends_on('visionary-defaults-dev-tools', when='+dev')
    depends_on('visionary-defaults-common')

    # TODO: extract hwdb dependencies and add only those here
    # Note: this effectively renders the +dev instructions mute
    depends_on('visionary-defaults')

    # OJB (2018-08-07): taken from slurm package, default values ajdusted
    variant('gtk', default=True, description='Enable GTK+ support')
    variant('mariadb', default=True, description='Use MariaDB instead of MySQL')

    variant('hwloc', default=True, description='Enable hwloc support')
    variant('hdf5', default=True, description='Enable hdf5 support')
    variant('readline', default=True, description='Enable readline support')

    depends_on('curl')
    depends_on('glib')
    depends_on('json-c')
    depends_on('lz4')
    depends_on('munge')
    depends_on('openssl')
    depends_on('pkgconfig') # build dependency removed because we build slurmviz separately
    depends_on('readline', when='+readline')
    depends_on('zlib')

    depends_on('gtkplus', when='+gtk')
    depends_on('hdf5', when='+hdf5')
    depends_on('hwloc', when='+hwloc')
    depends_on('mariadb build_type=Release', when='+mariadb') # keep build size small
