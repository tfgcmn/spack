##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
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
from spack import *


class Neomutt(AutotoolsPackage):
    """NeoMutt is a command-line mail reader (or Mail User Agent). It's a version of Mutt with added features."""

    homepage = "https://www.neomutt.org/"
    url      = "https://github.com/neomutt/neomutt/archive/neomutt-20170225-1.tar.gz"

    version('neomutt-20170225-1', '31628575709c53b089d9f4bb93ce6210')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    # otherwise install requires root perms?
    patch('do_not_call_chgrp.patch')

    variant('pop', default=True, description="Enable POP3 support")
    variant('imap', default=True, description="Enable IMAP support")
    variant('smtp', default=True, description="Enable SMTP support")

    variant('sidebar', default=False, description="Enable sidebar patchset")
    variant('notmuch', default=False, description="Enable notmuch patchset")
    depends_on('notmuch', when='+notmuch')

    variant('ssl', default=True, description="Enable support for SSL")
    depends_on('openssl', when='+ssl')

    variant('gnutls', default=True, description="Enable support for gnutls")
    depends_on('gnutls', when='+gnutls')

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = [
            #'--enable-compressed', # FIXME
            #'--enable-nntp', # FIXME?
            #'--enable-gpgme', # FIXME
            #'--with-gss', # FIXME?
            #'--with-sasl', # FIXME?
            #'--with-kyotocabinet', #FIXME!!!! needs kyotocabinet package!
        ]
	
        if '+pop' in self.spec:
            args.append('--enable-pop')

        if '+imap' in self.spec:
            args.append('--enable-imap')

        if '+smtp' in self.spec:
            args.append('--enable-smtp')

        if '+sidebar' in self.spec:
            args.append('--enable-sidebar')

        if '+notmuch' in self.spec:
            args.append('--enable-notmuch')

        if '+ssl' in self.spec:
            args.append('--with-ssl')

        if '+gnutls' in self.spec:
            args.append('--with-gnutls')

        return args
