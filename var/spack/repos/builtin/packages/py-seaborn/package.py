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


class PySeaborn(Package):
    """Seaborn: statistical data visualization"""

    homepage = "http://stanford.edu/~mwaskom/software/seaborn"
    url      = "https://pypi.python.org/packages/ed/dc/f168ff9db34f8c03c568987b4f81603cd3df40dd8043722d526026381a91/seaborn-0.7.1.tar.gz#md5=ef07e29e0f8a1f2726abe506c1a36e93"

    version('0.7.1', 'ef07e29e0f8a1f2726abe506c1a36e93')

    extends('python')

    depends_on('py-setuptools',  type='build')
    depends_on('py-numpy',       type=nolink)
    depends_on('py-scipy',       type=nolink)
    depends_on('py-matplotlib',  type=nolink)
    depends_on('py-pandas',      type=nolink)
    depends_on('py-statsmodels', type=nolink)
    depends_on('py-patsy',       type=nolink)

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
