# Howto create a python 3.10+ patch

1) Checkout voltha-docs
2) cd voltha-docs
3) Create a virtual environment:
   - make venv (default python version)
   - make venv-activate-patched (for python v3.10+)
4) make patch-init
5) modify the file to be patched beneath staging/${relative_path_to_patch}
6) make patch-create PATCH_PATH=${relative_path_to_patch}
    o This will create patches/${relative_path_to_patch}/patch
    o make patch-create PATCH_PATH=lib/python3.10/site-packages/sphinx/util/typing.py
      lib/python3.10/site-packages/sphinx/util/typing/patch
7) Verify
    o make sterile
    o make venv
8) Validate
    o make lint
    o make test

# [EOF]
