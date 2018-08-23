#!/bin/bash

PY=python
BIN=./genPowerCouplesFiles.py

for row in 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000 ;
do
    for col in 100 200 300 400 500 ;
    do
        $PY $BIN -r $row -c $col -o input_${row}x${col}.csv
    done
done
