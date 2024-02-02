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
## -----------------------------------------------------------------------
## Intent:
##   - This makefile defines logic for interacting with library makefiles.
##   - Derived path construction assigned to make variables.
##   - Avoid duplicate makefile inclusion.
##   - Logic is non-destructive, at most two variables are defined.
## -----------------------------------------------------------------------
## Note:
##   o make function $(foreach) is often used purely for side effects.
##     It will artifically create context allowing declaration of named
##     local variables to improve readability.
## Todo:
##   o GNU Make v4.4 introduced $(let var[, ..var],list,action)
## -----------------------------------------------------------------------
## Usage:
##   include path-to-makefiles/makefiles/include.mk
##     prefix := project-mk
##     $(call gen-mk-paths,{prefix})
##     $(call gen-mk-include,{prefix})
##     $(info makefiles directory ($prefix) is $(project-mk-dir))
## -----------------------------------------------------------------------
##   {prefix}-dir    makefiles/ directory containing include.mk (absolute path)
##   {prefix}-top    sandbox root: path to parent makefile directory that
##                   included {prefix}-dir/makefiles/include.mk
## -----------------------------------------------------------------------

ifndef space
  null  :=#
  space := $(null) $(null)
endif

$(if $(DEBUG),$(eval DEBUG-onf-mk-paths := 1)) # Enabled by global debug flag
$(if $(-onf-mk-paths),$(warning ENTER))

## -----------------------------------------------------------------------
## Intent: Helper function used to trim trailing directory slash from a path
## -----------------------------------------------------------------------
dir-wo-slash = $(strip \
  $(foreach path,$(dir $(1)),\
    $(patsubst %/,%,$(path))\
  ))

## -----------------------------------------------------------------------
## Intent: Include a makefile at most once
## -----------------------------------------------------------------------
## Usage:
##   $(call include-once,path/to/makefile)
## Debug-mode:
##   % make DEBUG-onf-mk-paths=1#
## -----------------------------------------------------------------------
## Given:
##   scalar - path to a makefile (relative or absolute)
## Return:
##   none
## -----------------------------------------------------------------------
## Pre:
##   none
## Post:
##   Define a unique make variable to indicate a makefile has been loaded.
##   include-once-^-^path/to/makefile := true
## -----------------------------------------------------------------------
include-once =\
  $(if $(DEBUG-onf-mk-paths),\
	$(info ** include-once (makefile=$(1))))\
\
  $(foreach makefile,$(1),\
    $(foreach seen,include-once^-^$(makefile),\
    $(if $($(seen)),$(null),\
\
      $(if $(DEBUG-onf-mk-paths),\
        $(info ** $$(eval include $(makefile)))\
        $(info ** $$(eval $(seen) := true))\
      )\
\
      $(eval include $(makefile))\
      $(eval $(seen) := true)\
  )))

## -----------------------------------------------------------------------
## Intent: Given a string prefix conditionally define make variables
##   that reference derived path to a sandbox root directory.
##
##   A sandbox root directory is defined as the directory containing
##   a top level [mM]akefile that includes library makefiles.
## -----------------------------------------------------------------------
## Given:
##    scalar    A string prefix derived paths will be assigned to.
##
## Return:
##    none
## -----------------------------------------------------------------------
## Pre:
##   None
##
## Post: Variable defined containing derived paths:
##   {prefix}-top    Parent directory (makefiles/ removed).
## -----------------------------------------------------------------------
## Usage:
##   prefix := my-mk
##   $(call gen-mk-paths--var-top,$(prefix))
##   $(info sandbox root is $(my-mk-top))
## -----------------------------------------------------------------------
## Note: skip
##   1) skip current makefile: library-makefiles.mk
##   2) skip library makefile: include.mk
##   3) skip library includes: makefiles/%
##   [TODO: verify] $(filter-out makefiles/%) may cover everything
## -----------------------------------------------------------------------
gen-mk-paths--var-top =\
  $(if $(DEBUG-onf-mk-paths),\
	$(info ** gen-mk-paths--var-top (prefix=$(1))))\
