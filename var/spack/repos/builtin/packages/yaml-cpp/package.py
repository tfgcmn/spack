# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os, inspect


class YamlCpp(CMakePackage):
    """A YAML parser and emitter in C++"""

    homepage = "https://github.com/jbeder/yaml-cpp"
    url      = "https://github.com/jbeder/yaml-cpp/archive/yaml-cpp-0.5.3.tar.gz"
    git      = "https://github.com/jbeder/yaml-cpp.git"

    version('develop', branch='master')
    version('0.6.2', '5b943e9af0060d0811148b037449ef82')
    version('0.5.3', '2bba14e6a7f12c7272f87d044e4a7211')

    variant('shared', default=True,
            description='Additionally build of shared libraries')
    variant('pic',   default=True,
            description='Build with position independent code')

    depends_on('boost@:1.66.99', when='@:0.5.3')

    conflicts('%gcc@:4.7', when='@0.6.0:', msg="versions 0.6.0: require c++11 support")
    conflicts('%clang@:3.3.0', when='@0.6.0:', msg="versions 0.6.0: require c++11 support")
    # currently we can't check for apple-clang's version
    # conflicts('%clang@:4.0.0-apple', when='@0.6.0:',
    # msg="versions 0.6.0: require c++11 support")
    conflicts('%intel@:11.1', when='@0.6.0:', msg="versions 0.6.0: require c++11 support")
    conflicts('%xl@:13.1', when='@0.6.0:', msg="versions 0.6.0: require c++11 support")
    conflicts('%xl_r@:13.1', when='@0.6.0:', msg="versions 0.6.0: require c++11 support")

    def cmake_args(self):
        options = [
            '-DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=%s' % (
                'ON' if '+pic' in self.spec else 'OFF'),
        ]
        return options

    def cmake(self, spec, prefix):
        options = [os.path.abspath(self.root_cmakelists_dir)]
        options += self.std_cmake_args
        options += self.cmake_args()
        with working_dir(self.build_directory, create=True):
            inspect.getmodule(self).cmake(*options)
            inspect.getmodule(self).make(*self.build_targets)
            inspect.getmodule(self).make(*self.install_targets)
        if '+shared' in self.spec:
            options += ['-DBUILD_SHARED_LIBS:BOOL=ON']
            with working_dir(self.build_directory, create=True):
                inspect.getmodule(self).cmake(*options)
                inspect.getmodule(self).make(*self.build_targets)
                inspect.getmodule(self).make(*self.install_targets)
        # disable tests (avoids building the internal googletest libraries)
        options += ['-DYAML_CPP_BUILD_TESTS:BOOL=OFF']

    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        pass
