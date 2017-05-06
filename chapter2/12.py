#!usr/bin/env python
# -*- coding:utf-8 -*-

def extractColumn(f):
    f1 = open(txt1, "w")
    f2 = open(txt2, "w")
    for line in f:
        col = line.split("\t")
        f1.write(col[0] + "\n")
        f2.write(col[1] + "\n")
    f1.close()
    f2.close()

txt = "hightemp.txt"
txt1 = "col1.txt"
txt2 = "col2.txt"

with open(txt, "r") as f:
    extractColumn(f)
    f.close()

# cut -f 1 hightemp.txt > col1_cut.txt
# cut -f 2 hightemp.txt > col2_cut.txt