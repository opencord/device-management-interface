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

## -----------------------------------------------------------------------
## Intent: Install the doc8 tool
## -----------------------------------------------------------------------
.PHONY: lint-doc8-install

## Define a macro to standardize and simplify access
# DOC8 ?= $(venv-activate-bin)/doc8
# DOC8 ?= $(activate) && doc8

## -----------------------------------------------------------------------
## Intent: Display doc8 command version string.
##   Note: As a side effect, install doc8 by dependency
## -----------------------------------------------------------------------
.PHONY: lint-doc8-cmd-version
lint-doc8-cmd-version : $(venv-activate-bin)/doc8

	$(HIDE) echo
	$< --version

## -----------------------------------------------------------------------
## Intent: On-demand instalation of the doc8 command
## -----------------------------------------------------------------------
lint-doc8-install := $(venv-activate-bin)/doc8
$(lint-doc8-install) : $(venv-activate-script)

	$(call banner-enter,Target $@)
	$(activate) && pip install doc8
	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: Purge doc8 tool installation
## -----------------------------------------------------------------------
sterile ::
	$(HIDE)$(RM) "$(venv-abs-bin)/doc8"
# HIDE)$(RM) -r .venv/lib/*/site-packages/doc8

## -----------------------------------------------------------------------
## Intent: Display command usage
## -----------------------------------------------------------------------
lint-doc8-help ::
	@printf '  %-25.25s %s\n' 'lint-doc8-install' 'Install the doc8 tool'

# [EOF]
