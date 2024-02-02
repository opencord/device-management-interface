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
# SPDX-FileCopyrightText: 2024 Open Networking Foundation (ONF) and the ONF Contributors
# SPDX-License-Identifier: Apache-2.0
# -----------------------------------------------------------------------

$(if $(DEBUG),$(warning ENTER))

##-------------------##
##---]  GLOBALS  [---##
##-------------------##
# DEBUG := 1
# DEBUG-onf-mk-paths := 1

## -----------------------------------------------------------------------
## [LOADER] Define path vars based on library include directory
## -----------------------------------------------------------------------
$(foreach makefile,$(lastword $(MAKEFILE_LIST)),\
  $(foreach makedir,$(abspath $(dir $(makefile))),\
    $(eval include $(makedir)/library-makefiles.mk)\
))

$(call gen-mk-paths,onf-mk) # [ALSO] $(call gen-mk-include,onf-mk)

## Missing required vars are fatal
onf-mk-dir ?= $(error onf-mk-dir= is required)
onf-mk-top ?= $(error onf-mk-top= is required)
onf-mk-tmp := $(onf-mk-top)/tmp

ONF_MAKEDIR   := $(onf-mk-dir)#   # TODO: Deprecate ONF_MAKEDIR and MAKEDIR

#--------------------##
##---]  INCLUDES  [---##
##--------------------##
include $(ONF_MAKEDIR)/lint/make/warn-undef-vars.mk  # target lint-make helper

include $(ONF_MAKEDIR)/consts.mk
include $(ONF_MAKEDIR)/help/include.mk       # render target help
include $(ONF_MAKEDIR)/utils/include.mk      # dependency-less helper macros
include $(ONF_MAKEDIR)/etc/include.mk        # banner macros
include $(ONF_MAKEDIR)/commands/include.mk   # Tools and local installers

include $(ONF_MAKEDIR)/virtualenv/include.mk#  # python, lint, JJB dependency
# include $(ONF_MAKEDIR)/patches/include.mk#   # Patch when python 3.10+ in use
include $(ONF_MAKEDIR)/lint/include.mk

include $(ONF_MAKEDIR)/gerrit/include.mk
include $(ONF_MAKEDIR)/git/include.mk
include $(ONF_MAKEDIR)/jjb/include.mk

$(if $(USE-VOLTHA-RELEASE-MK),\
  $(eval include $(ONF_MAKEDIR)/release/include.mk))

include $(ONF_MAKEDIR)/todo.mk
include $(ONF_MAKEDIR)/help/variables.mk

##------------------------------------##
##---]  Languages & Interpreters  [---##
##------------------------------------##
# include $(ONF_MAKEDIR)/src/golang/mod-update.mk

##---------------------##
##---]  ON_DEMAND  [---##
##---------------------##
$(if $(USE-ONF-GERRIT-MK),$(eval include $(ONF_MAKEDIR)/gerrit/include.mk))
$(if $(USE-ONF-DOCKER-MK),$(eval include $(ONF_MAKEDIR)/docker/include.mk))

##-------------------##
##---]  TARGETS  [---##
##-------------------##
include $(ONF_MAKEDIR)/targets/include.mk # clean, sterile

## Display make help text late
include $(ONF_MAKEDIR)/help/trailer.mk

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
