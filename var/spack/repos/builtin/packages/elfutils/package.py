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


class Elfutils(AutotoolsPackage):
    """elfutils is a collection of various binary tools such as
    eu-objdump, eu-readelf, and other utilities that allow you to
    inspect and manipulate ELF files. Refer to Table 5.Tools Included
    in elfutils for Red Hat Developer for a complete list of binary
    tools that are distributed with the Red Hat Developer Toolset
    version of elfutils."""

    homepage = "https://fedorahosted.org/elfutils/"

    version('0.163',
            git='http://git.fedorahosted.org/git/elfutils.git',
            tag='elfutils-0.163')

    provides('elf')
    depends_on('flex')  # needed in maintainer mode

    def autoreconf(self, spec, prefix):
        autoreconf = which('autoreconf')
        autoreconf('-if')

    def configure_args(self):
        return ['--enable-maintainer-mode']
