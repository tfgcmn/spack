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


class PyPydocstyle(PythonPackage):
    """docstring style checker"""

    homepage = "http://pydocstyle.org"
    url      = "https://pypi.io/packages/source/p/pydocstyle/pydocstyle-3.0.0.tar.gz"

    version('3.0.0', '5d37d5c28a24627b325751bdede21111')

    depends_on('py-setuptools', type='build')

    # docs from requirements/docs.txt
    # py-sphinxcontrib-issuetracker missing?
    depends_on('py-sphinx-rtd-theme', type=('build', 'run'))
    depends_on('py-sphinx', type=('build', 'run')) # TODO: upstream it is pinned to 1.6.2

    # runtime from requirements/runtime.txt
    depends_on('py-snowballstemmer@1.2.1:', type=('build', 'run'))
    depends_on('py-configparser@3.5.0:', type=('build', 'run'))
