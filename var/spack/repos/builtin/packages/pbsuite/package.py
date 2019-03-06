# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pbsuite(Package):
    """PBJelly is a highly automated pipeline that aligns long sequencing
       reads (such as PacBio RS reads or long 454 reads in fasta format)
       to high-confidence draft assembles."""

    homepage = "https://sourceforge.net/p/pb-jelly/wiki/Home/"
    url      = "https://downloads.sourceforge.net/project/pb-jelly/PBSuite_15.8.24.tgz"

    version('15.8.24', sha256='1be082faa62cb3f701c78498db8544c844c3d6d3e3524fecf00a12e82a97e12b')

    depends_on('blasr@1.3.1:', type='run')
    depends_on('python@2.7:', type='run')
    depends_on('py-networkx@1.1:', type='run')

    def install(self, spec, prefix):
        install_tree('pbsuite', prefix.pbsuite)
        install_tree('bin', prefix.bin)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PYTHONPATH', self.prefix)
