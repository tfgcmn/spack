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

class VisionaryNest(CMakePackage):
    """This repository contains many NEST models developed within the
    electronic vision(s) group, compiled into a single nest module."""

    url = "ssh://git@gitviz.kip.uni-heidelberg.de/model-visionary-nest.git"

    version('master', git=url, branch="master")

    depends_on('nest@2.14.0:')

    def cmake_args(self):
        args = ["-DCMAKE_CXX_FLAGS=-I{}".format(
                join_path(self.specs["nest"].prefix))]
        return args

    def setup_environment(self, spack_env, run_env):
        run_env.append_path("NEST_MODULES", "visionarymodule")
