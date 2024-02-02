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

##-------------------##
##---]  GLOBALS  [---##
##-------------------##
.PHONY: lint-shell lint-shell-all lint-shell-mod lint-shell-src

# Gather sources to check
shell-check-find := find .
shell-check-find += -name 'vendor' -prune
shell-check-find += -o \( -name '*.sh' -o -name '*.bash' \)
shell-check-find += -type f -print0

# shell-check    := $(env-clean) shellcheck
shell-check      := shellcheck

shell-check-args += --check-sourced

##------------------##
##---]  MACROS  [---##
##------------------##

## -----------------------------------------------------------------------
## Intent: Derive a list of dependencies when make builds a target by name
## -----------------------------------------------------------------------
## Given:
##   target  - Makefile target name to check if evaluating
##   listref - An indirect make variable containing a list of file paths
##
## Return:
##   target  - Variable assigned a list of target dependencies
## -----------------------------------------------------------------------
## Usage: $(gen-lint-shell-deps,lint-shell-mod,BY_GIT)
##    lint-shell-mod := foo bar tans fans
##    lint-shell-mod : $(lint-shell-mod)
##    $(lint-shell-mod):
##        perform-action-on-one-dependency $@
## -----------------------------------------------------------------------
gen-lint-shell-deps =\
  $(strip \
    $(foreach target,$(1),\
      $(if $(findstring $(target),$(MAKECMDGOALS)),\
      $(foreach listref,$(2),\
      $(eval $(target) := $(null))\
      $(foreach path,$($(listref)),\
        $(if $(DEBUG),$(info ** $$(eval $(target) += $(addprefix $(target)--,$(path)))))\
        $(eval $(target) += $(addprefix $(target)--,$(path)))\
      )\
    )\
    )\
  )\
)# gen-lint-shell-deps()

##-------------------##
##---]  TARGETS  [---##
##-------------------##
ifndef NO-LINT-SHELL # enabled(?)
  lint : lint-shell
endif

## -----------------------------------------------------------------------
## Conditional target: lint all source or source by name
## -----------------------------------------------------------------------
ifdef SHELL_SRC
  lint-shell : lint-shell-src
else
  lint-shell : lint-shell-all
endif

## -----------------------------------------------------------------------
## Intent: Perform a lint check on available sources
##   1) Display shellcheck version
##   2) Invoke shellcheck on all files with an *.sh extension
## -----------------------------------------------------------------------
lint-shell-all: lint-shellcheck-cmd-version

    # $(call banner-enter,(Target $@))
	$(env-clean) $(shell-check-find) \
	    | $(xargs-n1) $(shell-check) $(shell-check-args)
    # $(call banner-leave,(Target $@))

## -----------------------------------------------------------------------
## Intent: Perform lint check on a named list of files passed in
##   1) Display shellcheck version
##   2) Iterate and run shellcheck on each given file path.
## -----------------------------------------------------------------------
SHELL_SRC ?= $(error $(MAKE) $@ SHELL_SRC= is required)
$(call gen-lint-shell-deps,lint-shell-src,SHELL_SRC)

lint-shell-src: \
  lint-shellcheck-cmd-version \
  $(lint-shell-src)

## -----------------------------------------------------------------------
## Intent: Perform lint check on locally modified files
##   1) Display shellcheck version
##   2) Gather a list of locally modified files (~git status)
##   3) Iterate and run shellcheck on each gathered file.
## -----------------------------------------------------------------------
BY_GIT = $(shell git diff --name-only HEAD | grep -e '\.sh')
$(call gen-lint-shell-deps,lint-shell-mod,BY_GIT)

lint-shell-mod :\
  lint-shellcheck-cmd-version \
  $(lint-shell-mod)

## -----------------------------------------------------------------------
## Intent: Workhorse target:
##    1) gen-lint-shell-deps used to create target specific dependency lists.
##    2) These dependencies are used to invoke shellcheck against a single
##       path from the list.
##    3) lint-shell-mod : $(lint-shell-mod)
##       Named targets are dependent on a list of file to check.
##    4) make lint-shell-mod
##       Building a named target will force iteration, running shellcheck
##       against each file path in the dependency list.
## -----------------------------------------------------------------------
.PHONY: $(lint-shell-mod)
.PHONY: $(lint-shell-src)
$(lint-shell-mod) $(lint-shell-src):
	$(env-clean) $(shell-check) $(shell-check-args) $(lastword $(subst --,$(space),$@))

$(if $(DEBUG),$(warning LEAVE))

# [TODO]
# -----------------------------------------------------------------------
# Implement exclusion lists by appling $(filter-out $(lint-shell-excl))
# against the list of files passed to gen-lint-shell-deps.  Not definining
# a target dependency will inhibit runnig shellcheck on a file.

# Ignore vendor/ scripts but they really should be lintable
# lint-shell-excl += 'vendor'
# -----------------------------------------------------------------------

# [EOF]
