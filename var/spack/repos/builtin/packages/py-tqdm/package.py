# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyTqdm(PythonPackage):
    """A Fast, Extensible Progress Meter"""

    homepage = "https://github.com/tqdm/tqdm"
    url      = "https://pypi.io/packages/source/t/tqdm/tqdm-4.36.1.tar.gz"

    version('4.36.1', sha256='abc25d0ce2397d070ef07d8c7e706aede7920da163c64997585d42d3537ece3d')
    version('4.31.1', sha256='e22977e3ebe961f72362f6ddfb9197cc531c9737aaf5f607ef09740c849ecd05')
    version('4.8.4',  sha256='bab05f8bb6efd2702ab6c532e5e6a758a66c0d2f443e09784b73e4066e6b3a37')

    depends_on('python@2.6:2.8,3.2:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-nose', type='test')
    depends_on('py-flake8', type='test')
    depends_on('py-coverage', type='test')
