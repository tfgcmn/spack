##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-doxypy
#
# You can edit this file again by typing:
#
#     spack edit py-doxypy
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyDoxypy(Package):
    """doxypy is an input filter for Doxygen."""

    homepage = "https://pypi.python.org/pypi/doxypy"
    url      = "http://pypi.python.org/packages/b9/05/e0bbd4b5fcbf17b9d9c93d2da748667f4a2f21ad02730919fce0bbe3d3a6/doxypy-0.3.tar.gz"

    version('0.3', '3b52289e0962d31b92af8be0eef8cbb2')

    extends('python')
    
    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
