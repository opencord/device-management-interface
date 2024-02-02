# Migration support for python 3.10+

## Intent

Applications of patches will enable local use of newer python versions
available with a recent OS install or package manager installation.
Makefile targets will fail out of the box w/o modifying collection imports.

Create new patches as needed to help testing along.
Eventually this hierarchy can be dismantled once the latest interpreter
is generally in use.

## patches/

This directory contains patch files that can be directly applied to sources
in the python virtualenv directory.  Patches are created to support use of
three python version variants for the robot ramework:
    python 2x       (deprecated)
    python >= 3.10  (collections.abc required)
    python < 3.10   (collections.abc optional)


# .venv/

Makefile will first create a python virtualenv directory to selectively
use packages.  After setup patches are applied to venv (as a transition)
to fully enable support for local interpreter use for newer OS installs.


# staging/

The staging directory is used for comparison with the .venv directory
to generate patches.  Populate the directory with a copy of a cleanly
patched virtual interpreter then modify files benath/ staging to generate
a patch from.

% make sterile
% make venv
% mkdir staging
% rsync -rv --checksum .venv/. staging/.
[NOTE] Make python 3.10+ migration edits beneath staging as needed
% make patch-gather
% make sterile
% make lint


# makefile targets

make patch-gather:
   * gather a list of potential sources to edit.

make patch-apply:
   * Gather a list of patch files.
   * Apply each in turn to sources in the virtualenv directory.

make patch-create:
   * make patch-create VENV_NAME="venv_docs" PATCH_PATH="lib/python3.10/site-packages/sphinx/util/typing.py"
   * make sterile
   * make help     # reinstall virtualenv and verify help target

# Verify installation
   * make lint -or- make test

# [EOF]