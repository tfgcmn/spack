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


class Pytorch(CMakePackage):
    """Tensors and Dynamic neural networks in Python with strong GPU acceleration"""

    homepage = "https://pytorch.org"
    url      = "https://github.com/pytorch/pytorch"

    version('1.0.1', commit='18eef1d8d96bf893c86b2259d4012267e4141e4b',
            submodules=True, git="https://github.com/pytorch/pytorch")

    depends_on('py-setuptools')
    depends_on('py-numpy')
    depends_on('py-pyyaml')
    depends_on('py-cffi')
    depends_on('py-typing')

    # Disable -Werror in ideep
    patch('disable_ideep_werror.patch')

    def install(self, spec, prefix):
        env['CMAKE_PREFIX_PATH'] = prefix
        env['NO_FBGEMM']='1' # disable SSE/AVX stuff
        python = which('python')
        python('setup.py', 'install', '--prefix={}'.format(prefix))
