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


class PyBrian2(Package):
    """A clock-driven simulator for spiking neural networks"""

    homepage = "http://www.briansimulator.org"
    url      = "https://pypi.python.org/packages/50/43/5373353174657fac2c474beb1299d330c2c5716911c9995b22def4c8b330/Brian2-2.0rc3.tar.gz"

    version('2.0rc3', '3100c5e4eb9eb83a06ff0413a7d43152')

    extends('python', ignore=r'bin/*') # just copies of binaries...

    depends_on('py-setuptools@6.0:',   type='build')
    #depends_on('py-nosetests@1.0:',    type=nolink) # extra test
    #depends_on('py-nosetests@1.0:',    type=nolink) # extra docs
    #depends_on('py-sphinx@1.0.1:',     type=nolink) # extra docs
    depends_on('py-sympy@0.7.6:',      type=nolink)
    depends_on('py-pyparsing',         type=nolink)
    depends_on('py-py-cpuinfo@0.1.6:', type=nolink)
    depends_on('py-numpy@1.8.2:',      type=nolink)
    depends_on('py-jinja2@2.7:',       type=nolink)

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
