# -*- coding:utf-8 -*-
import re

def word_ngram(sentence, n):
    # word n-gram
    alpha = re.split('\W+', sentence)
    wordN = [alpha[i:i+n] for i in range(len(alpha)-(n-1))]
    print(wordN)

def alpha_ngram(sentence, n):
    # alphabet n-gram
    alpha = re.split('\W+', sentence)
    alphaN = [''.join(alpha)[i:i+n] for i in range(len(''.join(alpha))-(n-1))]
    print(alphaN)

sentence = 'I am an NLPer'
n=2

word_ngram(sentence, n)
alpha_ngram(sentence, n)

'''
>>> [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
>>> ['Ia', 'am', 'ma', 'an', 'nN', 'NL', 'LP', 'Pe', 'er']
'''

# python には ngram というライブラリがあるので，それを使えば楽．