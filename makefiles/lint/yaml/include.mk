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

ifndef --onf-mk-lint-yaml--

$(if $(DEBUG),$(warning ENTER))

##--------------------##
##---]  INCLUDES  [---##
##--------------------##
include $(ONF_MAKEDIR)/lint/yaml/help.mk
include $(ONF_MAKEDIR)/lint/yaml/find_utils.mk
include $(ONF_MAKEDIR)/lint/yaml/install.mk

# [TODO] Consolidate and refactor to support a simpler answer
# Special snowflake linting requirements
-include $(ONF_MAKEDIR)/lint/yaml/byrepo/$(--repo-name--)/include.mk

# Standard lint-yaml targets
include $(ONF_MAKEDIR)/lint/yaml/yamllint.mk

--onf-mk-lint-yaml-- := true#        # Flag to inhibit re-including

$(if $(DEBUG),$(warning LEAVE))

endif # --onf-mk-lint-yaml--

# [EOF]
