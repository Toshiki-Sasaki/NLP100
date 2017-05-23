#!usr/bin/env python
# -*- coding:utf-8

import re
import json
import requests

input = "jawiki-remove-allmarkups.json"

with open(input, "r") as f:
    doc = json.load(f)

wikipedia_api = "http://ja.wikipedia.org/w/api.php?"
prop = {
    'action': "query",
    'titles': "Image:",
    'prop': "imageinfo",
    'iiprop': "url",
    'format': "json",
    'formatversion': '2',
    'utf8': '',
    'continue': ''
}

for line in doc:
    if "国旗画像" in line:
        filename = doc['国旗画像']
        prop['titles'] = "Image:" + filename
        res = requests.get(url=wikipedia_api, params=prop)
        datum = json.loads(res.text)
        try:
            file_url = datum['query']['pages'][0]['imageinfo'][0]['url']
        except Exception:
            print(datum)
            break
        print(filename, file_url)

f.close()

# output
# Flag of the United Kingdom.svg https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg
