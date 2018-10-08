#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( dirname "$SCRIPT_DIR" )"

python3 -m unittest discover -v  $BASE_DIR/unit_tests/test_data_structures  -p "test_*.py"
# python3 -m unittest discover -v  $BASE_DIR/unit_tests/test_data_provider_simple  -p "test_*.py"
# python3 -m unittest discover -v  $BASE_DIR/unit_tests/decimal  -p "test_*.py"
