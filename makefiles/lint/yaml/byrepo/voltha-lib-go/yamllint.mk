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
#
# SPDX-FileCopyrightText: 2024 Open Networking Foundation (ONF) and the ONF Contributors
# SPDX-License-Identifier: Apache-2.0
# -----------------------------------------------------------------------

$(if $(DEBUG),$(warning ENTER))

--onf-mk-lint-yaml-- := true#       # Inhibit loading downstream lint-yaml targets

# yamllint      := $(env-clean) yamllint
# yamllint      := $(activate) && yamllint

YAMLLINT = $(activate) && yamllint

## -------------------------------
## Add requirement(s) for checking
## -------------------------------
yamllint-cfg  := yamllint.helm
yamllint-conf = $(wildcard $(yamllint-cfg) $(ONF_MAKEDIR)/lint/yaml/$(yamllint-cfg))
yamllint-args += $(addprefix --config-file$(space),$(yamllint-conf))
yamllint-args += --strict

## -----------------------------------------------------------------------
## Intent: Use the yaml command to perform syntax checking.
## -----------------------------------------------------------------------
ifndef NO-LINT-YAML
  # lint-yaml-mode := $(if $(have-yaml-files),modified,all)
  lint      : lint-yaml
  lint-yaml : lint-yaml-votlha-lib-go
#  lint-yaml : lint-yaml-all-votlha-lib-go-$(lint-yaml-mode)
endif# NO-LINT-YAML

## -----------------------------------------------------------------------
## ----------------------------------------------------------------------
lint-yaml-votlha-lib-go: lint-yaml-cmd-version

	$(call banner-enter,Target $@)
	$(HIDE)$(MAKE) --no-print-directory lint-yaml-install

	$(HIDE)$(env-clean) $(call gen-yaml-find-cmd) \
	    | $(env-clean) $(xargs-cmd) -I'{}' \
		bash -c "$(YAMLLINT) $(yamllint-args) {}"
	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: Display command usage
## -----------------------------------------------------------------------
help::
  # lint-yaml help already displayed by lint/yaml/help.mk
  ifdef VERBOSE
	@echo '  $(MAKE) lint-yaml YAML_FILES=...'
	@echo '  lint-yaml-votlha-lib-go   lint-yaml for repo:voltha-lib-go'
  endif

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
