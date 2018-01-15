#!/bin/bash
i=0
while [ $i -lt 40000 ]; do
python3 bike.py
#python3 library.py
sleep 30
i=$((i + 1))
#echo $i
done
