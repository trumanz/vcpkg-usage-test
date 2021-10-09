# vcpkg-usage-test

[![azure-pipeline](https://dev.azure.com/trumanckzhou/trumanckzhou/_apis/build/status/trumanz.vcpkg-usage-test?branchName=main)](https://dev.azure.com/trumanckzhou/trumanckzhou/_build/latest?definitionId=8&branchName=main)

 


# Table of contents
1. [Vcpkg Installation](#installation)
2. [Example](#example)
    1. [sqlit](#sqlit)

 


# Vcpkg Installation <a name="installation"></a>

https://vcpkg.io/en/getting-started.html

```
$ git clone https://github.com/Microsoft/vcpkg.git
$ ./vcpkg/bootstrap-vcpkg.sh
$ export VCPKG_HOME=$(pwd)/vcpkg
$ export PATH=$PATH:$(pwd)/vcpkg
```

# Example <a name="example"></a>
## sqlite <a name="sqlit"></a>

```
$ cd example-sqlite
$ mkdir build
$ cd build
$ cmake  .. "-DCMAKE_TOOLCHAIN_FILE=${VCPKG_HOME}/scripts/buildsystems/vcpkg.cmake"
$ cmake --build .
$ ./main
```