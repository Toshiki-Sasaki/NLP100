#!usr/bin/env python3
# -*- coding:utf-8 -*-

import codecs

def getMorphemeDict(INPUT):
    f = open(INPUT, 'r')
    tmpArray = []
    dictArray = []
    for line in f:
        data = line.rstrip().split('\t')
        # EOF(End of file)以外を実行
        try:
            feature = data[1].split(',')
        except IndexError:
            print("EOS")
        morphemeDict = {'surface':data[0], 'base':feature[6], 'pos':feature[0], 'pos1':feature[1]}
        tmpArray.append(morphemeDict)
        # 文の最後であれば、文をリストとして表現。
        if feature[1] == '句点':
            dictArray.append(tmpArray)
            tmpArray = []
    f.close()
    return dictArray

if __name__ == '__main__':
    INPUT = 'neko.txt.mecab'
    #OUTPUT = 'neko_30.txt'
    d = getMorphemeDict(INPUT)
