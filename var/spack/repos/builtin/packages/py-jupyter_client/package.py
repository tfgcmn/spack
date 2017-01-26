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


class PyJupyterClient(PythonPackage):
    """Jupyter protocol implementation and client libraries"""

    homepage = "http://jupyter.org"
    url      = "https://pypi.python.org/packages/88/03/d8e218721af0b084d4fda5e3bb89dc201505780f96ae060bf5e3e67c7707/jupyter_client-4.4.0.tar.gz#md5=8a428a07cbcd4f2e4ca7c2f728b718ea"

    version('4.4.0', '8a428a07cbcd4f2e4ca7c2f728b718ea')

    depends_on('py-setuptools',   type='build')
    depends_on('py-traitlets',    type=('build', 'run'))
    depends_on('py-pyzmq@13:',    type=('build', 'run'))
    depends_on('py-jupyter_core', type=('build', 'run'))
