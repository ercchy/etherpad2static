#!/bin/bash

FILES=*

for f in $FILES
do
   filename="${f##*/}"
   base="${filename%.[^.]*}"
   echo "Processing $f file..."
   ln -s $f ${f%%.*}
  # take action on each file. $f store current file name
  #cat $f
done