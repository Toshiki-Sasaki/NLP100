#!usr/bin/env python3
# -*- coding:utf-8 -*-

import p30
import json

def extractNounJunc(INPUT):
    W = []
    for morpheme in INPUT:
        w = []
        for i in morpheme:
            if i['pos'] == '名詞':
                w.append(i['surface'])
            else:
                if len(w) > 1:
                    W.append(''.join(w)) #長さが2以上なら連接なのでappend
                w = [] #名詞以外がきたら初期化
    return W

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'results/neko_35.json'
    d = p30.getMorphemeDict(INPUT)
    D = extractNounJunc(d)
    print(len(D))
    print(D[0:10])
    o = open(OUTPUT, 'w')
    json.dump(D, o, ensure_ascii=False)
