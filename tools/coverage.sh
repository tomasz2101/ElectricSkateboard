#!/bin/bash


mkdir -p build
rm -f build/unit_test_coverage.xml
rm -f build/coverage_html

coverage run .pybuild/bin/pytest
coverage report --omit=/usr/local/lib/python3.6/* > build/unit_test_coverage.xml
coverage html -d build/coverage_html --omit=/usr/local/lib/python3.6/*

if [ "$1" == "open" ];
    then
        open build/coverage_html/index.html
fi
