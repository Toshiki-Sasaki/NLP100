#!usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def sort_templature():
    f = open(txt, "r")
    lines = [line.split("\t") for line in f.readlines()]
    sortedList = sorted(lines, key=lambda x: x[2])
    
    for line in sortedList:
        print(" ".join(line).rstrip("\n"))
        
txt = "hightemp.txt"
sort_templature()


# どちらでも
# sort -k3n hightemp.txt 
# sort -k3 hightemp.txt 
