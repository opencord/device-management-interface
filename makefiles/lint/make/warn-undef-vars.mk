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
# SPDX-FileCopyrightText: 2024 Open Networking Foundation (ONF) and the ONF Contributors
# SPDX-License-Identifier: Apache-2.0
# -----------------------------------------------------------------------

$(if $(DEBUG),$(warning ENTER))

## -----------------------------------------------------------------------
## Intent: Target lint-make* undef var warnings:
##   o This helper makefile defines var := $(null) for known variables.
##   o Definitions only exist for lint target use.
##   o Decrease warning volume until undef sources can be cleaned up.
## -----------------------------------------------------------------------
$(if $(findstring --warn-undefined-variables,$(MAKEFLAGS)),\
	$(eval IS-WARN-UNDEFINED-VARIABLES := true))

ifdef IS-WARN-UNDEFINED-VARIABLES
  export null :=#

  # ----------------------------------------
  # Helper macro
  # Usage: $(call define-if-undef,{varname})
  # ----------------------------------------
  define-if-undef =\
    $(if $(findstring undef,$(flavor $(1))),\
      $(if $(DEBUG),$(info ** $$(eval export $(1) := $$(null))))\
      $(eval export $(1) := $(null))\
    )

  # ----------------------------------------------
  # Faux defines used to shorten lint error volume
  # ----------------------------------------------
  $(call define-if-undef,WORKSPACE)#   Jenkins: yes, interactive: no
  $(call define-if-undef,NULL)#        s/NULL/null
  $(call define-if-undef,UNSTABLE)#    enable raw bulk warnings for pylint
  $(call define-if-undef,JJB_DEBUG)

  # Helpers for transition of local makefiles to repo:onf-make
  $(call define-if-undef,USE-ONF-DOCKER-MK)
  $(call define-if-undef,USE-ONF-GERRIT-MK)
  $(call define-if-undef,USE-VOLTHA-RELEASE-MK)

  # ------------------------------------------------------------------
  # Future make:
  #   o detect available sources
  #   o enable features based on source detection
  #   o conditional makefile library loading based on source detection
  # ------------------------------------------------------------------
  $(call define-if-undef,DOC8_SOURCE)
  $(call define-if-undef,have-python-files)

endif # IS-WARN-UNDEFINED-VARIABLES

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
