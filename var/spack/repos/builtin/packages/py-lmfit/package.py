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


class PyLmfit(PythonPackage):
    """Least-Squares Minimization with Bounds and Constraints"""

    homepage = "http://lmfit.github.io/lmfit-py/"
    url      = "https://pypi.python.org/packages/06/a0/42fda64e1fb05bfc21367fbc34732b83eb637e6ef3efb1e3466212b69271/lmfit-0.9.5.tar.gz#md5=3a38aa3e4510a564d9e2f606d2537522"

    version('0.9.5', '3a38aa3e4510a564d9e2f606d2537522')

    depends_on('py-numpy@1.5:',  type=('build', 'run'))
    depends_on('py-scipy@0.14:', type=('build', 'run'))
    depends_on('py-setuptools',  type='build')
