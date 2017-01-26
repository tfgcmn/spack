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


class PyHttpbin(Package):
    """HTTP Request and Response Service"""

    homepage = "https://github.com/Runscope/httpbin"
    url      = "https://pypi.python.org/packages/61/8d/2e5b787a3381ff6c380cd05a0d0bc3d97888299704294ae198e90693c4cd/httpbin-0.5.0.tar.gz#md5=923793df99156caa484975ade96ee115"

    version('0.5.0', '923793df99156caa484975ade96ee115')

    extends('python')

    depends_on('py-setuptools',         type='build')
    depends_on('py-decorator@3.4.0:',   type=nolink)
    depends_on('py-flask@0.10.1:',      type=nolink)
    #depends_on('py-gevent@1.0.2:',      type=nolink)
    #depends_on('py-greenlet@0.4.2:',    type=nolink)
    #depends_on('py-gunicorn@19.2:',     type=nolink)
    depends_on('py-itsdangerous@0.24:', type=nolink)
    #depends_on('py-jinja2@2.7.2:',      type=nolink)
    depends_on('py-markupsafe@0.23:',   type=nolink)
    depends_on('py-six@1.6.1:',         type=nolink)
    #depends_on('py-werkzeug@0.9.4:',    type=nolink)

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
