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


class PyFasteners(Package):
    """A python package that provides useful locks."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/harlowja/fasteners"
    url      = "https://pypi.python.org/packages/f4/6f/41b835c9bf69b03615630f8a6f6d45dafbec95eb4e2bb816638f043552b2/fasteners-0.14.1.tar.gz#md5=fcb13261c9b0039d9b1c4feb9bc75e04"

    version('0.14.1', 'fcb13261c9b0039d9b1c4feb9bc75e04')

    extends('python')

    depends_on('py-setuptools', type='build')
    depends_on('py-monotonic',  type=nolink)

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
