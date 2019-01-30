from spack import *


class PyYccp(PythonPackage):
    """YAML with pre-Computed Common Parameters is a library for easy
    parameter-file handling. It allows for simple computations on common
    parameters which can then be referenced in the rest of the parameter
    file.
    """

    homepage = "https://github.com/obreitwi/yccp"
    url      = "https://github.com/obreitwi/yccp"

    version('0.5.0', git="https://github.com/obreitwi/yccp.git", tag="v0.5.0")
    version('0.4.0', git="https://github.com/obreitwi/yccp.git",
            commit="055dfd62945f1b1e0990ba9318afeea325ed2de2")
    version('master', git="https://github.com/obreitwi/yccp.git")

    depends_on('pkgconfig', type="build")
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy')
    depends_on('py-pyyaml')
