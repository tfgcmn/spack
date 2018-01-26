#!/usr/bin/env bash

modulename=$1
modulespec=$2

spack fetch -D $module
srun -p compile -c8 -t6:00:00 spack install --only dependencies --show-log-on-error "$modulespec"
# fancy bash-magic to get the hash of the installed package
newhash=$(spack install --show-log-on-error "$modulespec" | tail -n1 | tr "-" "\n" | tail -n1)

viewname=views/$modulename_$iteration
spack view --dependencies yes hardlink -i $viewname /$newhash
spack view --dependencies no hardlink -i $viewname $compiler

bash 00_module.sh $viewname $modulename
