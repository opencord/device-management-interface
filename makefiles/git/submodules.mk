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

show-submodules:

	$(HIDE)cat .gitmodules

	@echo
	$(HIDE) git submodule

$(if $(DEBUG),$(warning LEAVE))

# https://github.com/lfit/releng-global-jjb/tags
# git checkout v0.86.7
# [crucible:global-jjb] git checkout v0.86.7
# Previous HEAD position was 5dc3432 Update regexp in lf-infra-ship-logs macro
# HEAD is now at c5bd1d3 Fix: Pin urllib3~=1.26.15 in pypi dist jobs

# 5dc3432cae2f13d9e5151a00a76a78ce73d92d70 global-jjb (v0.53.3)
# 0d88f8b7a24b53b1c3e189e30ab94373c51eea91 lf-ansible (0d88f8b)
# 4a5b0cd9032938194c4813fe36663ddee4f9e60e packer/common-packer (v0.1.0~22)

# https://stackoverflow.com/questions/30301510/git-submodule-specify-version
# cd global-jjb
# git checkout v0.86.7
# cd -
# git commit . -m "use submodule v0.86.7"

# https://github.com/lfit/releng-lf-ansible.git
# tag==master, no release

# https://github.com/lfit/releng-common-packer.git
# cd packer/common-packer
# git checkout v0.12.1
# cd -
# git commit . -m "use submodule v0.12.1""

# [EOF]
