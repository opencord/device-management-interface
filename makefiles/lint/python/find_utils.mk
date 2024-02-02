# -*- makefile -*-
# -----------------------------------------------------------------------
# Intent:
#   o Construct a find command able to gather python files with filtering.
#   o Used by library makefiles flake8.mk and pylint.mk for iteration.
# -----------------------------------------------------------------------

## -----------------------------------------------------------------------
## Intent: Construct a string for invoking find \( excl-pattern \) -prune
# -----------------------------------------------------------------------
gen-python-find-excl = \
  $(strip \
	-name '__ignored__' \
	$(foreach dir,$($(1)),-o -name $(dir)) \
  )

## -----------------------------------------------------------------------
## Intent: Construct a find command to gather a list of python files
##         with exclusions.
## -----------------------------------------------------------------------
## Usage:
#	$(activate) & $(call gen-python-find-cmd) | $(args-n1) pylint
## -----------------------------------------------------------------------
gen-python-find-cmd = \
  $(strip \
    find . \
      \( $(call gen-python-find-excl,onf-excl-dirs) \) -prune \
      -o -name '*.py' \
      -print0 \
  )

# [EOF]
