#!usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def print_set_of_prefecture():
    f = open(txt, "r")
    prefectures = [line.split("\t")[0] for line in f.readlines()]
    print(set(prefectures))
        
def print_set_of_prefecture_python():
    f = open(txt, "r")
    prefectures = set()
    for line in f:
        prefectures.add(line.split("\t")[0])
    print(prefectures)

txt = "hightemp.txt"
print_set_of_prefecture()
print_set_of_prefecture_python()

# 順不同
# {'愛媛県', '静岡県', '千葉県', '山形県', '和歌山県', '高知県', '埼玉県', '山梨県', '愛知県', '大阪府', '群馬県', '岐阜県'}

# cut -f1 hightemp.txt | sort | uniq