#!usr/bin/env python
# -*- coding:utf-8 -*-

def mergeFile(txt1, txt2):
    f1 = open(txt1, "r")
    line1 = f1.readlines()
    f2 = open(txt2, "r")
    line2 = f2.readlines()
    
    f3 = open(txt3, "w")
    for (col1, col2) in zip(line1, line2):
         f3.write(col1.rstrip("\n") + "\t" + col2)
    
    f1.close()
    f2.close()
    f3.close()

txt1 = "col1.txt"
txt2 = "col2.txt"
txt3 = "output_of_13.txt"

mergeFile(txt1, txt2)

# paste col1.txt col2.txt > output_of_13_paste.txt
