# -*- makefile -*-
# -----------------------------------------------------------------------
# Copyright 2022-2024 Open Networking Foundation (ONF) and the ONF Contributors
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
# -----------------------------------------------------------------------
# Intent: Helper makefile target used to setup for a release
# -----------------------------------------------------------------------

$(if $(DEBUG),$(warning ENTER))

##-------------------##
##---]  GLOBALS  [---##
##-------------------##

# TODO: Library function  $(call mk-path,makefiles/release/targets.mk)
release-mk-top := $(abspath $(lastword $(MAKEFILE_LIST)))
release-mk-top := $(subst /makefiles/release/targets.mk,$(null),$(release-mk-top))

GIT	?= /usr/bin/env git

##--------------------##
##---]  INCLUDES  [---##
##--------------------##
include $(ONF_MAKEDIR)/release/voltha-versions.mk
include $(ONF_MAKEDIR)/release/targets/voltha-certification.mk
include $(ONF_MAKEDIR)/release/targets/voltha-e2e.mk
include $(ONF_MAKEDIR)/release/targets/voltha-nightly-jobs.mk

# last-release  := voltha-2.11
last-release := $(voltha-release-last)


##-------------------##
##---]  TARGETS  [---##
##-------------------##
all: help

## ---------------------------------------------------------------------------
## Intent: Build these deps to create a new branch/release area
## ---------------------------------------------------------------------------
create-jobs-release += create-jobs-release-bat
create-jobs-release += create-jobs-release-certification
create-jobs-release += create-jobs-release-nightly
create-jobs-release += create-jobs-release-units
create-jobs-release += create-jobs-release-e2e

create-jobs-release : $(create-jobs-release)

	@echo
	$(GIT) status

## ---------------------------------------------------------------------------
## Intent: Create branch driven pipeline test jobs.
## ---------------------------------------------------------------------------
units-yaml := $(release-mk-top)/jjb/pipeline/voltha/$(voltha-version)
units-root := $(subst /$(voltha-version),$(null),$(units-yaml))
create-jobs-release-units : $(units-yaml)
$(units-yaml):

	@echo
	@echo "** Create branch driven pipeline: unit tests"
	$(HIDE)mkdir -vp $@
	rsync -r --checksum $(units-root)/master/. $@/.
	$(HIDE)/bin/ls -l $(units-root)

## ---------------------------------------------------------------------------
## Intent: Create branch driven nightly test jobs.
## ---------------------------------------------------------------------------
sterile-create-jobs-release := $(addprefix sterile-,$(create-jobs-release))
sterile-create-jobs-release : $(sterile-create-jobs-release)
	$(RM) -r $(units-yaml)

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
