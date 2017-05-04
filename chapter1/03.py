#-*- coding:utf-8 -*-

import math
import re

def _get_InitialLength_mine(sentence):
    return [len(str) for str in re.split('\W+', sentence) if not str=='']

sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

print(_get_InitialLength_mine(sentence))
print(math.pi)

'''
>>> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
>>> 3.141592653589793
'''
