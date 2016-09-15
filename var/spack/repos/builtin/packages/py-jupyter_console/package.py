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


class PyJupyterConsole(Package):
    """Jupyter terminal console"""

    homepage = "http://jupyter.org"
    url      = "https://pypi.python.org/packages/05/d6/64a59934c7fb8bf46e8b42bf6b21015643d9dd02e52234c7c8bc929dec5e/jupyter_console-5.0.0.tar.gz"

    version('5.0.0', '65d86429f41cc374a144f22526fe5048')

    extends('python')

    depends_on('py-setuptools',                 type='build')
    depends_on('py-pygments',                   type=nolink)
    depends_on('py-prompt_toolkit@1.0.0:1.9.9', type=nolink)
    depends_on('py-jupyter_client',             type=nolink)
    depends_on('py-ipython',                    type=nolink)
    depends_on('py-ipykernel',                  type=nolink)

    #pexpect; sys_platform != "win32" and extra == 'test'
    #mock; python_version=="2.7" and extra == 'test'

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
