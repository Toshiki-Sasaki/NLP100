#!usr/bin/env python3
# -*- coding:utf-8 -*-

import p30
import json
from collections import defaultdict #出現頻度は求められるが、ソートする必要がある
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns

def getFrequency(INPUT):
    morphemeDict = defaultdict(int)
    m = []
    for morpheme in INPUT:
        for i in morpheme:
            morphemeDict[i['surface']] += 1
    for k, v in sorted(morphemeDict.items(), key=lambda x: x[1], reverse=True):
        m.append(", ".join([k, str(v)]))
    return m

def zipf(D):
    freq = []
    for i in D:
        d = i.split(',')
        freq.append(int(d[1]))
    rank = np.arange(1,len(freq)+1)
    mpl.rcParams['font.family'] = 'AppleGothic'
    plt.xlabel('出現頻度順位')
    plt.ylabel('出現頻度')
    plt.xscale('log')
    plt.yscale('log')
    sns.set_palette('brightgit s')
    plt.scatter(rank, freq, s=15)
    plt.show()

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'results/neko_36.json'
    d = p30.getMorphemeDict(INPUT)
    D = getFrequency(d)
    zipf(D)
