# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyDeprecated(PythonPackage):
    """Python @deprecated decorator to deprecate old python classes, functions or methods."""

    homepage = "https://github.com/tantale/deprecated"
    url      = "https://pypi.io/packages/source/D/Deprecated/Deprecated-1.2.4.tar.gz"

    version('1.2.4', sha256='b784e0ca85a8c1e694d77e545c10827bd99772392e79d5f5442e761515a1246e')

    depends_on('python@2.7:2.8,3.4:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-wrapt@1:1.999',        type=('build', 'run'))
