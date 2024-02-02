# -*- makefile -*-
# -----------------------------------------------------------------------
# Copyright 2017-2024 Open Networking Foundation (ONF) and the ONF Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License")
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
.PHONY: lint-yaml lint-yaml-all lint-yaml-modified

have-yaml-files := $(if $(strip $(YAML_FILES)),true)
YAML_FILES      ?= $(error YAML_FILES= is required)

YAMLLINT = $(activate) && yamllint
yamllint-args += --strict

## -----------------------------------------------------------------------
## Intent: Use the yaml command to perform syntax checking.
## -----------------------------------------------------------------------
ifndef NO-LINT-YAML
  lint-yaml-mode := $(if $(have-yaml-files),modified,all)
  lint      : lint-yaml
  lint-yaml : lint-yaml-$(lint-yaml-mode)
endif# NO-LINT-YAML

## -----------------------------------------------------------------------
## Intent: exhaustive yaml syntax checking
## -----------------------------------------------------------------------
lint-yaml-all: lint-yaml-cmd-version

	$(call banner-enter,Target $@)
	$(HIDE)$(MAKE) --no-print-directory lint-yaml-install
	$(HIDE)$(activate) && $(call gen-yaml-find-cmd) \
	    | $(env-clean) $(xargs-cmd) -I'{}' \
		bash -c "$(YAMLLINT) $(yamllint-args) {}"
	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: check deps for format and python3 cleanliness
## Note:
##   yaml --py3k option no longer supported
## -----------------------------------------------------------------------
lint-yaml-modified: lint-yaml-cmd-version

	$(call banner-enter,Target $@)
	$(HIDE)$(MAKE) --no-print-directory lint-yaml-install
	$(YAMLLINT) $(yamllint-args) $(YAML_FILES)
	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: Display command usage
## -----------------------------------------------------------------------
help::
	@echo '  lint-yaml          Syntax check python using the yaml command'
  ifdef VERBOSE
	@echo '  $(MAKE) lint-yaml YAML_FILES=...'
	@echo '  lint-yaml-all       yaml checking: exhaustive'
	@echo '  lint-yaml-modified  yaml checking: only locally modified'
	@echo '  lint-yaml-install   Install the pylint command'
  endif

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
