#!/bin/bash

COUNTER=0
while read line
do
    name=$line
    let COUNTER=COUNTER+1
    echo "$COUNTER. filename: $name (http://pad.p2pu.org/p/$name/export/html)"
    wget -O $name.html -P ~/erika/DEV/p2pu/etherpad2static/etherpad_static_files http://pad.p2pu.org/p/$name/export/html
    echo "done with $name file"
    sleep 1
done < $1