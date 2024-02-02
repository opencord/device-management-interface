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
# https://gerrit.opencord.org/plugins/gitiles/onf-make
# ONF.makefiles.lint.groovy.version = 1.1.1 (+local edits)
# -----------------------------------------------------------------------

##-------------------##
##---]  GLOBALS  [---##
##-------------------##

groovy-check      := npm-groovy-lint

groovy-check-args := $(null)
# groovy-check-args += --loglevel info
# groovy-check-args += --ignorepattern
# groovy-check-args += --verbose

##-------------------##
##---]  TARGETS  [---##
##-------------------##

## -----------------------------------------------------------------------
## Intent: Enabled by repository_sandbox_root/config.mk
## -----------------------------------------------------------------------
ifndef NO-LINT-GROOVY
  lint : lint-groovy
endif

## -----------------------------------------------------------------------
## All or on-demand
##   make lint-groovy BY_SRC="a/b/c.groovy d/e/f.groovy"
## -----------------------------------------------------------------------
ifdef GROOVY_SRC
  lint-groovy : lint-groovy-src
else
  lint-groovy : lint-groovy-all
endif

## -----------------------------------------------------------------------
## Intent: Perform a lint check on command line script sources
## -----------------------------------------------------------------------
lint-groovy-all:

	$(call banner-enter,Target $@)

	$(groovy-check) --version
	@echo
	$(HIDE)$(env-clean) find . -iname '*.groovy' -print0 \
  | $(xargs-n1) $(groovy-check) $(groovy-check-args)

	$(call banner-leave,Target $@)

## -----------------------------------------------------------------------
## Intent: On-demand lint checking
## -----------------------------------------------------------------------
lint-groovy-src:
  ifndef GROOVY_SRC
	@echo "ERROR: Usage: $(MAKE) $@ GROOVY_SRC="
	@exit 1
  endif
	$(groovy-check) --version
	@echo
	$(HIDE) $(groovy-check) $(groovy-check-args) $(GROOVY_SRC)

## -----------------------------------------------------------------------
## Intent: Perform lint check on locally modified sources
## -----------------------------------------------------------------------
# lint-groovy-bygit = $(shell git diff --name-only HEAD | grep '\.groovy')
lint-groovy-bygit = $(git status -s | grep '\.sh' | grep -v -e '^D' -e '^?' | cut -c4-)
lint-groovy-mod:
	$(groovy-check) --version
	@echo
	$(foreach fyl,$(lint-groovy-bygit),$(groovy-check) $(groovy-check-args) $(fyl))

## -----------------------------------------------------------------------
## Intent: Display command help
## -----------------------------------------------------------------------
help-summary ::
	@echo '  lint-groovy          Conditionally lint groovy source'
  ifdef VERBOSE
	@echo '  lint-groovy-all      Lint all available sources'
	@echo '  lint-groovy-mod      Lint locally modified (git status)'
	@echo '  lint-groovy-src      Lint individually (BY_SRC=list-of-files)'
  endif

# [EOF]
