# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class VisionaryExa(Package):
    """Visionary Meta Package - software needed for EXA (machine learning using
    hagen mode)"""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    variant("dev", default=True, description="With visionary-dev-tools")

    depends_on('visionary-dls~gccxml+dev', when="+dev")  # let's try without gccxml for now
    depends_on('visionary-dls~gccxml~dev', when="~dev")  # let's try without gccxml for now
    # TODO Re-enable once https://github.com/spack/spack/pull/13112 is merged
    #  depends_on('tensorflow')
    depends_on('py-pandas')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-dls.py'))

        # we could create some filesystem view here?
