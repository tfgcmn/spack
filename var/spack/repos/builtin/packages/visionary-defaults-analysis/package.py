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


class VisionaryDefaultsAnalysis(Package):
    """Visionary Meta Package"""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack-visions/archive/master.tar.gz'
    version('1.0', git='https://github.com/electronicvisions/spack-visions.git')


    depends_on('python')

    depends_on('py-attrs')
    depends_on('py-autopep8')
    depends_on('py-cython')
    depends_on('py-doxypy')
    depends_on('py-flake8')
    depends_on('py-html5lib')
    depends_on('py-ipython')
    depends_on('py-jedi')
    depends_on('py-junit-xml')
    depends_on('py-jupyter-notebook')
    depends_on('py-line-profiler')
    depends_on('py-lmfit')
    depends_on('py-matplotlib')
    depends_on('py-nose')
    depends_on('py-numpy')
    depends_on('py-pandas')
    depends_on('py-pillow')
    depends_on('py-pip')
    depends_on('py-pylint')
    depends_on('py-pylint', when='@0.2.11:')
    depends_on('py-pytest')
    depends_on('py-pytest-xdist')
    depends_on('py-pyyaml')
    depends_on('py-scikit-image')
    depends_on('py-scipy')
    depends_on('py-seaborn')
    depends_on('py-setuptools')
    depends_on('py-sphinx')
    depends_on('py-sqlalchemy')
    depends_on('py-statsmodels')
    depends_on('py-symfit')
    depends_on('py-sympy')
    depends_on('py-tabulate')
    depends_on('py-virtualenv')
    depends_on('py-xmlrunner')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-defaults.py'))

        # we could create some filesystem view here?
