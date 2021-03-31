## System Requirements

**Software** :

1. Essential tools for building packages

Install the following packages

   `sudo apt-get update && sudo apt-get install -y git pkg-config build-essential autoconf clang libc++-dev cmake g++-4.9`

Run the below commands to ensure that g++-4.9 and gcc-4.9 are default g++ and gcc compiler versions.

```shell
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 20
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 20
```

2. Install cmake version 3.5.1 or above.

```shell
cd /tmp
git clone -b v3.5.1 https://gitlab.kitware.com/cmake/cmake.git
cd /tmp/cmake
./bootstrap
make
sudo make install
```

3. Install gRPC version v1.31.1

``` shell
cd /tmp
git clone -b v1.31.1  https://github.com/grpc/grpc
cd /tmp/grpc
git submodule update --init
mkdir -p cmake/build
cd cmake/build
cmake ../.. -DgRPC_INSTALL=ON                \
            -DCMAKE_BUILD_TYPE=Release       \
            -DgRPC_ABSL_PROVIDER=module     \
            -DgRPC_CARES_PROVIDER=module    \
            -DgRPC_PROTOBUF_PROVIDER=module \
            -DgRPC_RE2_PROVIDER=module      \
            -DgRPC_SSL_PROVIDER=module      \
            -DgRPC_ZLIB_PROVIDER=module
make
sudo make install
# copy library and grpc_cpp_plugin to path below.
sudo cp `find . -name "*.a"` /usr/local/lib/
sudo cp `find . -name grpc_cpp_plugin` /usr/local/bin/
```
