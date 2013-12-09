#!/bin/bash

COUNTER=0
while read line
do
    name=$line
    let COUNTER=COUNTER+1
    echo "$COUNTER. Padname: $name is getting a link"
    ln -s p/$name.html $name
    echo "done with $name file"
    sleep 1
done < $1