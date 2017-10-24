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


class VisionaryDefaults(Package):
    """Visionary Meta Package"""

    # This is a meta-package.  Instructions:
    # $ cd /tmp
    # $ spack install binutils+plugins+gold
    # $ spack find binutils+plugins+gold
    # -- linux-debian8-x86_64 / gcc@4.X.X -----------------------------
    # qxd4ne6 binutils@2.27
    # $ spack install gcc@6.2.0+binutils+gold ^/qxd4ne6
    # $ spack cd -i "gcc@6.2.0+binutils+gold"
    # $ spack compiler find --scope site .
    # $ spack install visionary-defaults %gcc@6.2.0

    homepage = None
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack-visions/archive/master.tar.gz'
    version('0.1', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: added on 2017-01-31
    version('0.2', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-02-01 (cereal added)
    version('0.2.1', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-02-01 (vim with python and lots of other stuff, ucs4 for python)
    version('0.2.2', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-02-08 (moved from custom nodejs to upstream node-js)
    version('0.2.3', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: py-pyside
    version('0.2.4', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-02-20 add py-symfit and --linker
    version('0.2.5', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-02-22 add py-jedi and add +lua +perl to vim
    version('0.2.6', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-03-03 default to tensorflow built with +cuda
    version('0.2.7', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-03-15 rename some dependencies according to upstream names
    version('0.2.8', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-04-05 pin googletest to 1.7.0 and add pybind11
    version('0.2.9', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-05-08 add py-pytest-xdist (requested by Paul)
    version('0.2.10', git='https://github.com/electronicvisions/spack-visions.git')
    # ECM: 2017-06-30 add ffmeg (requested by TMA) and py-pylint
    version('0.2.11', git='https://github.com/electronicvisions/spack-visions.git')
    # AB: 2017-08-19 add py-scikit-learn
    version('0.2.12', git='https://github.com/electronicvisions/spack-visions.git')
    # AB: 2017-08-31 remove nest@2.2.2 as it does not build with gcc@6.4.0
    version('0.2.13', git='https://github.com/electronicvisions/spack-visions.git')
    # AB: 2017-09-20 add py-sqlalchemy which is needed for dls stuff
    version('0.2.14', git='https://github.com/electronicvisions/spack-visions.git')
    # JK: 2017-10-10 / 2017-10-19 visionary patches for llvm, py-line-profiler, cppcheck
    version('0.2.15', git='https://github.com/electronicvisions/spack-visions.git', default=True)

    # ECM: 2017-04-28 pin python to >= 3.6.0
    # version('0.3.0', git='https://github.com/electronicvisions/spack-visions.git')


    # This does not work, spack will try to reinstall gcc :(((((
    # variant('wheezy', default=False)

    # depends_on('gcc@6.2.0+binutils+gold %gcc@4.7', when="+wheezy")
    # depends_on('gcc@6.2.0+binutils+gold %gcc@4.9.2', when="~wheezy")

    depends_on('binutils+gold+plugins', when='@0.2.5:')

    depends_on('vim', when='@:0.2.1')
    depends_on('vim +python +cscope +ruby +huge', when='@0.2.2:0.2.5')
    depends_on('vim +python +ruby +lua +perl +cscope +huge', when='@0.2.6:')

    depends_on('emacs ~X')
    depends_on('tmux')
    depends_on('ncdu')
    depends_on('units')
    depends_on('ranger', when='@:0.2.7')
    depends_on('py-ranger', when='@0.2.8:')

    depends_on('mosh', when='@0.2:')

    depends_on('mercurial')
    depends_on('git')
    depends_on('git-review', when='@:0.2.7')
    depends_on('py-git-review', when='@0.2.8:')

    depends_on('cmake')
    depends_on('doxygen')
    depends_on('bear')
    depends_on('rtags')
    depends_on('cppcheck', when='@0.2.15:')

    # requested by TMA for generating animations ;)
    depends_on('ffmpeg', when='@0.2.11:')

    depends_on('gdb')
    depends_on('llvm', when='@:0.2.14')
    depends_on('llvm+visionary+python@5.0.0:', when='@0.2.15:')
    # depends_on('nodejs', when='@0.2.2')
    depends_on('node-js', when='@0.2.3:')

    depends_on('boost@1.55.0+graph+icu+mpi+python')
    depends_on('yaml-cpp+shared')
    depends_on('tensorflow', when='@:0.2.6')
    depends_on('tensorflow', when='@0.2.7:')  # +cuda
    depends_on('log4cxx')
    # depends_on('libpsf')
    depends_on('googletest', when='@:0.2.11')
    depends_on('googletest +gmock', when='@0.2.12:')
    depends_on('gflags')

    depends_on('cereal', when='@0.2.1:')
    depends_on('py-pybind11', when='@0.2.9:')

    depends_on('py-bokeh')
    depends_on('py-pygtk', when='@0.2.4:')
    depends_on('gtkplus+X', when='@0.2.4:')
    depends_on('cairo+X', when='@0.2.4:')
    depends_on('py-pyside')

    depends_on('nest@2.2.2+python', when='@0.2:0.2.12')
    depends_on('py-brian')
    depends_on('py-brian2')
    depends_on('py-elephant')
    #depends_on('py-spykeviewer')
    depends_on('py-pynn @0.7.5')

    # depends_on('python+tk @2.7:2.7.999')
    depends_on('python @2.7:2.7.999', when='@:0.2.1')
    depends_on('python @2.7:2.7.999 +ucs4', when='@0.2.2:')
    depends_on('python @3.6.0:', when='@0.3.0:')
    depends_on('py-cython')
    depends_on('py-pip')
    depends_on('py-pylint', when='@0.2.11:')

    depends_on('py-ipython')
    # depends_on('py-ipdb')
    # depends_on('py-jupyter')
    # depends_on('py-notebook')

    depends_on('py-matplotlib~tk+qt+ipython')
    # depends_on('py-matplotlib+tk+ipython')
    depends_on('py-numpy')
    depends_on('py-pandas @0.19.0:')
    depends_on('py-pytables @3.3.0:')
    depends_on('py-scipy')
    depends_on('py-scikit-image', when='@0.2.12:')
    depends_on('py-seaborn')
    depends_on('py-sympy')
    depends_on('py-statsmodels')
    depends_on('py-lmfit')
    depends_on('py-symfit', when='@0.2.5:')
    depends_on('py-sqlalchemy', when='@0.2.14:')

    depends_on('py-pyyaml')

    depends_on('py-autopep8')
    # depends_on('py-flake8')
    # depends_on('py-pylint')
    depends_on('py-jedi', when='@0.2.6:')

    depends_on('py-sphinx')
    depends_on('py-doxypy')
    depends_on('py-nose')
    depends_on('py-junit-xml')
    depends_on('py-xmlrunner')
    depends_on('py-pytest-xdist', when='@0.2.10:')
    depends_on('py-line-profiler', when='@0.2.15:')

    # depends_on('py-appdirs')
    # depends_on('py-current')
    # depends_on('py-funcsigs')
    # depends_on('py-lazy')
    depends_on('py-attrs')
    depends_on('py-setuptools')

    depends_on('py-tabulate')
    depends_on('py-html', when='@:0.2.7')
    depends_on('py-html5lib', when='@0.2.8:')
    # depends_on('py-myhdl')
    depends_on('py-pillow')
    # depends_on('py-pyserial')
    # depends_on('py-shiboken')
    # depends_on('py-xlrd')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-defaults.py'))

        # we could create some filesystem view here?
