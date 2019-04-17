# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack import *


class PyNbconvert(PythonPackage):
    """Jupyter Notebook Conversion"""

    homepage = "https://github.com/jupyter/nbconvert"
    url      = "https://github.com/jupyter/nbconvert/archive/4.2.0.tar.gz"

    version('5.4.1', '2da47f215c9cc4f10e3aa1a45c9317f9')
    version('4.2.0', '8bd88771cc00f575d5edcd0b5197f964')
    version('4.1.0', '06655576713ba1ff7cece2b92760c187')
    version('4.0.0', '9661620b1e10a7b46f314588d2d0932f')

    depends_on('py-pycurl', type='build')
    depends_on('python@2.7:2.8,3.3:')
    depends_on('py-mistune@0.8.1:', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'))
    depends_on('py-pygments', type=('build', 'run'))
    depends_on('py-traitlets@4.2:', type=('build', 'run'))
    depends_on('py-jupyter-core', type=('build', 'run'))
    depends_on('py-nbformat@4.4:', type=('build', 'run'))
    depends_on('py-entrypoints@0.2.2:', type=('build', 'run'))
    depends_on('py-tornado', type=('build', 'run'))
    depends_on('py-jupyter-client', type=('build', 'run'))

    depends_on('py-setuptools', type='build', when='@5:')
    depends_on('py-bleach', type=('build', 'run'), when='@5:')
    depends_on('py-pandocfilters', type=('build', 'run'), when='@5:')
    depends_on('py-defusedxml', type=('build', 'run'), when='@5:')
    depends_on('py-testpath', type=('build', 'run'), when='@5:')

    def patch(self):
        # We bundle this with the spack package so that the installer
        # doesn't try to download it.
        install(os.path.join(self.package_dir, 'style.min.css'),
                os.path.join('nbconvert', 'resources', 'style.min.css'))
