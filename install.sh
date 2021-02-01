#! /usr/bin/env bash

python3 -m venv env
if [[ $? -ne 0 ]] ; then
	echo "Failed to run python3"
    exit 1
fi
./env/bin/pip install -r requirements.txt
