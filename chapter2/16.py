#!usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def print_lines_Nsplit(N):
    f = open(txt, "r")
    i = 1
    for line in (f.readlines()):
        if i!=N:
            print(line.rstrip("\n"))
            i += 1
        else:
            print(line)
            i = 1
        
txt = "hightemp.txt"
N = int(sys.argv[1])
print_lines_Nsplit(N)

# split -l 3 hightemp.txt 
# xaa, xab, ..., というファイルで複数個作成される