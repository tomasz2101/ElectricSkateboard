#!/bin/bash

pip install pbr
pip install -r /src/requirements.txt
pip install -e /src/ 
cd /web-root
/src/scripts/makehistory.py -p /web-root/pipeline_names.txt

