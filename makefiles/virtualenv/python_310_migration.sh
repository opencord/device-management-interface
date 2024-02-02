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
# -----------------------------------------------------------------------

##-------------------##
##---]  GLOBALS  [---##
##-------------------##
set -euo pipefail

## -----------------------------------------------------------------------
## Intent: Display script documentation.
## -----------------------------------------------------------------------
function show_help()
{
    cat <<EOH
Usage: $0
  apply    Patch virtualenv python modules by version (3.10+).
  backup   Create a tarball for work-in-progress.
  gather   Display a list of potential source files to patch.

  --venv   Installed venv directory to patch (override default)
  --help   This message

See Also
  patches/README.md       Howto create a patch file.

EOH
    exit 0
}

##----------------##
##---]  MAIN  [---##
##----------------##
declare dst='.venv'  # "vst_venv"
declare src="staging"
declare pat="patches"

## -----------------------
## Slurp available patches
## -----------------------
pushd "$pat" >/dev/null
readarray -t fyls < <(find . -name 'patch' -print)
popd         >/dev/null

if [ $# -eq 0 ]; then set -- apply; fi

while [ $# -gt 0 ]; do
    opt="$1"; shift
    case "$opt" in

	-*help) show_help ;;
	-*venv) dst="$1"; shift ;;

	apply)
	    pushd "$dst" >/dev/null || { echo "pushd $dst failed"; exit 1; }
	    for fyl in "${fyls[@]}";
	    do
		path="${fyl%/*}"

		# Conditional install, jenkins may not support interpreter yet.
		if [ ! -e "$path" ]; then
		    echo "[SKIP] $path"
		    continue
		fi
		
		echo "[APPLY] $path"
		patch -R -p1 < "../$pat/${path}/patch"
	    done
	    popd >/dev/null || { echo "popd $dst failed"; exit 1; }
	    ;;

	backup)
	    mkdir ~/backups
	    pushd "$src" || { echo "pushd $dst failed"; exit 1; }
	    tar czvf ~/backups/vault."$(date '+%Y%m%d%H%M%S')" "${fyls[@]}"
	    popd || { echo "popd $dst failed"; exit 1; }
	    ;;

	gather)
	    for fyl in "${fyls[@]}";
	    do
		patchDir="$pat/$fyl"
		mkdir -p "$patchDir"
		diff -Naur "$src/$fyl" "$dst/$fyl" | tee "$pat/$fyl/patch"
	    done
	    find "$pat" -print
	    ;;

	help) show_help ;;

	*)
	    echo "ERROR: Unknown action [$opt]"
	    exit 1
	    ;;
    esac

    echo
done

# [EOF]
