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

        # Add wrappers for a selection of whitelisted binaries that will run
        # in their own environment.
        # We need to whitelist since we do not want to have Xilinx-supplied
        # compilers in our path when loading this package.
        #
        # Add any ISE tools you like to use here!
        executables = ["impact", "planAhead"]

        arch_bit = 64 if self.spec.architecture.target == 'x86_64' else 32
        env_definition = join_path(self.spec.prefix, "settings%d.sh" % arch_bit)

        mkdirp(self.prefix.bin)

        for binary in executables:
            wrapper_file = join_path(self.prefix.bin, binary)
            with open(wrapper_file, "wt") as wrapper:
                wrap_commands = [
                    '#!/usr/bin/env bash',

                    '# Xilinx must not evaluate "$@", outsource it in a function',
                    'function prepare_xilinx_env {',
                    '  source %s' % env_definition,
                    '}',

                    '# Remove this script from PATH to avoid recursive calls',
                    'SCRIPTPATH=$(cd "$(dirname "$0")"; pwd -P)',
                    'export PATH=${PATH//${SCRIPTPATH}/}',

                    '# Prepare the Xilinx runtime environment',
                    'prepare_xilinx_env',

                    '# UHEI/KIP license server',
                    'export LM_LICENSE_FILE=${LM_LICENCE_FILE}:2100@phobos',

                    '# Actual command, will be found in the env prepared above',
                    '%s "$@"' % binary]

                wrapper.writelines([cmd + os.linesep for cmd in wrap_commands])

            which("chmod")("+x", wrapper_file)
