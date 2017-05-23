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


class BundleTools(Package):
    """Tools Meta Package"""

    homepage = None
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack-visions/archive/master.tar.gz'
    version('0.1', git='https://github.com/electronicvisions/spack-visions.git')

    depends_on('vim', when='@:0.2.1')
    depends_on('vim +python +cscope +ruby +huge', when='@0.2.2:0.2.5')
    depends_on('vim +python +ruby +lua +perl +cscope +huge', when='@0.2.6:')

    depends_on('emacs ~X')
    depends_on('tmux')
    depends_on('ncdu')
    depends_on('units')
    depends_on('ranger', when='@:0.2.7')
    depends_on('py-ranger', when='@0.2.8:')

    depends_on('mosh', when='@0.2:')

    depends_on('mercurial')
    depends_on('git')
    depends_on('git-review', when='@:0.2.7')
    depends_on('py-git-review', when='@0.2.8:')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-defaults.py'))

        # we could create some filesystem view here?
