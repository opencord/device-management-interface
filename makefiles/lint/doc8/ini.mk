# -*- makefile -*-
# -----------------------------------------------------------------------
# Copyright 2023-2024 Open Networking Foundation (ONF) and the ONF Contributors
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
.PHONY: lint-doc8-ini-tmp

lint-doc8-ini-tmp = $(onf-mk-tmp)/doc8.ini
.DELETE_ON_ERROR  : $(lint-doc8-ini-tmp)
.PHONY            : lint-doc8-ini-tmp $(lint-doc8-ini-tmp)

lint-doc8-ini-tmp : $(lint-doc8-ini-tmp)

# -----------------------------------------------------------------------
# Intent: Doc8(s) --config switch will only accept one argument and
#   configs/exclusions are needed from multiple sources.
#   This target will merge doc8.ini from onf-make/ and local/ for use.
# -----------------------------------------------------------------------
# repo:onf-make is special, MAKEDIR=makefiles/local does not exist.
# -----------------------------------------------------------------------
lint-doc8-ini-raw := $(ONF_MAKEDIR)/lint/doc8/doc8.ini
ifneq ($(--repo-name--),onf-make)
  lint-doc8-ini-raw += $(MAKEDIR)/lint/doc8/doc8.ini
endif

lint-doc8-ini-src = $(wildcard $(lint-doc8-ini-raw))
$(lint-doc8-ini-tmp):

	$(call banner,Target $@)

	@echo "FILES: $(lint-doc8-ini-src)"
	mkdir -p $(dir $@)

	@echo "** [doc8.ini] Generate $@"
	@echo '[doc8]' > $@

	@echo '** [doc8.ini] Merge onf-make and local config options'
	$(HIDE)grep -v --fixed-strings --no-filename \
	    -e '[doc8]' \
	    -e 'ignore-path' \
	    -e 'max-line-length' \
	    $(lint-doc8-ini-src) \
	    >> $@

	@echo '** [doc8.ini] Construct ignore-path='
	@echo -n 'ignore-path = ' >> $@
	$(HIDE)awk -F'=' '/^ignore-path/ {print $$2}' $(lint-doc8-ini-src) \
	   	| paste -sd ',' - \
	    >> $@

#   # Prefer local config setting
	@echo '** [doc8.ini] Extract max-line-length'
	$(HIDE)grep --fixed-strings --no-filename 'max-line-length' $(lint-doc8-ini-src) \
	   | tail -n 1 \
	   >> $@

	$(if $(DEBUG),cat $@)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
clean ::
	$(RM) $(lint-doc8-ini-tmp)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
lint-doc8-help ::
	@printf '  %-25.25s %s\n' 'lint-doc8-ini-tmp' \
  'Create doc8.ini from onf-make/ and local/'

# [EOF]
