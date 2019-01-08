# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-pygithub
#
# You can edit this file again by typing:
#
#     spack edit py-pygithub
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyPygithub(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://pypi.io/packages/source/P/PyGithub/PyGithub-1.43.4.tar.gz"

    version('1.43.4', sha256='5d3e3bdee80be63a1e5aaca5689ff450a4e7f7dfac728577fdb9caac080c5479')

    depends_on('python@2.7:2.8,3.4:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-requests@2.14.0:',        type=('build', 'run'))
    depends_on('py-pyjwt',        type=('build', 'run'))
    depends_on('py-deprecated',        type=('build', 'run'))
    depends_on('py-cryptography',        type=('build', 'run'))
