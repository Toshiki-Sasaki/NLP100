#!usr/bin/env python 
# -*- coding:utf-8

import re 

input = "jawiki-england.txt"
output = "jawiki-england-category-names.txt"

f = open(input, "r")
o = open(output, "w")

prog = re.compile(r"\[\[Category:(.+)\]\]")

# 正規表現の変数展開はできないみたい
# prog = re.compile(r".%s." %( "[[Category:(.+)]]" ))

for line in f:
    m = re.match(prog, line)
    if m:
        o.write(m.group(1) + "\n")

o.close()
f.close()