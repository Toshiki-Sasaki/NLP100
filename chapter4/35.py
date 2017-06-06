#!usr/bin/env python3
# -*- coding:utf-8 -*-

import p30
import json

def extractVerbs(INPUT):
    d = []
    # naiveな方法なので無駄があるコード
    for morpheme in INPUT:
        for i in range(len(morpheme)-2):
            data =  morpheme[i:i+3]
            m1 = morpheme[i]['pos'] == '名詞'
            m2 = morpheme[i+1]['surface'] == 'の'
            m3 = morpheme[i+2]['pos'] == '名詞'
            if m1 and m2 and m3:
                d.append(''.join([i['surface'] for i in data]))
    return d

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'results/neko_35.json'
    d = p30.getMorphemeDict(INPUT)
    D = extractVerbs(d)
    print(len(D))
    print(D[0:10])
    o = open(OUTPUT, 'w')
    json.dump(D, o, ensure_ascii=False)
