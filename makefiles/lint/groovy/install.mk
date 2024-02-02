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

##-------------------##
##---]  GLOBALS  [---##
##-------------------##
lint-groovy-cmds += $(shell which npm-groovy-lint)
lint-groovy-cmds += $(HOME)/.npm/bin/npm-groovy-lint
lint-groovy-cmds += /usr/bin/npm-groovy-lint
# lint-groovy-cmds += /dev/null#                     # force existence

lint-groovy-cmd = $(firstword $(wildcard $(lint-groovy-cmds)))

##-------------------##
##---]  TARGETS  [---##
##-------------------##
ifndef NO-LINT-GROOVY

  lint : lint-groovy
endif

## -----------------------------------------------------------------------
## Intent: Install npm-groovy-lint
## -----------------------------------------------------------------------
$(lint-groovy-cmd) : lint-groovy-install
lint-groovy-install:

## -----------------------------------------------------------------------
## Intent: Display command help
## -----------------------------------------------------------------------
help-summary ::
	@echo '  lint-groovy-install          Syntax check groovy sources'

# [EOF]

