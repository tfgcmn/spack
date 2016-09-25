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


class PySpykeviewer(Package):
    """A multi-platform GUI application for navigating, analyzing and visualizing electrophysiological datasets"""

    homepage = "https://github.com/rproepp/spykeviewer"
    url      = "https://pypi.python.org/packages/38/52/916cf5f0776d9970ef8aba5fae8aefccb309098669bff03d242b8b2b28da/spykeviewer-0.4.4.tar.gz"

    version('0.4.4', '08737c4a3cb6de9bef96a9a06acf6224')

    extends('python')

    depends_on('py-setuptools',         type='build')
    depends_on('py-guidata',            type=nolink)
    depends_on('py-guiqwt@2.1.4:3.9.9', type=nolink)

    # spyderlib was renamed to spyder in 3.0...
    depends_on('py-spyder@2.1.0:2.9.9', type=nolink, when='@:0.4.4')

    depends_on('py-spykeutils@0.4.0:',  type=nolink)
    depends_on('py-neo@0.2.1:',         type=nolink)
    depends_on('py-matplotlib',         type=nolink)
    depends_on('py-scipy',              type=nolink)
    depends_on('py-pytables',              type=nolink)

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
