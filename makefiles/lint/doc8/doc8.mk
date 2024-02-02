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

$(if $(DEBUG),$(eval LINT_DOC8_DEBUG=1))

$(if $(LINT_DOC8_DEBUG),$(warning ENTER))

##-------------------##
##---]  GLOBALS  [---##
##-------------------##
.PHONY: lint-doc8 lint-doc8-all lint-doc8-modified

have-doc8-files := $(if $(strip $(DOC8_SOURCE)),true)
DOC8_SOURCE     ?= $(error DOC8_SOURCE= is required)

# -----------------------------------------------------------------------
# Well that is annoying.  Cannot pass two --config switches, doc8 will
# use only one.  Repos have more special exclusions so pass onf-make
# doc8 config as command line args so local makefiles to use --config
# -----------------------------------------------------------------------
# lint-doc8-args += --config $(ONF_MAKEDIR)/lint/doc8/doc8.ini

## -----------------------------------------------------------------------
## -----------------------------------------------------------------------
ifndef NO-LINT-DOC8
  lint-doc8-mode := $(if $(have-doc8-files),mod,all)
  lint : lint-doc8-$(lint-doc8-mode)
endif# NO-LINT-DOC8

## -----------------------------------------------------------------------
# Support consistent lint target names across makefiles
# Clone logic makefiles/lint/shellcheck/shellcheck.mk deps
# *-{mod, src} targets and exclusiosn.
## -----------------------------------------------------------------------
lint-doc8-all : lint-doc8
lint-doc8-mod : lint-doc8
lint-doc8-src : lint-doc8

## -----------------------------------------------------------------------
## Intent: Morph exclusion strings into command line arguments.
##   NOTE: Do not double-quote argument: -ignore-path "$(dir)"
##         Single quotes surrounding exclusion strings added in doc8/excl.mk
##         will become part of exclusion string and fail pattern matching.
## -----------------------------------------------------------------------
## [TODO] - move lint-doc8-excl into doc8.ini (autogenerate)
## -----------------------------------------------------------------------
lint-doc8-excl := $(strip \
  $(foreach dir,$(onf-excl-dirs) $(lint-doc8-excl-raw),\
	$(if $(LINT_DOC8_DEBUG),$(info ** linux-doc8-excl += [$(dir)]))\
    --ignore-path $(dir))\
)

## -----------------------------------------------------------------------
## Usage: make lint-doc8 LINT_DOC8_DEBUG=1
## -----------------------------------------------------------------------
lint-doc8: lint-doc8-cmd-version

	$(call banner-enter,Target $@)
	$(activate) && doc8 $(lint-doc8-excl) $(lint-doc8-args)
	$(call banner-enter,Target $@)

$(if $(LINT_DOC8_DEBUG),$(warning LEAVE))

# [EOF]
