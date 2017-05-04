#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

def _cipher_mine(sen):
    word = ""
    for i in range(len(sen)):
        if re.match(r'[a-z]', sen[i]):
            word += chr(219 - ord(sen[i]))
        else:
            word += sen[i]
            pass
    return word

def _cipher_python(sen):
    word = ""
    for char in sen:
        word += chr(219-ord(char)) if char.islower() else char
    return word

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine."
print(_cipher_mine(sentence))
print(_cipher_python(sentence))
