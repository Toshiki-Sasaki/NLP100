#!usr/bin/env python3
# -*- coding:utf-8 -*-

import codecs
import json

def getMorphemeDict(INPUT):
    f = open(INPUT, 'r')
    o = open(OUTPUT, 'w')
    tmpArray = []
    dictArray = []
    for line in f:
        data = line.rstrip().split('\t')
        try:
            feature = data[1].split(',')
        except IndexError:
            print("EOS")
        morphemeDict = {'surface':data[0], 'base':feature[6], 'pos':feature[0], 'pos1':feature[1]}
        tmpArray.append(morphemeDict)
        if feature[1] == '句点':
            dictArray.append(tmpArray)
            tmpArray = []
    json.dump(dictArray, o, ensure_ascii=False)
    f.close()
    o.close()
    return dictArray

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    OUTPUT = 'neko_30.json'
    #OUTPUT = 'neko_30.txt'
    d = getMorphemeDict(INPUT)
