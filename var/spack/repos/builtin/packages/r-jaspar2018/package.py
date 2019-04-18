# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RJaspar2018(RPackage):
    """Data package for JASPAR 2018. To search this databases,
    please use the package TFBSTools (>= 1.15.6)."""

    homepage = "http://jaspar.genereg.net/"
    git      = "https://git.bioconductor.org/packages/JASPAR2018.git"

    version('1.0.0', commit='4c84092b3737bb1c57ab56f4321f2f5e4b0efeaa')

    depends_on('r@3.4.0:')