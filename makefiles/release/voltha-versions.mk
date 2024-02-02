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

##-------------------##
##---]  GLOBALS  [---##
##-------------------##
voltha-versions += master
voltha-versions += voltha-2.12
voltha-versions += voltha-2.11
voltha-versions += voltha-2.8
voltha-versions += playground

# VOLTHA: release
#   active : $(words 0,$(voltha-versions))
#     next : $(words 1,$(voltha-versions))
#     last : $(words 2,$(voltha-versions))

# fatal to make help (param is null)
voltha-version ?= $(error $(MAKE) voltha-verison=voltha-x.yy is required)\

voltha-release-this := $(word 1,$(voltha-versions)) 
voltha-release-last := $(word 2,$(voltha-versions))

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
