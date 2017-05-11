#!usr/bin/env python
# -*- coding:utf-8

import re

input = "jawiki-engrand.txt"
output = "jawiki-engrand-mediafiles.txt"

f = open(input, "r")
o = open(output, "w")

# 
prog = re.compile(r"\[*(file|File|ファイル|Media)\:(.+?)\|+")

for line in f:
    m = re.match(prog, line)
    if m:
        o.write(m.group(2) + "\n")

o.close()
f.close()