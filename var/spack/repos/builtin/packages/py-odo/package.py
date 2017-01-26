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


class PyOdo(Package):
    """FIXME"""
    homepage = "http://odo.readthedocs.org/"
    url = "https://pypi.io/packages/source/o/odo/odo-0.4.1.tar.gz"

    version('0.4.1', '')

    extends('python')
    depends_on('py-datashape', type=nolink)
    depends_on('py-numpy', type=nolink)
    depends_on('py-pandas', type=nolink)
    depends_on('py-toolz', type=nolink)
    depends_on('py-multipledispatch', type=nolink)
    depends_on('py-networkx', type=nolink)
    depends_on('py-dask', type=nolink)
    depends_on('py-setuptools', type='build')

    # TODO: set up variants: https://github.com/blaze/odo/tree/master/etc
    # requirements_*.txt

    def install(self, spec, prefix):
        setup_py('install', '--prefix=%s' % prefix)
