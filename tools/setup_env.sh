#!/bin/bash

virtualenv -p python3 .
./bin/pip install pbr
./bin/pip install -r requirements.txt
./bin/pip install -U .

