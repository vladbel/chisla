#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( dirname "$SCRIPT_DIR" )"

# clear the screen
printf "\033c"

echo ""
echo "START TESTS"
echo "*******************************************************************"
echo " Run data structure tests"

python3 -m unittest discover $BASE_DIR/unit_tests/test_data_structures  -p "test_*.py"

echo ""
echo "*******************************************************************"
echo " Run data provider tests"

python3 -m unittest discover $BASE_DIR/unit_tests/test_data_provider_simple  -p "test_*.py"

echo ""
echo "*******************************************************************"
echo " Run decimal"

python3 -m unittest discover $BASE_DIR/unit_tests/decimal  -p "test_*.py"

echo ""
echo "*******************************************************************"
echo " Run environment"

python3 -m unittest discover $BASE_DIR/unit_tests/test_environment  -p "test_*.py"
