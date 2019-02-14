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


class PyRegex(PythonPackage):
    """Alternative regular expression module, to replace re."""

    homepage = "https://pypi.python.org/pypi/regex/"
    url      = "https://pypi.io/packages/source/r/regex/regex-2017.07.11.tar.gz"

    version('2019.02.07', 'b887ba08ec75564463791013cb1465f1')
    version('2018.01.10', '318e5c65deeb05a00f0b63d2189d2e7e')
    version('2017.07.11', '95f81ebb5273c7ad9a0c4d1ac5a94eb4')

    depends_on('py-setuptools', type='build')
