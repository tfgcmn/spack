# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyTerminado(PythonPackage):
    """Terminals served to term.js using Tornado websockets"""

    homepage = "https://pypi.python.org/pypi/terminado"
    url      = "https://pypi.io/packages/source/t/terminado/terminado-0.6.tar.gz"

    version('0.8.2', sha256='de08e141f83c3a0798b050ecb097ab6259c3f0331b2f7b7750c9075ced2c20c2')
    version('0.8.1', sha256='55abf9ade563b8f9be1f34e4233c7b7bde726059947a593322e8a553cc4c067a')
    version('0.6', sha256='2c0ba1f624067dccaaead7d2247cfe029806355cef124dc2ccb53c83229f0126')

    depends_on('py-tornado@4:', type=('build', 'run'))
    depends_on('py-ptyprocess', type=('build', 'run'))
