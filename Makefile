# Copyright 2020-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Makefile for device-management-interface
default: test

# initialize path of grpc_cpp_plugin binary
GRPC_CPP_PLUGIN_PATH ?= $(shell which grpc_cpp_plugin)

# set default shell options
SHELL = bash -e -o pipefail

# tool containers
VOLTHA_TOOLS_VERSION ?= 2.5.0

PROTOC    = docker run --rm --user $$(id -u):$$(id -g) -v ${CURDIR}:/app $(shell test -t 0 && echo "-it") voltha/voltha-ci-tools:${VOLTHA_TOOLS_VERSION}-protoc protoc
PROTOC_SH = docker run --rm --user $$(id -u):$$(id -g) -v ${CURDIR}:/go/src/github.com/opencord/device-management-interface/v3 $(shell test -t 0 && echo "-it") --workdir=/go/src/github.com/opencord/device-management-interface/v3 voltha/voltha-ci-tools:${VOLTHA_TOOLS_VERSION}-protoc sh -c
GO        = docker run --rm --user $$(id -u):$$(id -g) -v ${CURDIR}:/app $(shell test -t 0 && echo "-it") -v gocache:/.cache -v gocache-${VOLTHA_TOOLS_VERSION}:/go/pkg voltha/voltha-ci-tools:${VOLTHA_TOOLS_VERSION}-golang go

# Function to extract the last path component from package line in .proto files
define if_package_path
$(shell grep if_package $(1) | sed -n 's/.*\/\(.*\)";/\1/p')
endef

# Variables
PROTO_FILES := $(sort $(wildcard protos/dmi/*.proto))

PROTO_GO_DEST_DIR := go
PROTO_GO_PB:= $(foreach f, $(PROTO_FILES), $(patsubst protos/dmi/%.proto,$(PROTO_GO_DEST_DIR)/$(call if_package_path,$(f))/%.pb.go,$(f)))

PROTO_PYTHON_DEST_DIR := python/dmi
PROTO_PYTHON_PB2 := $(foreach f, $(PROTO_FILES), $(patsubst protos/dmi/%.proto,$(PROTO_PYTHON_DEST_DIR)/%_pb2.py,$(f)))

PROTO_CPP_DEST_DIR := cpp
PROTO_CPP_PB := $(foreach f, $(PROTO_FILES), $(patsubst protos/dmi/%.proto,$(PROTO_CPP_DEST_DIR)/$(call if_package_path,$(f))/%.pb.cc,$(f)))
# Force pb file to be regenrated every time.  Otherwise the make process assumes generated version is still valid
.PHONY: dmi.pb

print:
	@echo "Proto files: $(PROTO_FILES)"
	@echo "Go PB files: $(PROTO_GO_PB)"
	@echo "python PB files: $(PROTO_PYTHON_PB)"

# Generic targets
protos: go-protos python-protos cpp-protos

build: protos

test: go-test python-test cpp-test


venv_protos:
	virtualenv -p python3 $@;\
	source ./$@/bin/activate ; set -u ;\
	pip install grpcio-tools googleapis-common-protos

# Python targets
python-protos: $(PROTO_PYTHON_PB2)

$(PROTO_PYTHON_DEST_DIR)/%_pb2.py: protos/dmi/%.proto Makefile venv_protos
	source ./venv_protos/bin/activate ; set -u ;\
	python -m grpc_tools.protoc \
    -I protos \
    --python_out=python \
    --grpc_python_out=python \
    --descriptor_set_out=$(PROTO_PYTHON_DEST_DIR)/$(basename $(notdir $<)).desc \
    --include_imports \
    --include_source_info \
    $<

# Go targets
go-protos: dmi.pb
	@echo "Creating *.go.pb files"
	@${PROTOC_SH} " \
	  set -e -o pipefail; \
	  for x in ${PROTO_FILES}; do \
	    echo \$$x; \
	    protoc --go_out=plugins=grpc:/go/src -I protos \$$x; \
	  done"

dmi.pb:
	@echo "Creating $@"
	@${PROTOC} -I protos \
	  --include_imports --include_source_info \
	  --descriptor_set_out=$@ \
	  ${PROTO_FILES}

# Cpp targets
cpp-protos:
	echo "Creating *.pb.cpp files"
	@${PROTOC_SH} " \
      set -e -o pipefail; \
      for x in ${PROTO_FILES}; do \
		echo \$$x; \
		protoc --cpp_out=\$(PROTO_CPP_DEST_DIR) -I protos \$$x; \
		protoc --grpc_out=\$(PROTO_CPP_DEST_DIR) --plugin=protoc-gen-grpc=/usr/local/bin/grpc_cpp_plugin -I protos \$$x; \
	  done"

go-test:
	test/test-go-proto-consistency.sh
	${GO} mod verify

python-test: tox.ini
	test/test-python-proto-consistency.sh
	tox

python-build: setup.py python-protos
	rm -rf dist/
	python ./setup.py sdist

cpp-test:
	test/test-cpp-proto-consistency.sh
