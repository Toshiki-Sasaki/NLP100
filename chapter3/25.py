#!usr/bin/env python
# -*- coding:utf-8

import re
import json
from collections import OrderedDict

input = "jawiki-england.txt"
#output = "jawiki-england-basicinfo.txt"
output = "jawiki-england-basicinfo.json"

f = open(input, "r")
o = open(output, "w")

 
start = re.compile(r"\{\{基礎情報(.+)")
end = re.compile(r"\}\}")
con = re.compile(r"\|(.+)\s+=\s+(.+)")
infodict = OrderedDict()

m = False
for line in f:
    if re.match(start, line):
        m = True
    elif re.match(end, line):
        m = False
    n = re.match(con, line)
    if m and n:
        infodict[n.group(1)] = n.group(2)
json.dump(infodict, o, ensure_ascii=False)

o.close()
f.close()