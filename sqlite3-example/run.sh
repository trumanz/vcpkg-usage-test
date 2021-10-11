#!/bin/bash

set -xeuo  pipefail

vcpkg install sqlite3
rm -rf build
mkdir build
cd build 
cmake  .. "-DCMAKE_TOOLCHAIN_FILE=${VCPKG_HOME}/scripts/buildsystems/vcpkg.cmake"
cmake --build .
./main



