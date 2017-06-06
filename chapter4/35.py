#!usr/bin/env python3
# -*- coding:utf-8 -*-

import p30
import json

def extractNounJunc(INPUT):
    w = []
    for morpheme in INPUT:
        for i in morpheme:
            if i['surface'] == '名詞':
                w.append(i['surface'])
    return d

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'results/neko_35.json'
    d = p30.getMorphemeDict(INPUT)
    D = extractNounJunc(d)
    print(len(D))
    print(D[0:10])
    o = open(OUTPUT, 'w')
    json.dump(D, o, ensure_ascii=False)
