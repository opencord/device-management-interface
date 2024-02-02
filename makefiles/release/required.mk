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
# Intent: Conditionally load when named targets are requested.
#   var ?= $(error ...) definitions are fatal to "make help" and others
# -----------------------------------------------------------------------

voltha-release-mk-targets := $(NULL)
voltha-release-mk-targets += create-jobs-release
voltha-release-mk-targets += create-jobs-release-certification
voltha-release-mk-targets += create-jobs-release-nightly
voltha-release-mk-targets += create-jobs-release-units
voltha-release-mk-targets += sterile-create-jobs-release

# -----------------------------------------------------------------------
# Define a flag to only load release targets when mentioned by name
# Makefile can also explicitly define the flag to force always loading.
# -----------------------------------------------------------------------
$(foreach tgt,$(voltha-release-mk-targets),\
  $(if $(findstring $(tgt),$(MAKECMDGOALS)),$(eval USE_VOLTHA_RELEASE_MK := true))\
)

# [EOF]
