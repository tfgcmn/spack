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

class Nest(Package):
    """Nest simulator"""

    homepage = "http://www.nest-simulator.org"
    url = "https://github.com/nest/nest-simulator/releases/download/v2.10.0/nest-2.10.0.tar.gz"
    list_url = "http://www.nest-simulator.org/download"
    list_depth = 2

    version('2.10.0', 'e97371d8b802818c4a7de35276470c0c')
    version('2.8.0', '3df9d39dfce8a85ee104c7c1d8e5b337')
    version('2.6.0', 'ca7023c3a0ecb914ed2467d5d29265b0')
    version('2.4.2', 'c19db0280c9dd4219023ad96a62a4eda')

    # only relevant variants
    variant("debug", default=False,
            description="Enable debugging symbols")
    variant("optimize", default=True,
            description="Enable compiler optimizations")
    variant("python", default=True,
            description="Build PyNest interface")
    variant("mpi", default=False,
            description="Build with MPI bindings")

    # there is a dependency on openMP but it is always satisfied in our cases
    depends_on("mpi", when="+mpi")

    depends_on("python", when="+python")
    depends_on("py-numpy", when="+python")

    # technically these are optional dependencies, but we always want this!
    depends_on("gsl")
    depends_on("readline")

    extends("python", when="+python")


    @when('@:2.10.0')
    def install(self, spec, prefix):
        """
            Install script for old tarballs before the switch to cmake.
        """
        configure_args = [
                '--prefix=%s' % prefix,
                "--with-openmp",
                "--with-python"
            ]

        if spec.satisfies("+optimize +debug"):
            raise InstallError("Version too low for optimized debug build.")

        for v in ["debug", "mpi"]:
            if spec.satisfies("+" + v):
                configure_args.append("--with-" + v)
            else:
                configure_args.append("--without-" + v)

        configure(*configure_args)

        make()
        make("install")

    def setup_environment(self, spack_env, run_env):
        run_env.set("NEST_INSTALL_DIR", self.spec.prefix)

