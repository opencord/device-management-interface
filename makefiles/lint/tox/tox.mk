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

##-------------------##
##---]  GLOBALS  [---##
##-------------------##
.PHONY: lint-tox lint-tox-all lint-tox-modified

PYTHON_FILES      ?= $(error PYTHON_FILES= required)

## -----------------------------------------------------------------------
## Intent: Sanity check incoming JJB config changes.
##   Todo: Depend on makefiles/lint/jjb.mk :: lint-jjb
## -----------------------------------------------------------------------
ifndef NO-LINT-TOX
  lint-tox-mode := $(if $(have-python-files),modified,all)
  lint     : lint-tox
  lint-tox : lint-tox-$(lint-tox-mode)
endif# NO-LINT-TOX

## -----------------------------------------------------------------------
## Intent: Invoke tox on all sources
## -----------------------------------------------------------------------
lint-tox-all: $(venv-activate-script)
	$(MAKE) --no-print-directory lint-tox-install

	$(activate) && tox -e py310

## -----------------------------------------------------------------------
## Intent: Invoke tox on modified sources (target is mainly for consistency)
## -----------------------------------------------------------------------
lint-tox-modified: $(venv-activate-script)
	$(MAKE) --no-print-directory lint-tox-install

	$(activate) && tox -e py310 $(PYTHON_FILES)

## -----------------------------------------------------------------------
## Intent: https://tox.wiki/en/4.6.4/installation.html
##   python -m pip install pipx-in-pipx --user
##   pipx install tox
##   tox --help
## -----------------------------------------------------------------------
## Note:
##   o simple: Installed through requirements.txt
##   o This target can make usage on-demand.
## -----------------------------------------------------------------------
.PHONY: lint-tox-install
lint-tox-install: $(venv-activate-script)
	@echo
	@echo "** -----------------------------------------------------------------------"
	@echo "** python tox syntax checking"
	@echo "** -----------------------------------------------------------------------"
	$(activate) && pip install --upgrade tox
	$(activate) && tox --version
	@echo


## -----------------------------------------------------------------------
## Intent: Display command usage
## -----------------------------------------------------------------------
help::
	@echo '  lint-tox             Invoke the tox test command'
  ifdef VERBOSE
	@echo '  $(MAKE) lint-tox PYTHON_FILES=...'
	@echo '  lint-tox-modified  tox checking: only modified'
	@echo '  lint-tox-all       tox checking: exhaustive'
	@echo '  lint-tox-install     Install the tox command'
  endif

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
