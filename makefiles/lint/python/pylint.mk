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
.PHONY: lint-pylint lint-pylint-all lint-pylint-modified

PYTHON_FILES      ?= $(error PYTHON_FILES= required)

## -----------------------------------------------------------------------
## Intent: Use the pylint command to perform syntax checking.
##   o If UNSTABLE=1 syntax check all sources
##   o else only check sources modified by the developer.
## Usage:
##   % make lint UNSTABLE=1
##   % make lint-pylint-all
## -----------------------------------------------------------------------
ifndef NO-LINT-PYLINT
  lint-pylint-mode := $(if $(have-python-files),modified,all)
  lint        : lint-pylint
  lint-pylint : lint-pylint-$(lint-pylint-mode)
endif# NO-LINT-PYLINT

## -----------------------------------------------------------------------
## Intent: exhaustive pylint syntax checking
## -----------------------------------------------------------------------

# Construct: find . \( -name '__ignored__' -o -name dir -o name dir \)
# pylint-find-filter := $(null)
# pylint-find-filter += -name '__ignored__'#   # for alignment
# pylint-find-filter += $(foreach dir,$(onf-excl-dirs),-o -name $(dir)))

# pylint-find-filter := $(call gen-python-find-excl,onf-excl-dirs)
# $(error pylint-find-filter := $(pylint-find-filter))
lint-pylint-all: $(venv-activate-script)
	$(MAKE) --no-print-directory lint-pylint-install

	$(activate) && $(call gen-python-find-cmd) | $(xargs-n1) pylint
#	    | $(xargs-n1-clean) yamllint --strict

## -----------------------------------------------------------------------
## Intent: check deps for format and python3 cleanliness
## Note:
##   pylint --py3k option no longer supported
## -----------------------------------------------------------------------
lint-pylint-modified: $(venv-activate-script)
	$(MAKE) --no-print-directory lint-pylint-install

	$(activate) && pylint $(PYTHON_FILES)

## -----------------------------------------------------------------------
## Intent:
## -----------------------------------------------------------------------
.PHONY: lint-pylint-install
lint-pylint-install: $(venv-activate-script)
	@echo
	@echo "** -----------------------------------------------------------------------"
	@echo "** python pylint syntax checking"
	@echo "** -----------------------------------------------------------------------"
	$(activate) && pip install --upgrade pylint
	$(activate) && pylint --version
	@echo

## -----------------------------------------------------------------------
## Intent: Display command usage
## -----------------------------------------------------------------------
help::
	@echo '  lint-pylint          Syntax check python using the pylint command'
  ifdef VERBOSE
	@echo '  $(MAKE) lint-pylint PYTHON_FILES=...'
	@echo '  lint-pylint-modified  pylint checking: only modified'
	@echo '  lint-pylint-all       pylint checking: exhaustive'
	@echo '  lint-pylint-install   Install the pylint command'
  endif

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
