# -*- makefile -*-
## -----------------------------------------------------------------------
## Intent: Targets in this makefile will determine if locally modified
##   files exist in the sandbox.  VOLTHA currently uses this logic to
##   detect when go {tidy, update} have indirectly modified vendor go.mod
##   files during a build or test.
## -----------------------------------------------------------------------

$(error DISABLED -- not yet deployed/in use)

# $(MAKE) --no-print-directory detect-local-edits

## ---------------------------------------------------------------------
## Intent: Determine if sandbox contains locally modified files
## ---------------------------------------------------------------------
clean-tree := git status --porcelain
detect-local-edits:
	$(HIDE)[[ `$(clean-tree)` == "" ]] || {\
  echo "ERROR: Untracked files detected, commit or remove to continue" \
  && echo "`git status`" \
  && exit 1; }

# [EOF]
