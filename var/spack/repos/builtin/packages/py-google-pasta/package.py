from spack import *

class PyGooglePasta(PythonPackage):
    """Python AST Augmentation - Enable python source code refactoring through AST modifications."""

    homepage = "https://github.com/google/pasta"
    url      = "https://github.com/google/pasta/archive/v0.1.5.tar.gz"

    version('0.1.8', sha256='c6dc1118250487d987a7b1a404425822def2e8fb2b765eeebc96887e982b6085')
    version('0.1.7', sha256='324ae96cea1c27af1bbe289e502ad26673d9e00236a64a3efd68bf12dfd85a51')
    version('0.1.6', sha256='11c4efd38f2cfb053c12ded1e1c3e1219a77b83ea83d783eaeba879faebe6b8c')
    version('0.1.5', sha256='799bf5b40320495ebbb54706d35b8c8a818c39328aa4c27a842f5d2f645eef38')
    version('0.1.4', sha256='8a9208c806c4e3f267269e4bae94c1f41d4777472cf7a813f74ba9e0907b1a5f')
    version('0.1.3', sha256='29815aac18759d4518a80de24e23ac1ae3e098e9c5d7273abdc42174846a13e9')
    version('0.1.2', sha256='53e4c009a5eac38e942deb48bfc2d3cfca62cd457255fa86ffedb7e40f726a0c')
    version('0.1.1', sha256='66f6ea653c7caf5ad0a1cd6f69a750df9845ccce755ee3619db89b672d240c20')
    version('0.1',   sha256='33ce0c80b393d070a372cd65fd1471852507f0ccc5432687bb73589f05cb8452')

    depends_on('py-six@1.10.0:')
    depends_on('py-setuptools', type='build')
