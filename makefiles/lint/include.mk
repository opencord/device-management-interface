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

help ::
	@echo
	@echo "[LINT]"

## Disable python linting in bulk ?
ifdef NO-LINT-PYTHON
  NO-LINT-FLAKE8 := true
  NO-LINT-PYLINT := true
endif

include $(ONF_MAKEDIR)/lint/doc8/include.mk
include $(ONF_MAKEDIR)/lint/golang/include.mk
include $(ONF_MAKEDIR)/lint/groovy/include.mk
include $(ONF_MAKEDIR)/lint/jjb.mk
include $(ONF_MAKEDIR)/lint/json.mk
include $(ONF_MAKEDIR)/lint/license/include.mk
include $(ONF_MAKEDIR)/lint/make/include.mk
include $(ONF_MAKEDIR)/lint/python/include.mk
include $(ONF_MAKEDIR)/lint/shell/include.mk
include $(ONF_MAKEDIR)/lint/tox/include.mk
include $(ONF_MAKEDIR)/lint/yaml/include.mk

include $(ONF_MAKEDIR)/lint/help.mk

$(if $(DEBUG),$(warning LEAVE))

# [EOF]
