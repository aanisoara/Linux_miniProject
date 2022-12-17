set -e -x

CHOST=$(${SRC_DIR}/.build/*-*-*-*/build/build-cc-gcc-final/gcc/xgcc -dumpmachine)

mkdir -p ${PREFIX}/lib

pushd ${PREFIX}/lib/
ln -s libgomp.so.${libgomp_ver} libgomp.so.${libgomp_ver:0:1}
popd
