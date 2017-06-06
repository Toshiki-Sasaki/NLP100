#!usr/bin/env python3
# -*- coding:utf-8 -*-

import p30
import json
from collections import defaultdict #出現頻度は求められるが、ソートする必要がある
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn

def getFrequency(INPUT):
    morphemeDict = defaultdict(int)
    m = []
    for morpheme in INPUT:
        for i in morpheme:
            morphemeDict[i['surface']] += 1
    for k, v in sorted(morphemeDict.items(), key=lambda x: x[1], reverse=True):
        m.append(", ".join([k, str(v)]))
    return m

def genBar(D):
    label = []
    freq = []
    for i in D:
        d = i.split(',')
        label.append(d[0])
        freq.append(int(d[1]))
    x = np.arange(0,len(freq))
    mpl.rcParams['font.family'] = 'AppleGothic'
    plt.bar(x, freq, tick_label=label, align="center")
    plt.tick_params(labelsize=15)
    plt.show()

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'results/neko_36.json'
    d = p30.getMorphemeDict(INPUT)
    D = getFrequency(d)
    genBar(D[0:10])
    o = open(OUTPUT, 'w')
    json.dump(D, o, ensure_ascii=False)
