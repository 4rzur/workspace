#!/bin/bash

contador=1

while read line;do
    echo "Línea $contador: $line"
    let contador+=1
done < /etc/passwd

# by WOPR
