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


class PyMyhdl(Package):
    """Python as a Hardware Description Language"""

    homepage = "http://www.myhdl.org"
    url      = "https://pypi.python.org/packages/f4/fe/27d582508e53a4baf479b3f0184e1aa53cc8b64ccca55853ce4c99a0b338/myhdl-0.9.0.tar.gz"

    version('0.9.0', 'c3b4e7b857b6f51d43720413546df15c')

    extends('python')

    depends_on('py-setuptools', type='build')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
