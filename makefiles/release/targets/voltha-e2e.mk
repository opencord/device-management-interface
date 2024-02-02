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
# Intent: Helper makefile target used to setup for a release
# -----------------------------------------------------------------------

$(if $(DEBUG),$(warning ENTER))

## ---------------------------------------------------------------------------
## Intent: Create branch driven nightly test jobs.
##   o Clone config for the last nightly release
##   o In-place edit to the latest version.
## ---------------------------------------------------------------------------
## NOTE: WIP - nightly jobs have not yet migrated from the mega job config file
## ---------------------------------------------------------------------------
voltha-e2e-dir  := $(release-mk-top)/jjb/voltha-e2e
voltha-e2e-yaml := $(voltha-e2e-dir)/$(voltha-version).yaml
voltha-e2e-tmpl := $(voltha-e2e-dir)/$(voltha-release-last).yaml

create-jobs-release-e2e : $(voltha-e2e-yaml)
$(voltha-e2e-yaml) : $(voltha-e2e-tmpl)

	@echo
	@echo "** Create branch driven pipeline: nightly tests"
	sed -e 's/$(last-release)/$(voltha-version)/g' $< > $@
	$(HIDE)/bin/ls -l $(dir $@)

## ---------------------------------------------------------------------------
## Intent: Create branch driven nightly test jobs.
## ---------------------------------------------------------------------------
$(voltha-e2e-tmpl):
	@echo "ERROR: Yaml template branch does not exist: $@"
	@echo 1

## ---------------------------------------------------------------------------
## Intent: Create branch driven nightly test jobs.
## ---------------------------------------------------------------------------
sterile-create-jobs-release-e2e :
	$(RM) $(voltha-e2e-yaml)

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
