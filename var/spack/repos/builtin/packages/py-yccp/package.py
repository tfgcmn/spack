from spack import *


class PyYccp(PythonPackage):
    """YAML with pre-Computed Common Parameters is a library for easy
    parameter-file handling. It allows for simple computations on common
    parameters which can then be referenced in the rest of the parameter
    file.
    """

    homepage = "https://github.com/obreitwi/yccp"
    url      = "https://github.com/obreitwi/yccp"

    # Currently there is no stable 1.0 release yet so just build master all the time.
    version('0.4.0', git="https://github.com/obreitwi/yccp.git",
            commit="055dfd62945f1b1e0990ba9318afeea325ed2de2")
    version('master', git="https://github.com/obreitwi/yccp.git")

    depends_on('pkgconfig', type="build")
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy')
    depends_on('py-pyyaml')
