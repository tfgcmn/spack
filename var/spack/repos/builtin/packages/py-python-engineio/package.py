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


class PyPythonEngineio(PythonPackage):
    """Engine.IO is the implementation of transport-based
    cross-browser/cross-device bi-directional communication layer for Socket.IO."""

    homepage = "http://python-engineio.readthedocs.io/en/latest/"
    url      = "https://github.com/miguelgrinberg/python-engineio/archive/v2.0.2.tar.gz"

    version('3.3.0',
            sha256='e4ac17c04c32ccca67287dfdbbe4ee1e9eec3a0a1a9a6070f3ab784db08407dd',
            url='https://files.pythonhosted.org/packages/2f/09/83d627ad3dadd064bfb875c7767e93f3568354fe82cebe298b4e07f79238/python-engineio-3.3.0.tar.gz')
    version('2.0.2', 'b91c6fa900905f9a96b86c3e141e2754')

    depends_on('py-setuptools', type='build')
    depends_on('py-six@1.9.0:', type=('build', 'run'))
