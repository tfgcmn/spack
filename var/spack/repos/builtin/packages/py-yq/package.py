from spack import *


class PyYq(PythonPackage):
    """yq: Command-line YAML/XML processor - jq wrapper for YAML and XML
    documents"""

    homepage = "https://github.com/kislyuk/yq"
    git      = "https://github.com/kislyuk/yq"

    version('2.7.2',
            url="https://files.pythonhosted.org/packages/0c/23/aa30f88c916128aa60de9d4f53dd40c8f6c31cb7ebb808aab1b0501a701f/yq-2.7.2.tar.gz",
            sha256="f7dafd1e53d1f806ffe11de6da814e231d866595e2faae0dfc38135b8ee79bbb")

    depends_on('pkgconfig', type="build")
    depends_on('py-setuptools', type="build")
    depends_on('py-pyyaml@3.11:', type=("build", "run"))
    depends_on('py-xmltodict@0.11.0:', type=("build", "run"))
