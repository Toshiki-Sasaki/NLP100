#!usr/bin/env python3
# -*- coding:utf-8 -*-

import p30
import json
from collections import defaultdict #出現頻度は求められるが、ソートする必要がある
#from collections import Counter #出現頻度の多い順とかにするならやっぱCounterが便利そう?
#collectionsに関しては19番参考

def extractNounJunc(INPUT):
    morphemeDict = defaultdict(int)
    m = []
    for morpheme in INPUT:
        for i in morpheme:
            morphemeDict[i['surface']] += 1
    for k, v in sorted(morphemeDict.items(), key=lambda x: x[1], reverse=True):
        m.append(", ".join([k, str(v)]))
    return m

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'results/neko_36.json'
    d = p30.getMorphemeDict(INPUT)
    D = extractNounJunc(d)
    print(len(D))
    print(D[0:10])
    o = open(OUTPUT, 'w')
    json.dump(D, o, ensure_ascii=False)
