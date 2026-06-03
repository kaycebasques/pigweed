# Copyright 2026 The Pigweed Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Test importing generated python protos.

How to run this test:

CMake:
  source bootstrap.sh
  cmake -B out/cmake -S . -G Ninja \
    -DCMAKE_TOOLCHAIN_FILE=pw_toolchain/host_gcc/toolchain.cmake \
    -Dpw_ENABLE_CC_SANDBOX=OFF
  cmake --build out/cmake --target pw_protobuf_compiler.python_proto_test

Bazel:
  bazelisk test //pw_protobuf_compiler/py:python_proto_test

GN:
  gn gen out/gn
  ninja -C out/gn python/phony/pw_protobuf_compiler/py/py.tests
"""

import sys

try:
    from pw_protobuf_compiler.pwpb_test_protos import pwpb_test_pb2

    print("Successfully imported pwpb_test_pb2")
except ImportError as e:
    print(f"Failed to import pwpb_test_pb2: {e}", file=sys.stderr)
    sys.exit(1)

point = pwpb_test_pb2.Point()
point.x = 1
point.y = 2
point.name = "test"

assert point.x == 1
assert point.y == 2
assert point.name == "test"

print("Successfully used pwpb_test_pb2")
