#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( dirname "$SCRIPT_DIR" )"

python3 -m unittest discover -v  $BASE_DIR/unit_tests/  -p "*.py"
python3 -m unittest discover -v  $BASE_DIR/unit_tests/blank  -p "*.py"
