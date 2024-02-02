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
.PHONY: lint-flake8 lint-flake8-all lint-flake8-modified

PYTHON_FILES      ?= $(error PYTHON_FILES= required)

## -----------------------------------------------------------------------
## Intent: Use the flake8 command to perform syntax checking.
## Usage:
##   % make lint
##   % make lint-flake8-all
## -----------------------------------------------------------------------
ifndef NO-LINT-FLAKE8
  lint-flake8-mode := $(if $(have-python-files),modified,all)
  lint        : lint-flake8
  lint-flake8 : lint-flake8-$(lint-flake8-mode)
endif# NO-LINT-FLAKE8

## -----------------------------------------------------------------------
## Intent: exhaustive flake8 syntax checking
## -----------------------------------------------------------------------
# Construct: find . \( -name '__ignored__' -o -name dir -o name dir \)
# flake8-find-filter := $(null)
# flake8-find-filter += -name '__ignored__'#    # for alignment
# flake8-find-filter += $(foreach dir,$(onf-excl-dirs),-o -name $(dir)))

lint-flake8-all: $(venv-activate-script)
	$(HIDE)$(MAKE) --no-print-directory lint-flake8-install

	$(activate) && $(call gen-python-find-cmd) \
	    | $(xargs-n1) flake8 --max-line-length=99 --count

#  && find . \( $(flake8-find-filter) \) -prune -o -name '*.py' -print0 \
# 	| $(xargs-n1) flake8 --max-line-length=99 --count

## -----------------------------------------------------------------------
## Intent: check deps for format and python3 cleanliness
## Note:
##   pylint --py3k option no longer supported
## -----------------------------------------------------------------------
lint-flake8-modified: $(venv-activate-script)
	$(HIDE)$(MAKE) --no-print-directory lint-flake8-install

	$(activate)\
 && flake8 --max-line-length=99 --count $(PYTHON_FILES)

## -----------------------------------------------------------------------
## Intent:
## -----------------------------------------------------------------------
.PHONY: lint-flake8-install
lint-flake8-install: $(venv-activate-script)
	@echo
	@echo "** -----------------------------------------------------------------------"
	@echo "** python flake8 syntax checking"
	@echo "** -----------------------------------------------------------------------"
	$(activate) && pip install --upgrade flake8
	$(activate) && flake8 --version
	@echo

## -----------------------------------------------------------------------
## Intent: Display command usage
## -----------------------------------------------------------------------
help::
	@echo '  lint-flake8          Syntax check python using the flake8 command'
  ifdef VERBOSE
	@echo '  $(MAKE) lint-pylint PYTHON_FILES=...'
	@echo '  lint-flake8-modified  flake8 checking: only modified'
	@echo '  lint-flake8-all       flake8 checking: exhaustive'
	@echo '  lint-flake8-install   Install the flake8 command'
  endif

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
