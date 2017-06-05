#!usr/bin/env python3
# -*- coding:utf-8 -*-

#import sys
import MeCab

def getParse(INPUT, OUTPUT):
    f = open(INPUT, 'r')
    o = open(OUTPUT, 'w')
    o.write(m.parse(f.read()))
    f.close()
    o.close()

if __name__ == '__main__':
    #m = MeCab.Tagger('-Ochasen')
    m = MeCab.Tagger('mecabrc')
    INPUT = 'neko.txt'
    OUTPUT = 'neko.txt.mecab'
    getParse(INPUT, OUTPUT)
