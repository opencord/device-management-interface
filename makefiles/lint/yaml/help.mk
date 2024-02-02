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

## ---------------------------------------------------------------------------
## Intent: Display a help banner early so includes below that also define
##         help targets will be displayed beneath a high level banner.
## ---------------------------------------------------------------------------
help ::
  ifndef VERBOSE
	@echo '  lint-yaml          Invoke all yaml linting targets'
  else
	$(HIDE)$(MAKE) --no-print-directory help-lint-yaml
  endif

## ---------------------------------------------------------------------------
## Intent: Display extended target help
## ---------------------------------------------------------------------------
help-lint-yaml:
	@echo
	@echo '[LINT: yaml]   (make lint-yaml VERBOSE=1)'
	@echo '  lint-yaml          Invoke all yaml linting targets'

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
