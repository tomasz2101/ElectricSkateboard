#!/bin/bash

set -x
set -e

outputname=$1

# This script assumes it is run from the git root, meaning the had_config
# directory exists in the current working directory.

mkdir -p build
rm -f build/unit_test_ln_had_ci_scripts.xml

echo "Setting up python environment..."
virtualenv -p python3 .pybuild
. .pybuild/bin/activate
.pybuild/bin/pip install pbr
.pybuild/bin/pip install -r requirements.txt
.pybuild/bin/pip install -e .

echo "Running tests..."run_update_status.sh

. .pybuild/bin/activate
.pybuild/bin/pytest --pep8 \
                    --cov-report=term \
                    --cov-report=xml:build/test.xml \
                    --cov-report=html:build/test \
                    --junit-xml=${outputname} \
                    --ignore=pybuild \
                    --flakes

