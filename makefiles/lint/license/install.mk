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
## Intent: Install the reuse tool
## -----------------------------------------------------------------------

## Define a macro to standardize and simplify access
# REUSE ?= $(venv-activate-bin)/reuse
# REUSE ?= $(activate) && reuse

## -----------------------------------------------------------------------
## Intent: Display reuse command version string.
##   Note: As a side effect, install reuse by dependency
## -----------------------------------------------------------------------
.PHONY: lint-reuse-cmd-version
lint-reuse-cmd-version : $(venv-activate-bin)/reuse

	$(HIDE) echo
	$< --version

## -----------------------------------------------------------------------
## Intent: On-demand instalation of the reuse command
## -----------------------------------------------------------------------
.PHONY: lint-reuse-install
lint-reuse-install         : $(venv-activate-bin)/reuse
$(venv-activate-bin)/reuse : $(venv-activate-script)

	$(call banner-enter,Target $@)
	$(activate) && pip install reuse
	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: Purge reuse tool installation
## -----------------------------------------------------------------------
sterile ::
	$(HIDE)$(RM) "$(venv-abs-bin)/reuse"

## -----------------------------------------------------------------------
## Intent: Display command usage
## -----------------------------------------------------------------------
help::
	@printf '  %-30s %s\n' 'lint-reuse-install'\
      'Install the reuse compliance tool'

# [SEE ALSO]
# -----------------------------------------------------------------------
#   o https://github.com/fsfe/reuse-tool#install

# [EOF]
