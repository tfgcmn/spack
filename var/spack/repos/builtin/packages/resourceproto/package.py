# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Resourceproto(AutotoolsPackage):
    """X Resource Extension.

    This extension defines a protocol that allows a client to query the
    X server about its usage of various resources."""

    homepage = "http://cgit.freedesktop.org/xorg/proto/resourceproto"
    url      = "https://www.x.org/archive/individual/proto/resourceproto-1.2.0.tar.gz"

    version('1.2.0', sha256='469029d14fdeeaa7eed1be585998ff4cb92cf664f872d1d69c04140815b78734')

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
