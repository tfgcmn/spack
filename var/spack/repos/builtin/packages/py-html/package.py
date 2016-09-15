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


class PyHtml(Package):
    """simple, elegant HTML, XHTML and XML generation"""

    homepage = "http://pypi.python.org/pypi/html"
    url      = "https://pypi.python.org/packages/4a/df/0e3d22d50ee43274eb5116f49972a164d853bb3ab305a69a0540b6292252/html-1.16.tar.gz"

    version('1.16', '39b9db7cdcc84607828be021172d441f')

    extends('python')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
