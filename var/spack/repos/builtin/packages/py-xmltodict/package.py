from spack import *


class PyXmltodict(PythonPackage):
    """Python module that makes working with XML feel like you are working
    with JSON"""

    homepage = "https://github.com/martinblech/xmltodict"

    version('0.12.0', url="https://files.pythonhosted.org/packages/58/40/0d783e14112e064127063fbf5d1fe1351723e5dfe9d6daad346a305f6c49/xmltodict-0.12.0.tar.gz",
            sha256="50d8c638ed7ecb88d90561beedbf720c9b4e851a9fa6c47ebd64e99d166d8a21")

    depends_on('pkgconfig', type="build")
    depends_on('py-setuptools', type="build")
