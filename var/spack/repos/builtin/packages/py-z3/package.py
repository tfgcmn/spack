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
from spack import *


class PyZ3(Package):
    """The Z3 Theorem Prover"""
    homepage = "https://github.com/Z3Prover/z3/"
    url      = "https://github.com/Z3Prover/z3/archive/z3-4.5.0.zip"

    version('4.5.0', 'ceee5d3c5f57f63d45afa2ef22aeceec')
    version('4.4.1', 'a8af97d99246b22d17f6fb6fb724c3ce')
    version('4.4.0', '3a1144dd48b756ce42c382f1cedc00c7')
    version('4.3.2', 'a1f238e2e6f762c1786aba1268077c0c')
    version('4.3.1', '0562ddd21ed52666cb69cadc6311d359')

    depends_on('cmake', type="build")

    def install(self, spec, prefix):
        python = which('python')
        python('contrib/cmake/bootstrap.py', 'create')
        with working_dir('build', create=True):
            cmake('..', *std_cmake_args)
            make()
            make('install')



