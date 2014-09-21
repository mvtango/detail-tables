#! /bin/bash

HERE=`dirname $0`
cd $HERE
wget 'https://docs.google.com/spreadsheets/d/1VJ081DmWmYpSZhpVo9eWitn8OZ_m9cStFGOLR1CZKnw/export?format=csv&gid=509646809&single=true' --quiet --output-document=data.csv
python insert.py data.csv
datafreeze freeze.yaml
ls -l data.csv data.db export/index.json

