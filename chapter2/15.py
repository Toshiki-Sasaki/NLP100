#!usr/bin/env python
# -*- coding:utf-8 -*-
import sys

# 最終行を先頭にしてNこ
def print_tail_Nlines_reversed(N):
    f = open(txt, "r")
    for line in reversed(f.readlines()):
        if N > 0: 
            print(line.rstrip("\n"))
            N -= 1

# 最終行を最後にしてNこ
def print_head_Nlines(N):
    f = open(txt, "r")
    line = f.readlines()
    for i in reversed(range(N)):
        print(line[len(line)-1-i].rstrip("\n"))

txt = "hightemp.txt"
N = int(sys.argv[1])
print_tail_Nlines_reversed(N)
print("--------------------------")
print_head_Nlines(N)


# tail -n N hightemp.txt
