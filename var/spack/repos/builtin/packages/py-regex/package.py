# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyRegex(PythonPackage):
    """Alternative regular expression module, to replace re."""

    homepage = "https://pypi.python.org/pypi/regex/"
    url      = "https://pypi.io/packages/source/r/regex/regex-2017.07.11.tar.gz"

    version('2019.02.07', 'b887ba08ec75564463791013cb1465f1')
    version('2018.01.10', '318e5c65deeb05a00f0b63d2189d2e7e')
    version('2017.07.11', '95f81ebb5273c7ad9a0c4d1ac5a94eb4')

    depends_on('py-setuptools', type='build')
