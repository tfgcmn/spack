# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PySqlalchemy(PythonPackage):
    """The Python SQL Toolkit and Object Relational Mapper"""

    homepage = 'http://www.sqlalchemy.org/'
    url      = "https://pypi.io/packages/source/S/SQLAlchemy/SQLAlchemy-1.0.12.tar.gz"

    version('1.3.1', 'b3d3be3e83d2f4893dd33bbbe83bd402')
    version('1.0.12', '6d19ef29883bbebdcac6613cf391cac4')

    depends_on('py-setuptools', type='build')
