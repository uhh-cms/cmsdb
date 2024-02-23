#!/usr/bin/env bash
SCRIPT_DIR=$( cd -- "$( dirname -- "$0" )" &> /dev/null && pwd )
# Script that runs coverage tests.

# loop through all modules if no input arguments are given
for mod in ${@}; do
    echo "testing ${mod} ..."
    TESTMODULE=${mod} python -m unittest ${SCRIPT_DIR}/test_campaigns.py
done
