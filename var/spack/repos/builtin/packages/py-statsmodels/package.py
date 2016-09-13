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


class PyStatsmodels(Package):
    """Statistical computations and models for use with SciPy"""

    homepage = "http://www.statsmodels.org"
    url      = "https://pypi.python.org/packages/c8/0a/71ea3dbc6fd712e18123a9e513066c8f5e19dbcabc49b5ba7ab07c97ea29/statsmodels-0.8.0rc1.tar.gz#md5=da32434ebfebae2c7506e9577ac558f5"

    version('0.8.0rc1', 'da32434ebfebae2c7506e9577ac558f5')

    extends('python')

    depends_on('py-setuptools',    type='build')
    depends_on('py-numpy@1.5.1:',  type=nolink)
    depends_on('py-scipy@0.9.0:',  type=nolink)
    depends_on('py-pandas@0.7.1:', type=nolink)
    depends_on('py-patsy@0.3.0:',   type=nolink)
    depends_on('py-cython@0.20.1:', type=nolink)

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
