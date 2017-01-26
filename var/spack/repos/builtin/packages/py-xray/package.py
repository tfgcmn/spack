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


class PyXray(PythonPackage):
    """N-D labeled arrays and datasets in Python"""

    homepage = "https://github.com/pydata/xarray"
    url      = "https://pypi.python.org/packages/77/1d/0caab0a21b7f83cca7b497eee9e3e5e2643a5d5162a6d05bf773aa3daa9d/xray-0.7.0.tar.gz"

    version('0.7.0', 'e758549b4031784abc7ace6d58d0159c')

    depends_on('py-setuptools',      type='build')
    depends_on('py-pandas@0.15.0:',  type=('build', 'run'))
    depends_on('py-numpy@1.7:',      type=('build', 'run'))
    #depends_on('py-pytest@2.7.1:',  type=('build', 'run'))
