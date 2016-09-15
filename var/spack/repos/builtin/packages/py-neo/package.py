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


class PyNeo(Package):
    """Neo is a package for representing electrophysiology data in Python, together with support for reading a wide range of neurophysiology file formats"""

    homepage = "http://neuralensemble.org/neo"
    url      = "https://pypi.python.org/packages/ca/c7/51c39a5ae8d7ddbf5627ce38c99082e4319e74c48eb71bd6df238a345192/neo-0.4.1.tar.gz"

    version('0.4.1', 'f706df3a1bce835cb490b812ac198a6e')

    extends('python')

    depends_on('py-setuptools',        type='build')
    depends_on('py-numpy@1.7.1:',      type=nolink)
    depends_on('py-quantities@0.9.0:', type=nolink)

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
