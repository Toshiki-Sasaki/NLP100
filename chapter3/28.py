#!usr/bin/env python
# -*- coding:utf-8

import re
import json
from collections import OrderedDict

input = "jawiki-england.txt"
output = "jawiki-remove-allmarkups.json"

f = open(input, "r")
o = open(output, "w")

start = re.compile(r"\{\{基礎情報(.+)")
end = re.compile(r"\}\}")
con = re.compile(r"\|(.+)\s+=\s+(.+)")
rm = re.compile(r".*\[{2}(.+)\]{2}.*")
rm2 = re.compile(r"(\{{2}|\[{2}|\||#|\]{2}|\}{2}|<.+>)")
infodict = OrderedDict()

m = False
for line in f:
    if re.match(start, line):
        m = True
    elif re.match(end, line):
        m = False
    line2 = re.sub(r"'+", "", line)
    n = re.match(con, line2)
    if m and n:
        l = re.match(rm, n.group(2))
        if l:
            value = re.sub(rm2, "", n.group(2))
            infodict[n.group(1)] = value
        else:
            infodict[n.group(1)] = re.sub(rm2, "", n.group(2))
        
json.dump(infodict, o, ensure_ascii=False)

o.close()
f.close()