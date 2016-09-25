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


class PyRope(Package):
    """a python refactoring library..."""

    homepage = "https://github.com/python-rope/rope"
    url      = "https://pypi.python.org/packages/e1/5e/fe00383d52d0a1e0be42e6f1ee98d53902bfffb6b2835616c0fceca45597/rope-0.10.3.tar.gz"

    version('0.10.3', '2fd498b64fe5390946167494eff13642')

    extends('python')

    # depends_on('py-setuptools', type='build')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
