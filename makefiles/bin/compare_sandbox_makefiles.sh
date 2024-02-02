#!/bin/bash
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
# https://gerrit.opencord.org/plugins/gitiles/onf-make
# ONF.makefile.version = 1.0
# -----------------------------------------------------------------------
# Intent: This script is used to bulk refactor and merge makefile changes
##  between development repositories and repo:onf-make.
## -----------------------------------------------------------------------

## -----------------------------------------------------------------------
## Intent:
## -----------------------------------------------------------------------
function error
{
    echo "$*"
    exit 1
}

##----------------##
##---]  MAIN  [---##
##----------------##
src="$HOME/projects/sandbox/onf-make/makefiles"

dst="$(realpath .)"

[[ $# -eq 0 ]] && error "At least one directory or file is required"

while [ $# -gt 0 ]; do
    fyl=$1; shift

    echo "FYL: $fyl"
    if [ -d "$fyl" ]; then
	readarray -t fyls < <(find "$fyl" -type f -print)
	[[ ${#@} -gt 0 ]] && fyls+=("$@")
	# declare -p fyls
	[[ ${#fyls} -gt 0 ]] && set -- "${fyls[@]}"
	continue
    fi

    case "$fyl" in
  	    *~) continue ;;
  	 '#*#') continue ;;
	'\.#*') continue ;;
    esac
    
    src0="$src/$fyl"
    dst0="$dst/$fyl"

    [[ ! -e "$src0" ]] && error "File does not exist in src= $src0"
    [[ ! -e "$dst0" ]] && error "File does not exist in dst= $dst0"

    if ! diff -qr "$src0" "$dst0"; then
	emacs "$src0" "$dst0"
    fi
done

# [EOF]
