#! /usr/bin/env bash

rm -rf env
virtualenv env
source env/bin/activate
if [[ $? -ne 0 ]] ; then
    exit 1
fi
pip install -r requirements.txt
