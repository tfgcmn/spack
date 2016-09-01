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

class Rr(Package):
    """application execution recorder, player and debugger"""
    homepage = "http://rr-project.org/"
    url      = "https://github.com/mozilla/rr/archive/4.3.0.tar.gz"

    version('4.3.0', '31470564e8b7eb317f619e4ef2244082')
    # version('4.2.0', 'f345b7b4e5b0d2babf1b919692f00c4d')
    # version('4.1.0', '8efb2e73326174573b61e317379a8cb1')
    # version('4.0.3', '4b0fd46bc85349bf598a7b2b9f70e021')
    # version('4.0.2', '919c518b164e7b6cef78ecc9e7e3ee6c')

    depends_on('cmake')
    depends_on('gdb')
    depends_on('git')
    depends_on('pkg-config')
    depends_on('py-pexpect')
    depends_on('zlib')

    # patch('do_not_install_rr_exec_stub.patch')
    def patch(self):
        # because otherwise CMake would try and fail to set RPATH of rr_exec_stub
        filter_file(
            r'^(install\(TARGETS .*)\s*rr_exec_stub', r'\1', 'CMakeLists.txt')

    def install(self, spec, prefix):
        cmake('.', '-Ddisable32bit=ON', '-DCMAKE_BUILD_TYPE=Release',
              *[arg for arg in std_cmake_args
                if not arg.startswith('-DCMAKE_BUILD_TYPE=')])

        make()
        make("install")
        mkdirp(prefix.bin)
        install('bin/rr_exec_stub', prefix.bin)
