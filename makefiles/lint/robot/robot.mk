# -*- makefile -*-
# -----------------------------------------------------------------------
# Copyright 2017-2024 Open Networking Foundation (ONF) and the ONF Contributors
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

$(if $(DEBUG),$(warning ENTER))

##-------------------##
##---]  GLOBALS  [---##
##-------------------##
.PHONY: lint-robot lint-robot-all lint-robot-mod lint-robot-src

have-robot-files := $(if $(strip $(ROBOT_FILES)),true)
ROBOT_FILES      ?= $(error ROBOT_FILES= is required)

robot-check      = $(activate) && rflint
robot-check-args ?= --verbose --configure LineTooLong:130 -e LineTooLong \
             --configure TooManyTestSteps:65 -e TooManyTestSteps \
             --configure TooManyTestCases:50 -e TooManyTestCases \
             --configure TooFewTestSteps:1 \
             --configure TooFewKeywordSteps:1 \
             --configure FileTooLong:2000 -e FileTooLong \
             -e TrailingWhitespace

## -----------------------------------------------------------------------
## Intent: Use the robot command to perform syntax checking.
## -----------------------------------------------------------------------
ifndef NO-LINT-ROBOT
  lint-robot-mode := $(if $(have-robot-files),mod,all)
  lint       : lint-robot
  lint-robot : lint-robot-$(lint-robot-mode)
endif# NO-LINT-ROBOT

## -----------------------------------------------------------------------
## Intent: exhaustive robot syntax checking
## -----------------------------------------------------------------------
lint-robot-all:

	$(call banner-enter,Target $@)

	$(HIDE)$(MAKE) --no-print-directory lint-robot-version
	@find . -iname '*.robot' -print0 \
        | $(xargs-n1) bash -c "$(robot-check) $(robot-check-args)"
	@echo "DONE"

	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: On-demand lint checking
## -----------------------------------------------------------------------
lint-robot-src:
  ifndef ROBOT_SRC
	@echo "ERROR: Usage: $(MAKE) $@ ROBOT_SRC="
	@exit 1
  endif

	$(call banner-enter,Target $@)

	$(HIDE)$(MAKE) --no-print-directory lint-robot-version
	$(HIDE) $(robot-check-args) $(robot-check-args) $(ROBOT_SRC)

	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: Perform lint check on locally modified sources
## -----------------------------------------------------------------------
lint-robot-bygit = $(shell git ls-files -m -o | grep -i '\.robot')
lint-robot-mod:
	$(call banner-enter,Target $@)

	$(HIDE)$(MAKE) --no-print-directory lint-robot-version
	$(foreach fyl,$(lint-robot-bygit),$(robot-check) $(robot-check-args) $(fyl))

	$(call banner-leave,Target $@)

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
