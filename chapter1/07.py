#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string

def _makeString_mine(x, y, z):
    return str(x)+"時の"+str(y)+"は"+str(z)

def _makeString_python(x, y, z):
    s = string.Template("$x時の$yは$z")
    return s.substitute(x=x, y=y, z=z) #ここの書き方が特徴的

x = 12
y = "気温"
z = 22.4

print(_makeString_mine(x, y, z))
print(_makeString_python(x, y, z))
