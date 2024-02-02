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
## Intent: Install the yamllint tool
## -----------------------------------------------------------------------
.PHONY: lint-yaml-install

# -----------------------------------------------------------------------
# We can(/should?) define a command macro
# wait a bit until use cases are better known.
# Initial use required inserting xargs bash -c "$(YAMLLINT) {}"
# -----------------------------------------------------------------------
# YAMLLINT ?= $(venv-activate-bin)/yamllint
# YAMLLINT ?= $(activate) && yamllint

## -----------------------------------------------------------------------
## Intent: Display yamllint command version string.
##   Note: As a side effect, install yamllint by dependency
## -----------------------------------------------------------------------
.PHONY: lint-yaml-cmd-version
lint-yaml-cmd-version : $(venv-activate-bin)/yamllint

	$(HIDE) echo
	$< --version

## -----------------------------------------------------------------------
## Intent: On-demand instalation of the yamllint command
## -----------------------------------------------------------------------
lint-yaml-install := $(venv-activate-bin)/yamllint
$(lint-yaml-install) : $(venv-activate-script)

	$(call banner-enter,Target $@)
	$(activate) && pip install yamllint
	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: Purge yamllint tool installation
## -----------------------------------------------------------------------
sterile ::
	$(HIDE)$(RM) "$(venv-abs-bin)/yamllint"
	$(HIDE)$(RM) -r .venv/lib/*/site-packages/yamllint

        # Remove both file:command and dir:libraries
        # find "$(venv-abs-path)" -iname 'yamllint' -print0 \
        #    | $(xargs-n1-clean) $(RM) -r {}

## -----------------------------------------------------------------------
## Intent: Display command usage
## -----------------------------------------------------------------------
help::
	@echo '  lint-yaml-install       Install the yamllint tool'

# [EOF]
