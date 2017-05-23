#!usr/bin/env python
# -*- coding:utf-8

import re
import json
from collections import OrderedDict

input = "jawiki-england.txt"
output = "jawiki-remove-markup.json"

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
    # 25と違うのはここの一文 ('の繰り返しを削除)
    line2 = re.sub(r"'+", "", line)
    n = re.match(con, line2)
    if m and n:
        infodict[n.group(1)] = n.group(2)
json.dump(infodict, o, ensure_ascii=False)

o.close()
f.close()