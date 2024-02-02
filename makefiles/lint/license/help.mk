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

$(if $(DEBUG),$(warning ENTER))

## -----------------------------------------------------------------------
## Intent: Display topic help
## -----------------------------------------------------------------------
help-summary ::
	@printf '  %-30s %s\n' 'lint-reuse'\
      'License syntax check'
	@printf '  %-30s %s\n' 'lint-reuse-help'\
	  'Show verbose target help'
	@printf '  %-30s %s\n' 'lint-license'\
      'See target lint-reuse'
  ifdef VERBOSE
	@$(MAKE) --no-print-directory lint-reuse-help
  endif

## -----------------------------------------------------------------------
## Intent: Display extended topic help
## -----------------------------------------------------------------------
.PHONY: lint-reuse-help
lint-reuse-help ::
	@printf '  %-30s %s\n' 'lint-reuse-all'\
	  'License check available sources'
	@printf '  %-30s %s\n' 'lint-reuse-mod'\
	  'License check locally modified files (git status)'
	@printf '  %-30s %s\n' 'lint-reuse-src'\
	  'License check files by path'

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
