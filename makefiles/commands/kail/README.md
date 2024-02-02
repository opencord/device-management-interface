# -----------------------------------------------------------------------
# Workaround for godownloader disappearing:
#   This is a complete hack to get bbsim and v-s-t functional again.
#   A more permanent answer is needed, copy binaries into a *tool* repo
#   and use directly from git clone w/o access or install overhead.
# ----------------------------------------------------------------------

1) Retrieve an archived copy of the script and place in v-s-t/etc.
   https://searchcode.com/file/316605398/godownloader.sh
2) A few script edits are needed:
     o change download method from curl to wget.
     o VERSION= variable requires a 'v' prefix.
3) Update Makefile to install the new command.

# [EOF]
