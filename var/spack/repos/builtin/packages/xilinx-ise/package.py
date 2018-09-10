##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
import os
import fnmatch
from spack import *


class XilinxIse(Package):
    """Xilinx Integrated Synthesis Environment for producing and analyzing
    HDL designs.

    Since the Xilinx installer available from [1] requires a graphical user
    interface, this package relies on tarballs of pre-installed binaries.
    These tarballs are to be supplied within a valid spack mirror as
    `xilinx-ise/xilinx-ise-labtools-147.tar.gz` and
    `xilinx-ise/xilinx-ise-designsuite-147.tar.gz`.
    Since these files are managed as spack resources, an additional empty
    top-level file has to be supplied: `xilinx-ise/xilinx-ise-147.None`.

    There is one build variant available: 'designsuite'. If enabled, the full
    ISE design suite is installed. If disabled, only LabTools as a minimal
    set of tools are installed.

    Note that this package does not install cable drivers: Since this operation
    requires root privileges, it has to be done manually.

    [1] https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/design-tools.html
    """

    homepage = 'https://www.xilinx.com/products/design-tools/ise-design-suite'

    # TODO: Remove this placeholder as soon as url variable is no longer needed
    url = 'http://mirroronly.package/xilinx-ise-147.None'

    version('147', '2d61fc2af2e98e944b5cbb4796f99966', expand=False)

    resource(name='xilinx-ise-labtools',
             url='http://mirroronly.package/xilinx-ise-labtools.tar.gz',
             md5='06a0c4089d9f0579947b5302d5656a7d',
             when='~designsuite')
    resource(name='xilinx-ise-designsuite',
             url='http://mirroronly.package/xilinx-ise-designsuite.tar.gz',
             md5='f3feacf7fc27700572d5c7b09ced10eb',
             when='+designsuite')

    variant('designsuite', default=False,
            description='Install the full ISE Design Suite instead of '
                        'LabTools only')

    depends_on('fontconfig', type='run')
    depends_on('glib', type='run')
    depends_on('libice', type='run')
    depends_on('libsm', type='run')
    depends_on('libxi', type='run')
    depends_on('libxrandr', type='run')
    depends_on('libxrender', type='run')
    depends_on('libxtst', type='run')
    depends_on('libxcursor', type='run')
    depends_on('libxft', type='run')

    def setup_environment(self, spack_env, run_env):
        """
        Xilinx ISE environment variables as defined in `/cad/modules/xilinx/147`
        """
        is64bit = self.spec.architecture.target == 'x86_64'
        lin = 'lin64' if is64bit else 'lin32'

        # --- License server (UHEI-KIP only!) --- #
        run_env.append_path('LM_LICENSE_FILE', '2100@phobos')

        # --- Common --- #
        run_env.set('XILINXinst', self.prefix)
        run_env.append_path('PATH',
                            join_path(self.prefix, 'common', 'bin', lin))
        run_env.append_path('LD_LIBRARY_PATH',
                            join_path(self.prefix, 'common', 'lib', lin))

        # --- LabTools --- #
        if self.spec.satisfies('~designsuite'):
            run_env.set('XILINX', join_path(self.prefix, 'LabTools'))
            run_env.append_path('PATH',
                                join_path(self.prefix, 'LabTools', 'bin', lin))
            run_env.append_path('LD_LIBRARY_PATH',
                                join_path(self.prefix, 'LabTools', 'lib', lin))

        # --- Full Design Suite --- #
        if self.spec.satisfies('+designsuite'):
            # -- EDK -- #
            edk = join_path(self.prefix, 'EDK')
            run_env.set('XILINX_EDK', edk)
            run_env.append_path('LD_LIBRARY_PATH', join_path(edk, 'lib', lin))
            run_env.append_path('PATH', join_path(edk, 'bin', lin))

            for arch in ['arm', 'microblaze', 'powerpc-eabi']:
                run_env.append_path('PATH',
                                    join_path(edk, 'gnu', arch, 'lin', 'bin'))

            # -- PlanAhead -- #
            pabase = join_path(self.prefix, 'PlanAhead')
            run_env.set('XILINX_PLANAHEAD', pabase)
            run_env.append_path('PATH', join_path(pabase, 'bin'))

            # -- ISE Design tools -- #
            xhome = join_path(self.prefix, 'ISE')
            run_env.set('XILINX', xhome)
            run_env.set('XILINX_DSP', xhome)

            lmc_home = join_path(xhome, 'smartmodel', lin, 'installed_' + lin)
            run_env.set('LMC_HOME', lmc_home)
            run_env.append_path('LD_LIBRARY_PATH', join_path(xhome, 'lib', lin))
            run_env.append_path('LD_LIBRARY_PATH', join_path(xhome, 'bin', lin))
            run_env.append_path('LD_LIBRARY_PATH', join_path(lmc_home, 'lib'))
            run_env.append_path('LD_LIBRARY_PATH', join_path(xhome,
                                                             'sysgen', 'lib'))

            run_env.append_path('PATH', join_path(xhome, 'bin', lin))
            run_env.append_path('PATH', join_path(xhome, 'sysgen', 'util'))
            run_env.append_path('PATH', join_path(xhome, 'sysgen', 'bin'))

    def install(self, *_):
        os.remove('xilinx-ise-147')  # Unused top-level file

        # Rename '_binary' files with a matching 'binary' wrapper to 'binary':
        # Xilinx seems to do some env modification in the 'binary' wrappers
        # before calling '_binary'. These env modifications do not play well
        # with dependencies loaded by spack.
        # Removing the wrapping layer might have unwanted side effects yet to
        # be discovered.
        for directory, _, files in os.walk('spack-expanded-archive'):
            for binary_name in fnmatch.filter(files, '_*'):
                binary_path = os.path.join(directory, binary_name)
                wrapper_name = binary_name.lstrip("_")
                wrapper_path = os.path.join(directory, wrapper_name)

                if os.path.isfile(wrapper_path):
                    os.rename(binary_path, wrapper_path)

        # Install the extracted tree of files
        for f in os.listdir('spack-expanded-archive'):
            f = join_path('spack-expanded-archive', f)

            if os.path.isdir(f):
                install_tree(f, join_path(self.spec.prefix,
                                          os.path.basename(f)))
            else:
                assert os.path.isfile(f)
                install(f, join_path(self.spec.prefix, os.path.basename(f)))
