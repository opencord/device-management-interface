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
jjb-gen-dir := build
# JJB_DEBUG := true

##-------------------##
##---]  TARGETS  [---##
##-------------------##
all: help

## -----------------------------------------------------------------------
## Intent: Generate pipeline jobs
## -----------------------------------------------------------------------
.PHONY: jjb-gen

jjb-gen-args := $(null)
$(if $(JJB_DEBUG),$(eval jjb-gen-args += --log_level DEBUG))

jjb-gen-log := $(jjb-gen-dir)/jjb-gen.log
jjb-gen: $(venv-activate-script)

	$(call banner-enter,Target $@)
	@mkdir -p $(jjb-gen-dir)
	@touch "$(jjb-gen-dir)/.sentinel"
	( \
	  $(activate) \
	     && jenkins-jobs $(jjb-gen-args) test $(PWD)/jjb -o $(jjb-gen-dir) 3>&1 2>&1 \
	) | tee "$(jjb-gen-log)"

  ifdef LOGS
	-@less "$(jjb-gen-log)"
  endif

  ifdef VERBOSE
	@echo
	@echo "** Display generated pipelines"
	find "$(jjb-gen-dir)" -newer "$(jjb-gen-dir)/.sentinel" -ls
  endif

	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## -----------------------------------------------------------------------
sterile ::
	$(RM) -r $(jjb-gen-dir)

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
