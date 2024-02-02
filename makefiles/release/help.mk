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

## ---------------------------------------------------------------------------
## Intent: Display supported targets
## ---------------------------------------------------------------------------
help-voltha-release :
	@echo
	@echo '[RELEASE] - Create branch driven testing pipelines'
	@echo '  create-jobs-release'
	@echo '  create-jobs-release-bat            Build and test jobs'
	@echo '  create-jobs-release-e2e            End-to-End testing'
	@echo '  create-jobs-release-certification  Certification testing'
	@echo '  create-jobs-release-nightly        Nightly testing'
	@echo '  create-jobs-release-units          Unit testing'

	@echo '  sterile-create-jobs-release        Purge pipeline job content'

help ::
	@echo '  help-voltha-release Display voltha release targets'

# [EOF]
