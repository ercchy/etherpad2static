#!/bin/bash

COUNTER=0
while read line
do
    name=$line
    let COUNTER=COUNTER+1
    echo "$COUNTER. Padname: $name is removing"
    rm $name.html
    echo "done with $name file"
    sleep 1
done < $1