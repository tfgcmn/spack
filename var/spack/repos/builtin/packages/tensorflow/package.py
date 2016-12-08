from spack import *
from glob import glob

class Tensorflow(Package):
    """TensorFlow is an Open Source Software Library for Machine Intelligence"""

    homepage = "https://www.tensorflow.org"
    url      = "https://github.com/tensorflow/tensorflow/archive/v0.10.0.tar.gz"

    version('0.10.0', 'b75cbd494d61a809af5ef25d7fba561b')

    depends_on('bazel@0.3.1:',         type='build')
    depends_on('swig',                 type='build')

    extends('python')
    depends_on('py-numpy@1.8.2:',      type=nolink)
    depends_on('py-six@1.10.0:',       type=nolink)
    depends_on('py-protobuf@3.0.0b2:', type=nolink)
    depends_on('py-wheel',             type=nolink)
    depends_on('py-mock@2.0.0:',       type=nolink)

    # FIXME: tensorflow pulls in a lot more dependencies...
    # e.g. eigen3 already exists as a spack package!?

    variant('gcp', default=False,
            description='Enable Google Cloud Platform Support')

    variant('cuda', default=False,
            description='Enable CUDA Support')
    depends_on('cuda', when='+cuda')

    def install(self, spec, prefix):
        if '+gcp' in spec:
            env['TF_NEED_GCP'] = '1'
        else:
            env['TF_NEED_GCP'] = '0'
        env['PYTHON_BIN_PATH'] = str(which('python'))
        env['SWIG_PATH'] = str(which('swig'))
        env['GCC_HOST_COMPILER_PATH'] = str(which('gcc'))

        assert '~cuda' in spec # for CUDA fix env variables below
        if '+cuda' in spec:
            env['TF_NEED_CUDA'] = '1'
        else:
            env['TF_NEED_CUDA'] = '0'
        env['TF_CUDA_VERSION'] = '' # spec['cuda'].version ?
        env['CUDA_TOOLKIT_PATH'] = '' # spec['cuda'].prefix ?
        env['TF_CUDNN_VERSION'] = ''
        env['CUDNN_INSTALL_PATH'] = ''

        configure()
        if '+cuda' in spec:
            bazel('-c', 'opt', '--config=cuda', '//tensorflow/tools/pip_package:build_pip_package')
        else:
            bazel('-c', 'opt', '//tensorflow/tools/pip_package:build_pip_package')

        build_pip_package = Executable('bazel-bin/tensorflow/tools/pip_package/build_pip_package')
        build_pip_package('%s/tmp_tensorflow_pkg' % self.stage.path)

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
