# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyLineProfiler(PythonPackage):
    """Line-by-line profiler."""

    homepage = "https://github.com/rkern/line_profiler"
    url      = "https://pypi.io/packages/source/l/line_profiler/line_profiler-2.0.tar.gz"

    version('2.1.2', sha256='efa66e9e3045aa7cb1dd4bf0106e07dec9f80bc781a993fbaf8162a36c20af5c',
            url='https://pypi.io/packages/source/l/line_profiler/line_profiler-2.1.2.tar.gz')
    version('2.0', 'fc93c6bcfac3b7cb1912cb28836d7ee6')

    depends_on('python@2.5:')
    depends_on('py-setuptools',     type='build')
    depends_on('py-cython',         type='build')
    depends_on('py-ipython@0.13:',  type=('build', 'run'))

    @when("^python@3.7.0:")
    @run_before("build")
    def regenerate_cython_sources(self):
        """The sources include pre-generated cython code that does not work for
        newer python versions."""
        cython = which('cython')
        cython('_line_profiler.pyx')
