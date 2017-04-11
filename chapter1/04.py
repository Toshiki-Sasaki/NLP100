# -*- coding:utf-8 -*-
import re

def generateDictionary(sentence, nums):
    atomDict = {}
    for i, j in enumerate([str for str in re.split('\W+', sentence) if not str=='']):
        atom = j[0] if i+1 in nums else j[0:2]
        atomDict[atom] = i+1
    return atomDict

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
nums = [1, 5, 6, 7, 8, 9, 15, 16, 19]

print(generateDictionary(sentence, nums))
'''
>>> {'P': 15, 'K': 19, 'B': 5, 'He': 2, 'Si': 14, 'N': 7, 'Na': 11, 'Mi': 12, 'H': 1, 'Be': 4, 'Ne': 10, 'Al': 13, 'S': 16, 'O': 8, 'Li': 3, 'Cl': 17, 'Ca': 20, 'F': 9, 'C': 6, 'Ar': 18}
'''
