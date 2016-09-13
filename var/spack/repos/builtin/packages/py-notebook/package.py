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


class PyNotebook(Package):
    """A web-based notebook environment for interactive computing"""

    homepage = "http://jupyter.org"
    url      = "https://pypi.python.org/packages/10/81/6b015a84e4bfdf7908b1f6282de0adbc7e4b251f456f62290be5a953ab8e/notebook-4.2.2.tar.gz#md5=d951ac8776154eb56e041011aa093d0a"

    version('4.2.2', 'd951ac8776154eb56e041011aa093d0a')

    extends('python')

    # FIXME: Add additional dependencies if required.
    # depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=nolink)
    #mock; python_version == "2.7" and extra == 'test'
    #requests; extra == 'test'
    #nose; extra == 'test'
    #Sphinx (>=1.1); extra == 'doc'

    depends_on('py-terminado@0.3.3:', type=nolink)
    depends_on('py-traitlets',        type=nolink)
    depends_on('py-tornado@4:',       type=nolink)
    depends_on('py-nbformat',         type=nolink)
    depends_on('py-nbconvert',        type=nolink)
    depends_on('py-jupyter_core',     type=nolink)
    depends_on('py-jupyter_client',   type=nolink)
    depends_on('py-jinja2',           type=nolink)
    depends_on('py-ipython_genutils', type=nolink)
    depends_on('py-ipykernel',        type=nolink)


    def install(self, spec, prefix):
        # FIXME: Add logic to build and install here.
        setup_py('install', '--prefix={0}'.format(prefix))
