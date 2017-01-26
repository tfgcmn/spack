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


class PyQtconsole(PythonPackage):
    """Jupyter Qt console"""

    homepage = "http://ipython.org"
    url      = "https://pypi.python.org/packages/2b/94/ed3d11ab0ceac135f22fe418a9d5f99c4a071f74b5bd46c4f2ede65eafb1/qtconsole-4.2.1.tar.gz"

    version('4.2.1', 'c08ebebc7a60629ebadf685361ca0798')

    depends_on('py-setuptools',          type='build')
    depends_on('py-ipykernel@4.1:',      type=('build', 'run'))
    depends_on('py-jupyter_client@4.1:', type=('build', 'run'))
    depends_on('py-jupyter_core',        type=('build', 'run'))
    depends_on('py-pygments',            type=('build', 'run'))
    depends_on('py-traitlets',           type=('build', 'run'))

    #Sphinx (>=1.3); extra == 'doc'
    #mock; python_version=="2.7" and extra == 'test'
    #pexpect; sys_platform != "win32" and extra == 'test'
