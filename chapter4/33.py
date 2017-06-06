#!usr/bin/env python3
# -*- coding:utf-8 -*-

import p30
import json

def extractAofB(INPUT):
    D = []
    j=0
    for morpheme in INPUT:
        for i in morpheme:
            if i['pos1'] == 'サ変接続':
                D.append(i['surface'])
    return D

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'results/neko_33.json'
    d = p30.getMorphemeDict(INPUT)
    D = extractAofB(d)
    #print(len(D))
    #print(D[0:10])
    o = open(OUTPUT, 'w')
    json.dump(D, o, ensure_ascii=False)
