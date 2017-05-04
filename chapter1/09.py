#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import random

def _typoglycemia_mine(sen):
    word = sen.split()
    text = []
    for i in word:
        if len(i) >= 5:
            typo = list(i[1:-1])
            rdtext = random.sample(typo, len(typo))
            text.append(i[0] + "".join(rdtext) + i[-1])
        else:
            text.append(i)
    return " ".join(text)

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(_typoglycemia_mine(sentence))

"""
I c'lnodut beelvie that I cloud alutalcy uarnesndtd what I was rdnieag : the pnmnoaehel pewor of the hmuan mind .
"""
aa
