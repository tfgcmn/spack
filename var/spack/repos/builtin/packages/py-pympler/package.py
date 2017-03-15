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


class PyPympler(PythonPackage):
    """ 
	Development tool to measure, monitor and analyze the memory behavior 
        of Python objects in a running Python application.
    """

    homepage = "https://github.com/pympler/pympler"
    url      = "https://github.com/pympler/pympler/archive/0.4.3.tar.gz"

    version('0.4.3', 'd39b0adc1c0cbdc6fe40346b3ae8da83')
    version('0.4.2', 'ca4e208ee17add61092027e0f810796a')
    version('0.4.1', '90bb5d8958bffc3b6ca898cbafc4e54a')
    version('0.4'  , '97cfc50a9f60795dedfc9599c5c5c4e5')
    version('0.3.1', '09ed34c619925756230b4b3d69806a3a')
