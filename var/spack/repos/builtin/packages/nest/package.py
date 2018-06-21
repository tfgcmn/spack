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

    version('2.14.0', 'f484894d5cdcde68c96ff3e34c5d6c5c')
    version('2.12.0', '1ded6489466c6054abc0be230d97c424')
    version('2.10.0', 'e97371d8b802818c4a7de35276470c0c')
    version('2.8.0', '3df9d39dfce8a85ee104c7c1d8e5b337')
    version('2.6.0', 'ca7023c3a0ecb914ed2467d5d29265b0')
    version('2.4.2', 'c19db0280c9dd4219023ad96a62a4eda')
    version('2.4.2_custom_tso', 'c19db0280c9dd4219023ad96a62a4eda', url='https://github.com/nest/nest-simulator/releases/download/v2.4.2/nest-2.4.2.tar.gz')
    version('2.2.2', 'ced2d42091061973f6a18f0e5b97129f')

    # apply patches to specific versions
    patch('nest_2.4.2_tso.patch', when='@2.4.2_custom_tso')

    # only relevant variants
    variant("debug", default=False,
            description="Enable debugging symbols")
    variant("optimize", default=True,
            description="Enable compiler optimizations")
    variant("python", default=True,
            description="Build PyNest interface")
    variant("mpi", default=False,
            description="Build with MPI bindings")

    depends_on('libtool')

    # cmake to built new versions
    depends_on('cmake', type='build', when='@2.12.0:')
    # autotools to built old versions
    depends_on('automake', type='build', when='@:2.10.0')
    depends_on('autoconf', type='build', when='@:2.10.0')

    # there is a dependency on openMP but it is always satisfied in our cases
    depends_on("mpi", when="+mpi")

    depends_on("python", when="+python")
    depends_on("py-numpy", when="+python")

    depends_on("py-cython@0.19.2:", when="@2.12.0: +python")
    depends_on("py-nose", when="@2.12.0: +python")

    depends_on("doxygen", when="@2.12.0:")

    # technically these are optional dependencies, but we always want this!
    depends_on("gsl")
    depends_on("readline")

    extends("python", when="+python")
    depends_on("py-setuptools", when="+python", type="build")

    @when('@2.12.0:')
    def install(self, spec, prefix):
        """
            Install script for new tarballs after the switch to cmake.
        """
        cmake_args = [
            '-DCMAKE_INSTALL_PREFIX:PATH={0}'.format(prefix)
        ]

        for v in ["debug", "mpi", "optimize", "python"]:
            if spec.satisfies("+" + v):
                cmake_args.append("-Dwith-{}=ON".format(v))
            else:
                cmake_args.append("-Dwith-{}=OFF".format(v))

        cmake(*cmake_args)

        make()
        make("install")

        if spec.satisfies("@:2.14.0"):
            self.install_headers()

    @when('@:2.10.0')
    def install(self, spec, prefix):
        """
            Install script for old tarballs before the switch to cmake.
        """
        configure_args = [
                "CXXFLAGS=-std=c++03",
                "--prefix=%s" % prefix,
                "--with-openmp",
            ]

        if spec.satisfies("+optimize +debug"):
            raise InstallError("Version too low for optimized debug build.")

        for v in ["debug", "mpi", "python", "mpi"]:
            if spec.satisfies("+" + v):
                configure_args.append("--with-" + v)
            else:
                configure_args.append("--without-" + v)

        configure(*configure_args)

        make()
        make("install")

        self.install_headers()

    def install_headers(self):
        # copy source files to installation folder for older versions
        # (these are needed for modules to build against)
        # see https://github.com/nest/nest-simulator/pull/844
        path_headers = join_path(prefix, "include", "nest")

        mkdirp(path_headers)

        for suffix in ["h", "hpp"]:
            for f in find(
                    self.stage.source_path, "*.{}".format(suffix),
                    recurse=True):
                install(f, path_headers)

    def setup_environment(self, spack_env, run_env):
        run_env.set("NEST_INSTALL_DIR", self.spec.prefix)

