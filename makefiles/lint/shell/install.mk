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
lint-shell-dflt := $(venv-activate-bin)/shellcheck

lint-shell-cmds += $(shell which shellcheck)
lint-shell-cmds += $(lint-shell-dflt)
lint-shell-cmds += /usr/bin/shellcheck

lint-shell-cmd = \
  $(strip \
    $(firstword \
      $(wildcard $(lint-shell-cmds)) \
      $(lint-shell-dflt) \
  ))
lint-shell-cmd := $(venv-activate-bin)/shellcheck

##-------------------##
##---]  TARGETS  [---##
##-------------------##

## -----------------------------------------------------------------------
## Intent: Display shellcheck command version string.
##   Note: As a side effect, install shellcheck by dependency
## -----------------------------------------------------------------------
## Verified: v0.8.0
## -----------------------------------------------------------------------
.PHONY: lint-shellcheck-cmd-version
lint-shellcheck-cmd-version : $(lint-shell-cmd)

	$(HIDE) echo
	$< --version

## -----------------------------------------------------------------------
## Intent: Install shellcheck
## -----------------------------------------------------------------------
## Note: .venv/bin is somewhat odd for an install directory but:
##   o avoids existence and conflict problems with ./bin.
##   o auto-exclude from consideration by lint and test targets.
## -----------------------------------------------------------------------
## Verified: v0.8.0
## -----------------------------------------------------------------------

lint-shell-download = https://github.com/koalaman/shellcheck/releases/download/$(1)/shellcheck-$(1).$(2).x86_64.tar.xz

lint-shell-downloads=\
	$(call lint-shell-download,v0.9.0,darwin)\
	$(call lint-shell-download,v0.9.0,linux)

## -----------------------------------------------------------------------
## Intent: Retrieve and install the shellcheck command.
## -----------------------------------------------------------------------
## Cannot pass wildcards to wget, download endpoint must be dynamic.
## Attempts to glob using curl or wget returns "not found".
##   wget -r -l1 --no-parent -A.xz \
##     'https://github.com/koalaman/shellcheck/releases/download/v0.9.0
## -----------------------------------------------------------------------

.PHONY: lint-shell-install
lint-shell-install : $(lint-shell-cmd)
$(lint-shell-cmd)  :

	$(call banner-enter,(Target $@))

	$(call banner,(shellcheck: Download))
	$(HIDE)wget --quiet --unlink $(lint-shell-downloads)
	$(HIDE)umask 022 && mkdir -p $(dir $@)

	$(call banner,(shellcheck: Unpack and install))
	$(HIDE)case "$(uname -s)" in \
	    *arwin*) tar Jxf *darwin*.tar.xz -C $(dir $@) --strip-components=1 ;; \
	          *) tar Jxf *linux*.tar.xz  -C $(dir $@) --strip-components=1 ;; \
	esac

	$(HIDE)$(RM) $(notdir $(lint-shell-downloads))

	$(call banner-leave,(Target $@))

## -----------------------------------------------------------------------
## -----------------------------------------------------------------------
sterile ::
	$(RM) $(lint-shell-downloads)

## -----------------------------------------------------------------------
## Intent: Display command help
## -----------------------------------------------------------------------
lint-shell-help ::
	@printf '  %-30s %s\n' 'lint-shell-install' \
      'Install syntax checking tool shellcheck'
	@printf '  %-30s %s\n' 'lint-shellcheck-cmd-version' \
	  'Library target able to display version of shellcheck command'

# [EOF]
