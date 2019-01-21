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


class PyConfigargparse(PythonPackage):
    """A drop-in replacement for argparse that allows options to also be set
       via config files and/or environment variables."""

    homepage = "https://pypi.org/project/ConfigArgParse"
    url      = "https://pypi.io/packages/source/C/ConfigArgParse/ConfigArgParse-0.14.0.tar.gz"

    version('0.14.0', sha256='2e2efe2be3f90577aca9415e32cb629aa2ecd92078adbe27b53a03e53ff12e91')

    depends_on('py-setuptools', type='build')
    depends_on('py-pyyaml',     type=('build', 'run'))
