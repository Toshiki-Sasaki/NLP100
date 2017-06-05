#!usr/bin/env python3
# -*- coding:utf-8 -*-

import p30
import json

def extractVerbs(INPUT):
    D = []
    for morpheme in INPUT:
        for i in morpheme:
            if i['pos'] == '動詞':
                D.append(i['surface'])
    return D

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'neko_31.json'
    d = p30.getMorphemeDict(INPUT)
    D = extractVerbs(d)
    #o = open(OUTPUT, 'w')
    #json.dump(D, o, ensure_ascii=False)
