# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyjwt(PythonPackage):
    """JSON Web Token implementation in Python"""

    homepage = "https://github.com/jpadilla/pyjwt"
    url      = "https://pypi.io/packages/source/P/PyJWT/PyJWT-1.4.0.tar.gz"

    version('1.4.0', sha256='e1b2386cfad541445b1d43e480b02ca37ec57259fd1a23e79415b57ba5d8a694')

    depends_on('py-setuptools', type='build')
    depends_on('py-pytest@4:4.99',        type='test')
    depends_on('py-pytest-cov@2.6.0:2.99.99',        type='test')
    depends_on('py-pytest-runner@4.2.0:45.99.99',        type='test')
