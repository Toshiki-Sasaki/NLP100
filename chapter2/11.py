#!usr/bin/env python
# -*- coding:utf-8 -*-

def tab2space(f):
    for line in f:
        print(line.expandtabs())

txt = 'hightemp.txt'
with open(txt, "r") as f:
    tab2space(f)
    
# $ sed -e s/$'\t'/" "/g hightemp.txt
# $ cat hightemp.txt | tr "\t" " "
# $ expand -t 1 hightemp.txt