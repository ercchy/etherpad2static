#!/bin/bash


FILES=dddd.html

CONTENT="<!doctype html><html lang="en"><head><title>dddd</title><meta charset="utf-8"><style> * { font-family: arial, sans-serif;font-size: 13px;line-height: 17px; }ul.indent { list-style-type: none; }ol { list-style-type: decimal; }ol ol { list-style-type: lower-latin; }ol ol ol { list-style-type: lower-roman; }ol ol ol ol { list-style-type: decimal; }ol ol ol ol ol { list-style-type: lower-latin; }ol ol ol ol ol ol{ list-style-type: lower-roman; }ol ol ol ol ol ol ol { list-style-type: decimal; }ol  ol ol ol ol ol ol ol{ list-style-type: lower-latin; }</style></head><body>This text pad is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents!<br><br>Thanks for working together with your peers!<br><br></body></html>
"

for f in $FILES
do
    value=`cat $f`;

    #echo "Processing $f file..."
    #echo $value

    if [ $CONTENT == $value ]; then
       echo "same";
    else
        echo "not same"
    fi

done