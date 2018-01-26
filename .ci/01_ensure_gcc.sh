#!/usr/bin/env bash

rm -f $HOME/.spack/linux/compilers.yaml
spack fetch -D gcc@7.2.0
srun -p compile -c8 -t6:00:00 spack install --show-log-on-error gcc@7.2.0
spack compiler add --scope site $(spack location -i gcc@7.2.0)
