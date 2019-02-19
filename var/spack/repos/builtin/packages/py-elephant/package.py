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
import sys


class PyElephant(PythonPackage):
    """Elephant is a package for analysis of electrophysiology data in Python
    """

    homepage = "http://neuralensemble.org/elephant"
    url      = "https://pypi.io/packages/source/e/elephant/elephant-0.3.0.tar.gz"

    version('0.5.0', 'fc64516556ac748cbfefa6d829a81f25')
    version('0.4.1', '0e6214c96cae6ce777e4b3cf29bbdaa9')
    version('0.3.0', '84e69e6628fd617af469780c30d2da6c')

    variant('doc', default=False, description='Build the documentation')
    variant('pandas', default=True, description='Build with pandas')
    variant('scikit', default=True, description='Build with scikit-learn')
    variant('spade', default=False, description='Build with prebuild spade')

    patch('deletefetches.patch')

    resource(name='fim364.so',
             url='http://www.borgelt.net/bin64/py3/fim.so',
             destination='.',
             placement='elephant/spade_src/fim364.so',
             sha256='67d556ed8e5a56c7e295845a239fbf36f8499a4c7216de9cd677d75c03cf5d29',
             when='^python@3:',
             expand=False)

    resource(name='fim264.so',
             url='http://www.borgelt.net/bin64/py2/fim.so',
             placement='elephant/spade_src/fim264.so',
             destination='.',
             sha256='2a33e222a214401c092b29a6144f3fb6455ac2d9d5635462300ab36eaac4e290',
             when='^python@:2.8',
             expand=False)

    resource(name='fim332.so',
             url='http://www.borgelt.net/bin32/py3/fim.so',
             placement='elephant/spade_src/fim332.so',
             destination='.',
             sha256='93e70b5e681d4661dda89fbc350b35b8c98d98a60c7ad0da3db15d66f50e324e',
             when='^python@3:',
             expand=False)

    resource(name='fim232.so',
             url='http://www.borgelt.net/bin32/py2/fim.so',
             placement='elephant/spade_src/fim232.so',
             destination='.',
             sha256='14f312d6b09a723d1c8dd162015cd5343721d66171a03cbc311926ec3b7d878f',
             when='^python@:2.8',
             expand=False)

    @run_before('build')
    def ensure_library(self):
        if not self.spec.satisfies('+spade'):
            return
        if self.spec.satisfies('^python@:2.8'):
            if sys.maxsize > 2**32:
                install('elephant/spade_src/fim264.so/fim.so', 'elephant/spade_src/fim.so')
            else:
                install('elephant/spade_src/fim232.so/fim.so', 'elephant/spade_src/fim.so')
        else:
            if sys.maxsize > 2**32:
                install('elephant/spade_src/fim364.so/fim.so', 'elephant/spade_src/fim.so')
            else:
                install('elephant/spade_src/fim332.so/fim.so', 'elephant/spade_src/fim.so')

    depends_on('py-setuptools',         type='build')
    depends_on('py-neo@0.3.4:',         type=('build', 'run'))  # > 0.3.3 ?
    depends_on('py-numpy@1.8.2:',       type=('build', 'run'))
    depends_on('py-quantities@0.10.1:', type=('build', 'run'))
    depends_on('py-scipy@0.14.0:',      type=('build', 'run'))
    depends_on('py-six@1.10.0:',      type=('build', 'run'))
    depends_on('py-pandas@0.14.1:',     type=('build', 'run'), when='+pandas')
    depends_on('py-scikit-learn',       type=('build', 'run'), when='+scikit')
    depends_on('py-numpydoc@0.5:',      type=('build', 'run'), when='+docs')
    depends_on('py-sphinx@1.2.2:',      type=('build', 'run'), when='+docs')
    depends_on('py-nose@1.3.3:',        type=('build', 'run')) # tests
