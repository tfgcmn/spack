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


class PyPynn(PythonPackage):
    """A Python package for simulator-independent specification of neuronal network models"""

    homepage = "http://neuralensemble.org/PyNN/"
    url      = "https://pypi.python.org/packages/63/c8/be19667dc36adb28bf4ad86c0692d5454eb537ff6fa07b21ca4754fb0b21/PyNN-0.7.5.tar.gz#md5=d8280544e4c9b34b40fd372b16342841"

    version('0.7.5', 'd8280544e4c9b34b40fd372b16342841')
    version('0.8.1', '7fb165ed5af35a115cb9c60991645ae6', url='https://pypi.python.org/packages/43/30/291dab827c99068ca33a7d3dbfe5927bcfe0338556054bf850334e723931/PyNN-0.8.1.tar.gz')
    version('0.8beta', git='https://github.com/NeuralEnsemble/PyNN.git', commit='ffb0cb1661f2b0f2778db8f71865978fe7a7a6a4')

    depends_on('py-setuptools', type='build')
    depends_on('py-lazyarray@0.2.8:')
    depends_on('py-neo')

    # FIXME: variant for neuron and nest?
    # Neuron HAS to be loaded when installing nest --obreitwi
    # variant("neuron", default=False, description="Build with neuron")
    # depends_on("neuron", when="+neuron")

    # nest does not need variant, it is dynamically loaded via python

