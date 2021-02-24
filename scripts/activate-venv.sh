#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( dirname "$SCRIPT_DIR" )"

source ${BASE_DIR}/chisla_env/bin/activate

# Don't need export PYTHONPATH.
# This shall be handled by `chisla_env/lib/path.pth`
# export PYTHONPATH=${PYTHONPATH}:${BASE_DIR}/source:${BASE_DIR}/unit_tests