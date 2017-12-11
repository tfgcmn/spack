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


class Rtags(CMakePackage):
    """RTags is a client/server application that indexes C/C++ code"""

    homepage = "https://github.com/Andersbakken/rtags/"
    url      = "https://andersbakken.github.io/rtags-releases/rtags-2.14.tar.gz"

    version('2.16', 'e0415b22e779519e5bb3250a33105e57')
    version('2.14', 'c52fd1d6241c3ec14dc87c3dcafd8ba3')

    depends_on("llvm@3.3: +clang")
    depends_on("zlib")
    depends_on("openssl")
    depends_on("lua@5.3:")
    # FIXME: removed for versions > 2.14 because this pulls in bash as a dependency...
    depends_on("bash-completion", when="@:2.14")
    depends_on("pkgconfig", type='build')

    def cmake_args(self):
        args = ['-DCMAKE_EXPORT_COMPILE_COMMANDS=1',
                '-DRTAGS_NO_ELISP_FILES=1',
                ]
        return args
