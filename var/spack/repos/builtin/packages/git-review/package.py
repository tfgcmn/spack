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
import os

class GitReview(Package):
    """git-review is a tool that helps submitting git branches to gerrit for review"""

    homepage = "http://docs.openstack.org/infra/git-review"
    #url      = "https://github.com/openstack-infra/git-review/archive/1.25.0.tar.gz"
    url      = "https://pypi.python.org/packages/92/38/b97fee6752540a92f44e405a51c53d3c36b5d57e139683862597b09a5c6c/git-review-1.25.0.tar.gz"

    version('1.25.0', 'd090605cbbd125d8a01693692d39bc70')
    version('1.24'  , '145116fe58a3487c3ad1bf55538fd741')
    version('1.23'  , 'b0023ad8c037ab710da81412194c6a3a')
    version('1.22'  , 'e889df5838c059362e5e0d411bde9c48')
    version('1.21'  , 'eee88bdef1aa37a55cc8becd48c6aba9')

    extends('python')

    depends_on('py-setuptools',    type=nolink) # also needed during runtime
    depends_on('py-pbr',           type='build')
    depends_on('py-requests@1.1:', type=nolink)
    depends_on('git',              type=nolink)
    depends_on('tk',               type=nolink)

    def install(self, spec, prefix):
	os.environ['PBR_VERSION'] = str(spec.version)
        setup_py('install', '--prefix={0}'.format(prefix))
