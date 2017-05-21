#!usr/bin/env python
# -*- coding:utf-8

import re

input = "jawiki-england.txt"
output = "jawiki-england-sections.txt"

f = open(input, "r")
o = open(output, "w")

# 空白を含む表記も会うので \s を使用
prog = re.compile(r"^(==+)\s*(.+?)\s*(==+)")

for line in f:
    m = re.match(prog, line)
    if m:
        o.write(str(m.group(2)) + ", " + str(len(m.group(1))-1) + "\n")

o.close()
f.close()