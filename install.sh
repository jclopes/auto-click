#! /usr/bin/env bash

ENV=env

rm -rf ${ENV}
virtualenv -p python3 ${ENV}
source ${ENV}/bin/activate
if [[ $? -ne 0 ]] ; then
    exit 1
fi
pip install -r requirements.txt
