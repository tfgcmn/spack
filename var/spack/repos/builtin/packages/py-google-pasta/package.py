from spack import *

class PyGooglePasta(PythonPackage):
    """Python AST Augmentation - Enable python source code refactoring through AST modifications."""

    homepage = "https://github.com/google/pasta"
    url      = "https://github.com/google/pasta/archive/v0.1.5.tar.gz"

    version('0.1.5', '45b1a10baa8a494a08487e9a008aa32c')

    depends_on('py-six@1.10.0:')
    depends_on('py-setuptools')
