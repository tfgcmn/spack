# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Flatbuffers(CMakePackage):
    """Memory Efficient Serialization Library
    """

    homepage = "http://google.github.io/flatbuffers/"
    url      = "https://github.com/google/flatbuffers/archive/v1.9.0.tar.gz"

    version('1.10.0', sha256='3714e3db8c51e43028e10ad7adffb9a36fc4aa5b1a363c2d0c4303dd1be59a7c')
    version('1.9.0', sha256='5ca5491e4260cacae30f1a5786d109230db3f3a6e5a0eb45d0d0608293d247e3')
    version('1.8.0', sha256='c45029c0a0f1a88d416af143e34de96b3091642722aa2d8c090916c6d1498c2e')
