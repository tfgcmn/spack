from spack import *
from glob import glob

class Tensorflow(Package):
    """TensorFlow is an Open Source Software Library for Machine Intelligence"""

    homepage = "https://www.tensorflow.org"
    url      = "https://github.com/tensorflow/tensorflow/archive/v0.10.0.tar.gz"

    version('1.0.0-rc2', 'a058a7e0ba2b9761cf2420c82d520049')
    version('0.10.0',    'b75cbd494d61a809af5ef25d7fba561b')

    depends_on('swig',                 type='build')
    depends_on('bazel@0.4.4:',         type='build', when='@1:')
    depends_on('bazel@0.3.1:',         type='build', when='@:1')

    extends('python')
    depends_on('py-setuptools',        type=('build', 'run'))
    depends_on('py-numpy@1.8.2:',      type=('build', 'run'))
    depends_on('py-six@1.10.0:',       type=('build', 'run'))
    depends_on('py-protobuf@3.0.0b2:', type=('build', 'run'))
    depends_on('py-wheel',             type=('build', 'run'))
    depends_on('py-mock@2.0.0:',       type=('build', 'run'))

    patch('url-zlib.patch', when='@0.10.0')

    patch('crosstool.patch', when='@1.0.0-rc2') # auch auf 0.10.0 wenn mit cuda!

    # FIXME: tensorflow pulls in a lot more dependencies...
    # e.g. eigen3 already exists as a spack package!?

    variant('gcp', default=False,
            description='Enable Google Cloud Platform Support')

    variant('cuda', default=False,
            description='Enable CUDA Support')

    depends_on('cuda', when='+cuda')
    depends_on('cudnn', when='+cuda')

    def install(self, spec, prefix):
        if '+gcp' in spec:
            env['TF_NEED_GCP'] = '1'
        else:
            env['TF_NEED_GCP'] = '0'

        env['PYTHON_BIN_PATH'] = str(spec['python'].prefix.bin) + '/python'
        env['SWIG_PATH'] = str(spec['swig'].prefix.bin)
        env['GCC_HOST_COMPILER_PATH'] = spack_cc

        if '+cuda' in spec:
            env['TF_NEED_CUDA'] = '1'
            env['TF_CUDA_VERSION'] = str(spec['cuda'].version)
            env['CUDA_TOOLKIT_PATH'] = str(spec['cuda'].prefix)
            env['TF_CUDNN_VERSION'] = str(spec['cudnn'].version)[0]
            env['CUDNN_INSTALL_PATH'] = str(spec['cudnn'].prefix)
            env['TF_CUDA_COMPUTE_CAPABILITIES'] = '3.5,5.2'
        else:
            env['TF_NEED_CUDA'] = '0'
            env['TF_CUDA_VERSION'] = ''
            env['CUDA_TOOLKIT_PATH'] = ''
            env['TF_CUDNN_VERSION'] = ''
            env['CUDNN_INSTALL_PATH'] = ''

        if self.spec.satisfies('@1.0.0-rc2:'):
            env['CC_OPT_FLAGS'] = '-march=x86-64 -mtune=generic'
            env['TF_NEED_JEMALLOC'] = '0'
            env['TF_NEED_HDFS'] = '0'
            env['TF_ENABLE_XLA'] = '0'
            env['PYTHON_LIB_PATH'] = self.module.site_packages_dir
            env['TF_NEED_OPENCL'] = '0'

        # clean bazel build cache
        which('bazel')('clean')

        env['TESTTMP_DIR'] = '/tmp'
        configure()
        if '+cuda' in spec:
            bazel('-c', 'opt', '--config=cuda', '//tensorflow/tools/pip_package:build_pip_package')
        else:
            bazel('-c', 'opt', '//tensorflow/tools/pip_package:build_pip_package')

        tmp_path = join_path('/tmp', 'tmp_tensorflow_pkg')
        mkdirp(tmp_path)
        build_pip_package = Executable('bazel-bin/tensorflow/tools/pip_package/build_pip_package')
        build_pip_package(tmp_path)

        # using setup.py for installation
        # webpage suggests: sudo pip install /tmp/tensorflow_pkg/tensorflow-0.XYZ.whl
        mkdirp('_python_build')
        cd('_python_build')
        ln = which('ln')

        for fn in glob("../bazel-bin/tensorflow/tools/pip_package/build_pip_package.runfiles/org_tensorflow/*"):
            ln('-s', fn, '.')
        for fn in glob("../tensorflow/tools/pip_package/*"):
            ln('-s', fn, '.')
        setup_py('install', '--prefix={0}'.format(prefix))
