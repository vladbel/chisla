#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( dirname "$SCRIPT_DIR" )"
HORIZONTAL_LINE="_____________________________  END  ____________________________\n"

# clear the screen
printf "\033c"

echo "START TESTS"
echo " Run data structure tests"

python3 -m unittest discover $BASE_DIR/unit_tests/test_data_structures  -p "test_*.py"

echo ""
echo -e $HORIZONTAL_LINE
echo " Run data provider tests"

python3 -m unittest discover $BASE_DIR/unit_tests/test_data_provider_simple  -p "test_*.py"

echo -e $HORIZONTAL_LINE
echo " Run decimal"

python3 -m unittest discover $BASE_DIR/unit_tests/decimal  -p "test_*.py"

echo -e $HORIZONTAL_LINE
echo " Run environment"

python3 -m unittest discover $BASE_DIR/unit_tests/test_environment  -p "test_*.py"
