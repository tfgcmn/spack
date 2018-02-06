#!/usr/bin/env bash -xe

viewfolder=$1
modulename=$2

mkdir -p $(dirname $2)

rm -f ${modulename}
touch ${modulename}
cat > ${modulename} <<EOF
#%Module1.0#####################################################################
##
## modules modulefile
##

## basename to module name
set modname [lindex [split [module-info name] "_"] 0]

## filename to module version
set version [lindex [split [module-info name] "_"] 1]

proc ModulesHelp { } {
        global version
        puts stderr "\t\${modname} \${version}"
}

module-whatis "\${modname} \${version}"

# the debian versions we can support
set distribution [exec lsb_release -c -s]
set module_basedir ${viewfolder}

#puts stderr "module is \${modname}"
#puts stderr "version is \${version}"
#puts stderr "distribution is \${distribution}"
#puts stderr "module_basedir is \${module_basedir}"
#puts stderr "existing_basedir is \${existing_basedir}"

set existing_basedir [system "test -d \${module_basedir}"]
if { \${existing_basedir} != 0 } {
        puts stderr "Distribution \${distribution} is not supported!"
        break
}

prepend-path  PATH                \${module_basedir}/bin
prepend-path  PYTHONPATH          \${module_basedir}/lib/python2.7/site-packages
prepend-path  PYTHONUSERBASE      \${module_basedir}
prepend-path  MANPATH             \${module_basedir}/man
prepend-path  MANPATH             \${module_basedir}/share/man
prepend-path  LIBRARY_PATH        \${module_basedir}/lib
prepend-path  LIBRARY_PATH        \${module_basedir}/lib64
prepend-path  LD_LIBRARY_PATH     \${module_basedir}/lib
prepend-path  LD_LIBRARY_PATH     \${module_basedir}/lib64
prepend-path  TCLLIBPATH          \${module_basedir}/lib
# ECM: TCLLIBPATH is not colon-separated!!!
#prepend-path  TCLLIBPATH          \${module_basedir}/lib64
prepend-path  CPATH               \${module_basedir}/include
prepend-path  C_INCLUDE_PATH      \${module_basedir}/include
prepend-path  CPLUS_INCLUDE_PATH  \${module_basedir}/include
prepend-path  PKG_CONFIG_PATH     \${module_basedir}/lib/pkgconfig
prepend-path  PKG_CONFIG_PATH     \${module_basedir}/lib64/pkgconfig
prepend-path  CMAKE_PREFIX_PATH   \${module_basedir}

## Module generated on: \$(date +%Y%m%d)
EOF