\
  $(foreach prefix,$(1),\
    $(foreach skip,$(lastword $(MAKEFILE_LIST)),\
        $(eval skip += makefiles/)\
        $(eval skip += %/include.mk)\
    $(foreach parent,$(lastword \
        $(filter-out $(skip),$(MAKEFILE_LIST))),\
    $(foreach abs-parent,$(abspath $(parent)),\
      $(if $(DEBUG-onf-mk-paths),\
        $(info ** $$(eval $(prefix)-top := $(call dir-wo-slash,$(abs-parent)))))\
      $(eval $(prefix)-top := $(call dir-wo-slash,$(abs-parent)))\
  ))))

## -----------------------------------------------------------------------
## Intent: Given a string prefix conditionally define make variables
##   that reference derived path to a library makefile directory.
##
##   A library makefile directory is defined by existence of a
##   filesystem path that contains makefiles/include.mk.
## -----------------------------------------------------------------------
## Given:
##    scalar    A string prefix derived paths will be assigned to.
##
## Return:
##    none
## -----------------------------------------------------------------------
## Pre:
##   None
##
## Post: Variables defined containing derived paths:
##   {prefix}-abs    Absolute path to include.mk (current makefile).
##   {prefix}-dir    makefiles/ directory containing include.mk
##   {prefix}-top    Parent directory (makefiles/ removed).
## -----------------------------------------------------------------------
## Usage:
##   prefix := my-mk
##   $(call gen-mk-paths--var-dir,$(prefix))
##   $(info library makefile path is $(my-mk-dir))
## -----------------------------------------------------------------------
gen-mk-paths--var-dir =\
  $(if $(DEBUG-onf-mk-paths),\
	$(info ** gen-mk-paths--var-dir (prefix=$(1))))\
\
$(foreach prefix,$(1),\
\
  $(foreach loaded,$(prefix)-dir,\
  $(if $($(loaded)),$(null),\
\
  $(foreach makefile,$(lastword $(filter %/include.mk,$(MAKEFILE_LIST))),\
    $(foreach abs-mk,$(abspath $(makefile)),\
    $(foreach path,$(firstword $(subst /makefiles/,$(space),$(abs-mk))),\
\
      $(if $(DEBUG-onf-mk-paths),\
        $(info ** $$(eval $(prefix)-dir := [$(path)/makefiles])))\
      $(eval $(prefix)-dir := $(path)/makefiles)\
    ))\
  )))\
)

## -----------------------------------------------------------------------
## Intent: Derive paths to library makefile directory and parent makefile
##   that is including the library
## -----------------------------------------------------------------------
## Usage:
##   prefix := my-mk
##   $(call gen-mk-paths,$(prefix))
##   $(info sandbox root is $(my-mk-top))
##   $(info library makefile path is $(my-mk-dir))
## -----------------------------------------------------------------------
gen-mk-paths =\
  $(if $(DEBUG-onf-mk-paths),\
	$(info ** gen-mk-paths (prefix=$(1))))\
\
  $(foreach prefix,$(1),\
    $(call gen-mk-paths--var-dir,$(prefix),$(1))\
    $(call gen-mk-paths--var-top,$(prefix),$(1))\
)

## -----------------------------------------------------------------------
## Intent: Derive paths then include top level library makefile
## -----------------------------------------------------------------------
## Usage:
##   prefix := my-mk
##   $(call gen-mk-include,$(prefix))
##   $(info makefile loaded: $(my-mk-dir)/include.mk)
##   $(info sandbox root is $(my-mk-top))
##   $(info library makefile path is $(my-mk-dir))
## -----------------------------------------------------------------------
gen-mk-include =\
\
  $(if $(DEBUG-onf-mk-paths),\
	$(info ** gen-mk-include (prefix=$(1))))\
\
  $(foreach prefix,$(strip $(1)),\
    $(call gen-mk-paths,$(prefix))\
    $(call include-once,$($(prefix)-dir)/include.mk)\
  )

$(if $(-onf-mk-paths),$(warning LEAVE))

# [EOF]
