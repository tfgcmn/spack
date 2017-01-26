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


class PyBokeh(Package):
    """Statistical and novel interactive HTML plots for Python"""

    homepage = "http://github.com/bokeh/bokeh"
    url      = "https://pypi.python.org/packages/de/5d/88a95eacebbd863e77f78cc47152955c8afe28dc4ed1fe243fc3fb40ceb4/bokeh-0.12.2.tar.gz#md5=2d1621bffe6e2ab9d42efbf733861c4f"

    version('0.12.2', '2d1621bffe6e2ab9d42efbf733861c4f')

    extends('python')

    depends_on('py-setuptools',      type='build')
    depends_on('py-six@1.5.2:',      type=nolink)
    depends_on('py-requests@1.2.3:', type=nolink)
    depends_on('py-pyyaml@3.10:',    type=nolink)
    depends_on('py-dateutil@2.1:',   type=nolink)
    depends_on('py-jinja2@2.7:',     type=nolink)
    depends_on('py-numpy@1.7.1:',    type=nolink)
    depends_on('py-tornado@4.3:',    type=nolink)
    depends_on('py-pandas',          type=nolink)
    depends_on('py-bs4',             type=nolink)
    depends_on('py-nbformat',        type=nolink)
    depends_on('py-futures',         type=nolink)
    depends_on('py-flexx',           type=nolink)
    depends_on('py-notebook',        type=nolink)

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
