#! /bin/bash

HERE=`dirname $0`
cd $HERE
python insert.py
datafreeze freeze.yaml

