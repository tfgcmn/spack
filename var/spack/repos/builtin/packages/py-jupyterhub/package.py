# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyJupyterhub(PythonPackage):
    """Multi-user server for Jupyter notebooks."""

    homepage = "https://pypi.org/project/jupyterhub"
    url      = "https://pypi.io/packages/source/j/jupyterhub/jupyterhub-0.9.4.tar.gz"

    version('0.9.4',    sha256='7848bbb299536641a59eb1977ec3c7c95d931bace4a2803d7e9b28b9256714da')

    depends_on('python@3.5:')
    depends_on('node-js', type=('build', 'run'))
    depends_on('npm', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-python-dateutil', type='run')
    depends_on('py-jinja2', type='run')
    depends_on('py-sqlalchemy@1.1:', type='run')
    depends_on('py-tornado@5.0:', type='run')
    depends_on('py-traitlets@4.3.2:', type='run')
    depends_on('py-alembic', type='run')
    depends_on('py-mako', type='run')
    depends_on('py-async-generator@1.8:', type='run')
    depends_on('py-jupyter-notebook', type='run')
    depends_on('py-prometheus-client@0.0.21:', type='run')
    depends_on('py-send2trash', type='run')
    depends_on('py-requests', type='run')
    depends_on('py-python-oauth2', type='run')
    depends_on('py-pamela', type='run')
#    depends_on('py-certipy@0.1.2:', type='run')

    @run_after('install')
    def install_npm_dependency(self):
        with working_dir(self.prefix):
            npm = Executable('npm')
            npm('install', 'configurable-http-proxy', '-g', '--prefix={0}'.format(self.spec.prefix))
