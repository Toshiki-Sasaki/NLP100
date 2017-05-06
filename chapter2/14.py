#!usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def print_head_Nlines(N):
    f = open(txt, "r")
    for _ in range(N):
        print(f.readline().rstrip("\n"))

txt = "hightemp.txt"
N = int(sys.argv[1])
print_head_Nlines(N)


# head -n N hightemp.txt
