# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import spack.architecture


class Pmix(AutotoolsPackage):
    """The Process Management Interface (PMI) has been used for quite some
       time as a means of exchanging wireup information needed for
       interprocess communication. However, meeting the significant
       orchestration challenges presented by exascale systems requires
       that the process-to-system interface evolve to permit a tighter
       integration between the different components of the parallel
       application and existing and future SMS solutions.

       PMI Exascale (PMIx) addresses these needs by providing an extended
       version of the PMI definitions specifically designed to support
       exascale and beyond environments by: (a) adding flexibility to the
       functionality expressed in the existing APIs, (b) augmenting the
       interfaces with new APIs that provide extended capabilities, (c)
       forging a collaboration between subsystem providers including
       resource manager, fabric, file system, and programming library
       developers, (d) establishing a standards-like body for maintaining
       the definitions, and (e) providing a reference implementation of the
       PMIx standard that demonstrates the desired level of scalability
       while maintaining strict separation between it and the standard
       itself."""

    homepage = "https://pmix.org"
    url      = "https://github.com/pmix/pmix/releases/download/v3.1.2/pmix-3.1.2.tar.bz2"
    maintainers = ['rhc54']

    version('3.1.2',    sha256='28aed0392d4ca2cdfbdd721e6210c94dadc9830677fea37a0abe9d592c00f9c3')
    version('3.0.2',    sha256='df68f35a3ed9517eeade80b13855cebad8fde2772b36a3f6be87559b6d430670')
    version('3.0.1',    sha256='b81055d2c0d61ef5a451b63debc39c820bcd530490e2e4dcb4cdbacb618c157c')
    version('3.0.0',    sha256='ee8f68107c24b706237a53333d832445315ae37de6773c5413d7fda415a6e2ee')
    version('2.2.2',    sha256='cd951dbda623fadc5b32ae149d8cc41f9462eac4d718d089340911b1a7c20714')
    version('2.1.4',    sha256='eb72d292e76e200f02cf162a477eecea2559ef3ac2edf50ee95b3fe3983d033e')
    version('2.1.3',    sha256='281283133498e7e5999ed5c6557542c22408bc9eb51ecbcf7696160616782a41')
    version('2.1.2',    sha256='94bb9c801c51a6caa1b8cef2b85ecf67703a5dfa4d79262e6668c37c744bb643')
    version('2.0.1',    'ba3193b485843516e6b4e8641e443b1e')
    version('1.2.5',    'c3d20cd9d365a813dc367afdf0f41c37')

    depends_on('libevent@2.0.20:2.0.22,2.1.8')
    depends_on('hwloc@1.11.0:1.11.99,2.0.1:', when='@3.0.0:')

    def configure_args(self):

        spec = self.spec
        config_args = [
            '--enable-shared',
            '--enable-static'
        ]

        # libevent support
        config_args.append(
            '--with-libevent={0}'.format(spec['libevent'].prefix))

        # Versions < 2.1.1 have a bug in the test code that *sometimes*
        # causes problems on strict alignment architectures such as
        # aarch64.  Work-around is to just not build the test code.
        if 'aarch64' in spack.architecture.sys_type() and \
           self.spec.version < Version('2.1.1'):
            config_args.append('--without-tests-examples')

        # Versions >= 3.0 also use hwloc
        if self.spec.version >= Version('3.0.0'):
            config_args.append('--with-hwloc={0}'.format(spec['hwloc'].prefix))

        return config_args
