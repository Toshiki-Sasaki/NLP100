#!usr/bin/env python 
# -*- coding:utf-8

import re 
import json

input = "jawiki-country.json/jawiki-country.json"
output = "jawiki-england.txt"

f = open(input, "r")
o = open(output, "w")

for line in f:
    doc = json.loads(line)

    if re.search(u"イギリス", doc[u"title"]):
        o.write(doc[u"text"])
o.close()
f.close()