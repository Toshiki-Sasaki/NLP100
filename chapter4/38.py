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

def genHist(D):
    freq = []
    for i in D:
        d = i.split(',')
        freq.append(int(d[1]))
    mpl.rcParams['font.family'] = 'AppleGothic'
    plt.xlabel('出現頻度')
    plt.ylabel('単語の種類数')
    plt.hist(freq, bins=40, range=(0,40))
    plt.show()

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'results/neko_36.json'
    d = p30.getMorphemeDict(INPUT)
    D = getFrequency(d)
    genHist(D)
