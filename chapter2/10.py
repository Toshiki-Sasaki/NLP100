#!usr/bin/env python
# -*- coding:utf-8 -*-

def _get_txtlength_mine(txt):
    f = open(txt, "r")
    return len(f.readlines())

txt = 'hightemp.txt'
print(_get_txtlength_mine(txt))

# wc -l hightemp.txt
