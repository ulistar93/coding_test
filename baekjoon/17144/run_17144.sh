#!/bin/bash

#python3 ./17144_dust.py ./17144_input1.txt ./17144_ans1.txt
for i in $@
do
  python3 ./17144_dust.py ./17144_input$i.txt ./17144_ans$i.txt
done
