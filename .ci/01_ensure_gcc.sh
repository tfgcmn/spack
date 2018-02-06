#!/usr/bin/env bash -xe

umask 0002

# ensure that system compiler are available
rm -f $HOME/.spack/linux/compilers.yaml
spack compiler add
spack fetch -D gcc@7.2.0
srun -p compile -c8 -t6:00:00 spack install --show-log-on-error gcc@7.2.0
# remove system compiler
rm -f $HOME/.spack/linux/compilers.yaml
# add gcc to local configuration
spack compiler add --scope site $(spack location -i gcc@7.2.0)
