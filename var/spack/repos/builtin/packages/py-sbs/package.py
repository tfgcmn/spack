from spack import *

class PySbs(PythonPackage):
    """Spike based Sampling framework"""

    homepage = "https://gitviz.kip.uni-heidelberg.de"
    url      = "https://gitviz.kip.uni-heidelberg.de"

    version('master', git='git@gitviz.kip.uni-heidelberg.de:model-nmsampling-sbs.git')
    version('1.6.5', git='git@gitviz.kip.uni-heidelberg.de:model-nmsampling-sbs.git', commit='3ce21de823b7df37fb83b87ec7f9607e781aaa1a')
    version('1.6.2', git='git@gitviz.kip.uni-heidelberg.de:model-nmsampling-sbs.git', commit='318ed67dbf6330323c4eb398219701c14eb7a945')
    version('1.5.2', git='git@gitviz.kip.uni-heidelberg.de:model-nmsampling-sbs.git', commit='c0adeed57a467b4edaa399a623fb2865ac2a06c6')
    version('1.4.1', git='git@gitviz.kip.uni-heidelberg.de:model-nmsampling-sbs.git', commit='655c930dc07efec01ffe02e44fcc99660e4c96c3')
    version('1.4.0', git='git@gitviz.kip.uni-heidelberg.de:model-nmsampling-sbs.git', commit='68889dbd832cb6b8bf17f38684634e3126adac1f')
    version('1.3.2', git='git@gitviz.kip.uni-heidelberg.de:model-nmsampling-sbs.git', commit='87bb9787b4bdc741e349ad17191165a496e85042')

    depends_on('py-setuptools', type="build")
    depends_on('py-cython', type='build')
    depends_on('py-numpy', type=("build", "run"))
    depends_on('py-scipy', type=("build", "run"))
    depends_on('py-matplotlib', type=("build", "run"))
    depends_on('py-pynn@0.8:', type=("build", "run"))

    @when("@1.0.0:1.5.2")
    def patch(self):
        # remove unnecessary h5py dependency from source code
        filter_file("^import h5py$", "# import h5py", "sbs/meta.py")
