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


class PyPromptToolkit(PythonPackage):
    """Library for building powerful interactive command lines in Python"""

    homepage = "https://github.com/jonathanslenders/python-prompt-toolkit"
    url      = "https://pypi.python.org/packages/dd/55/2fb4883d2b21d072204fd21ca5e6040faa253135554590d0b67380669176/prompt_toolkit-1.0.7.tar.gz"

    version('1.0.7', 'f74cd8ac84176fac1cdb136843ccb0d6')

    depends_on('py-setuptools', type='build')
    depends_on('py-six@1.9.0:', type=('build', 'run'))
    depends_on('py-wcwidth',    type=('build', 'run'))
    depends_on('py-pygments',   type=('build', 'run'))
