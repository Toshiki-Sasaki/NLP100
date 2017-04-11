# -*- coding:utf-8 -*-
import re

def ngram(sentence, n):
    alpha = re.split('\W+', sentence)
    # word n-gram
    wordN = [alpha[i:i+n] for i in range(len(alpha)-(n-1))]
    # alphabet n-gram
    alphaN = [''.join(alpha)[i:i+n] for i in range(len(''.join(alpha))-(n-1))]
    return wordN, alphaN

sentence = 'I am an NLPer'
n=2

wordN, alphaN = ngram(sentence, n)
print(wordN)
print(alphaN)

'''
>>> [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
>>> ['Ia', 'am', 'ma', 'an', 'nN', 'NL', 'LP', 'Pe', 'er']
'''
