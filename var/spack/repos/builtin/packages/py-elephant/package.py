# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys


class PyElephant(PythonPackage):
    """Elephant is a package for analysis of electrophysiology data in Python
    """

    homepage = "http://neuralensemble.org/elephant"
    url      = "https://pypi.io/packages/source/e/elephant/elephant-0.3.0.tar.gz"

    version('0.5.0', sha256='eeedc58f49200b158a9be329015c8dd562450b3c2aa01fdcd92375aca80e461c')
    version('0.4.1', sha256='86b21a44cbacdc09a6ba6f51738dcd5b42ecd553d73acb29f71a0be7c82eac81')
    version('0.3.0', sha256='747251ccfb5820bdead6391411b5faf205b4ddf3ababaefe865f50b16540cfef')

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
             sha256='9fabf43d0a5b6b2c0d8b5cb78c23af591a059c160a9b7f7831e64c09e60b8465',
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
             sha256='1ecc4d63af01005a530ab4a19be177d30be31aea7626c4a168610f1680c26401',
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
    depends_on('py-six@1.10.0:',        type=('build', 'run'))
    depends_on('py-pandas@0.14.1:',     type=('build', 'run'), when='+pandas')
    depends_on('py-scikit-learn',       type=('build', 'run'), when='+scikit')
    depends_on('py-numpydoc@0.5:',      type=('build', 'run'), when='+docs')
    depends_on('py-sphinx@1.2.2:',      type=('build', 'run'), when='+docs')
    depends_on('py-nose@1.3.3:',        type='test')
