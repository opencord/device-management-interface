# -*- makefile -*-
## -----------------------------------------------------------------------
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
# -----------------------------------------------------------------------
# Intent:
#   This makefile defines dependencies that will install a python virtualenv
#   beneath $(sandbox)/.venv/.  The $(activate) macro is used to source
#   .venv/bin/activate allowing command python and pip to be used.
# -----------------------------------------------------------------------
# Usage:
#   include makefiles/virtualenv/include.mk
#
# Makefile Target Dependencies:
#     tgt : $(venv-activate-patched)      # python 3.10+ local use
#     tgt : $(venv-activate-script)       # python < v3.8
#
# Make definitions (convenience macros used for command access)
#   PIP    := $(activate) && pip          # invoke pip from virtualenv
#   PYTHON := $(activate) && python       # invoke python from virtualenv
#
# Target declaration and command invocation:
#   my-target : $(venv-activate-script)   # dependency installs virtualenv
#   <tab>$(PYTHON) --version              # invoke python with arguments
#	<tab>$(PYTHON) my-command.py
#	<tab>$(activate) && pip install foobar
#
#   % make my-target                      # Invoke make target from shell
# -----------------------------------------------------------------------

$(if $(DEBUG),$(warning ENTER))

##-------------------##
##---]  GLOBALS  [---##
##-------------------##
.PHONY: venv venv-patched

##------------------##
##---]  LOCALS  [---##
##------------------##
venv-name            ?= .venv#                            # default install directory
venv-abs-path        := $(PWD)/$(venv-name)#              #
venv-activate-bin    := $(venv-name)/bin#                 # no whitespace
venv-activate-script := $(venv-activate-bin)/activate#    # dependency

# ------------------------------------------------------------------------
# Intent: Define macro activate= to access virtualenv activation script.
#  Usage:
#    - $(activate) && python             # Syntax inlined within a target
#    - PYTHON := $(activate) && python   # Define a named command macro
# ------------------------------------------------------------------------
activate             ?= set +u && source $(venv-activate-script) && set -u

## -----------------------------------------------------------------------
## Intent: Activate script path dependency
## Usage:
##    o place on the right side of colon as a target dependency
##    o When the script does not exist install the virtual env and display.
## -----------------------------------------------------------------------
$(venv-activate-script):
	@echo
	@echo '============================='
	@echo 'Installing python virtual env'
	@echo '============================='
	virtualenv -p python3 $(venv-name)
	$(activate) && python -m pip install --upgrade pip
	$(activate) && pip install --upgrade setuptools
	$(activate) && [[ -r requirements.txt ]] \
	    && { python -m pip install -r requirements.txt; } \
	    || { /bin/true; }

	$(activate) && python --version

## -----------------------------------------------------------------------
## Intent: Explicit named installer target w/o dependencies.
##         Makefile targets should depend on venv-activate-script.
## -----------------------------------------------------------------------
venv-activate-patched := $(venv-activate-script).patched
venv-activate-patched : $(venv-activate-patched)
$(venv-activate-patched) : $(venv-activate-script)
	$(call banner-enter,Target $@)
	$(ONF_MAKEDIR)/virtualenv/python_310_migration.sh
	touch $@
	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: Explicit named installer target w/o dependencies.
##         Makefile targets should depend on venv-activate-script.
## -----------------------------------------------------------------------
venv         : $(venv-activate-script)
venv-patched : $(venv-activate-patched)

## -----------------------------------------------------------------------
## Intent: Revert installation to a clean checkout
## -----------------------------------------------------------------------
sterile :: clean
	$(RM) -r "$(venv-abs-path)"

## -----------------------------------------------------------------------
## -----------------------------------------------------------------------
help ::
	@echo
	@echo '[VIRTUAL ENV]'
	@echo '  venv                Create a python virtual environment'
	@echo '    venv-name=        Subdir name for virtualenv install'
	@echo '  venv-activate-script         make macro name'
	@echo '      $$(target) dependency    install python virtualenv'
	@echo '      source $$(macro) && cmd  configure env and run cmd'

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
