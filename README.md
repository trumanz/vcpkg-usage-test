# vcpkg-usage-test

[![azure-pipeline](https://dev.azure.com/trumanckzhou/trumanckzhou/_apis/build/status/trumanz.vcpkg-usage-test?branchName=main)](https://dev.azure.com/trumanckzhou/trumanckzhou/_build/latest?definitionId=8&branchName=main)


# install vcpkg

https://vcpkg.io/en/getting-started.html

```
$ git clone https://github.com/Microsoft/vcpkg.git
$ ./vcpkg/bootstrap-vcpkg.sh
$ export VCPKG_HOME=$(pwd)/vcpkg
$ export PATH=$PATH:$(pwd)/vcpkg
```

# Example sqlite
```
$ cd example-sqlite
$ mkdir build
$ cd build
$ cmake  .. "-DCMAKE_TOOLCHAIN_FILE=${VCPKG_HOME}/scripts/buildsystems/vcpkg.cmake"
$ cmake --build .
$ ./main
```