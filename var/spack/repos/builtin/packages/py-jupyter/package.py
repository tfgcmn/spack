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


class PyJupyter(Package):
    """Jupyter metapackage. Install all the Jupyter components in one go."""

    homepage = "http://ipython.org"
    url      = "https://pypi.python.org/packages/c9/a9/371d0b8fe37dd231cf4b2cff0a9f0f25e98f3a73c3771742444be27f2944/jupyter-1.0.0.tar.gz"

    version('1.0.0', 'c6030444c7eb6c05a4d7b1768c72aed7')

    extends('python', ignore=r'lib/python2.7/site-packages/jupyter.py*')

    depends_on('py-setuptools',      type='build')
    depends_on('py-notebook',        type=nolink)
    depends_on('py-qtconsole',       type=nolink)
    depends_on('py-jupyter_console', type=nolink)
    depends_on('py-nbconvert',       type=nolink)
    depends_on('py-ipykernel',       type=nolink)
    depends_on('py-ipywidgets',      type=nolink)

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
