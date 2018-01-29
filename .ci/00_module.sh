#!/usr/bin/env bash -xe

viewfolder=$1
modulename=$2

mkdir -p $(dirname $2)

rm -f ${modulename}
touch ${modulename}
echo '#%Module1.0#####################################################################' > ${modulename}
echo '##' >> ${modulename}
echo '## modules modulefile' >> ${modulename}
echo '##' >> ${modulename}
echo '' >> ${modulename}
echo '## basename to module name' >> ${modulename}
echo 'set modname [lindex [split [module-info name] "/"] 0]' >> ${modulename}
echo '' >> ${modulename}
echo '## filename to module version' >> ${modulename}
echo 'set version [lindex [split [module-info name] "/"] 1]' >> ${modulename}
echo '' >> ${modulename}
echo 'proc ModulesHelp { } {' >> ${modulename}
echo '        global version' >> ${modulename}
echo '        puts stderr "\t${modname} ${version}"' >> ${modulename}
echo '}' >> ${modulename}
echo '' >> ${modulename}
echo 'module-whatis "${modname} ${version}"' >> ${modulename}
echo '' >> ${modulename}
echo '# the debian versions we can support' >> ${modulename}
echo 'set distribution [exec lsb_release -c -s]' >> ${modulename}
echo 'set module_basedir '"${viewfolder}" >> ${modulename}
echo '' >> ${modulename}
echo '#puts stderr "module is ${modname}"' >> ${modulename}
echo '#puts stderr "version is ${version}"' >> ${modulename}
echo '#puts stderr "distribution is ${distribution}"' >> ${modulename}
echo '#puts stderr "module_basedir is ${module_basedir}"' >> ${modulename}
echo '#puts stderr "existing_basedir is ${existing_basedir}"' >> ${modulename}
echo '' >> ${modulename}
echo 'set existing_basedir [system "test -d ${module_basedir}"]' >> ${modulename}
echo 'if { ${existing_basedir} != 0 } {' >> ${modulename}
echo '        puts stderr "Distribution ${distribution} is not supported!"' >> ${modulename}
echo '        break' >> ${modulename}
echo '}' >> ${modulename}
echo '' >> ${modulename}
echo 'prepend-path  PATH                ${module_basedir}/bin' >> ${modulename}
echo 'prepend-path  PYTHONPATH          ${module_basedir}/lib/python2.7/site-packages' >> ${modulename}
echo 'prepend-path  PYTHONUSERBASE      ${module_basedir}' >> ${modulename}
echo 'prepend-path  MANPATH             ${module_basedir}/man' >> ${modulename}
echo 'prepend-path  MANPATH             ${module_basedir}/share/man' >> ${modulename}
echo 'prepend-path  LIBRARY_PATH        ${module_basedir}/lib' >> ${modulename}
echo 'prepend-path  LIBRARY_PATH        ${module_basedir}/lib64' >> ${modulename}
echo 'prepend-path  LD_LIBRARY_PATH     ${module_basedir}/lib' >> ${modulename}
echo 'prepend-path  LD_LIBRARY_PATH     ${module_basedir}/lib64' >> ${modulename}
echo 'prepend-path  TCLLIBPATH          ${module_basedir}/lib' >> ${modulename}
echo '# ECM: TCLLIBPATH is not colon-separated!!!' >> ${modulename}
echo '#prepend-path  TCLLIBPATH          ${module_basedir}/lib64' >> ${modulename}
echo 'prepend-path  CPATH               ${module_basedir}/include' >> ${modulename}
echo 'prepend-path  C_INCLUDE_PATH      ${module_basedir}/include' >> ${modulename}
echo 'prepend-path  CPLUS_INCLUDE_PATH  ${module_basedir}/include' >> ${modulename}
echo 'prepend-path  PKG_CONFIG_PATH     ${module_basedir}/lib/pkgconfig' >> ${modulename}
echo 'prepend-path  PKG_CONFIG_PATH     ${module_basedir}/lib64/pkgconfig' >> ${modulename}
echo 'prepend-path  CMAKE_PREFIX_PATH   ${module_basedir}' >> ${modulename}
echo '' >> ${modulename}
echo "## Module generated on: $(date +%Y%m%d)" >> ${modulename}
