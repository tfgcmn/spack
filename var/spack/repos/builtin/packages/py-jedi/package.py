# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyJedi(PythonPackage):
    """An autocompletion tool for Python that can be used for text editors."""

    homepage = "https://github.com/davidhalter/jedi"
    url      = "https://pypi.io/packages/source/j/jedi/jedi-0.9.0.tar.gz"

    # unfortunately pypi.io only offers a .whl
    version('0.13.2', '451d3244896588b298dbc622fd461201',
                url='https://github.com/davidhalter/jedi/archive/v0.13.2.tar.gz')
    version('0.12.1', '49a94ffb781c1383e8542ca5f71cebf0',
                url='https://github.com/davidhalter/jedi/archive/v0.12.1.tar.gz')
    version('0.12.0', '8947d4d0201f857743da93c8bbf3889a',
                url='https://github.com/davidhalter/jedi/archive/v0.12.0.tar.gz')
    version('0.10.0', '89ed853d4a283bfa0fdbcf688b4d35fe',
                url='https://github.com/davidhalter/jedi/archive/v0.10.0.tar.gz')
    version('0.9.0', '2fee93d273622527ef8c97ac736e92bd')

    depends_on('py-setuptools', type='build')
    depends_on('py-parso', type=('build', 'run'), when='@0.12.1:')
