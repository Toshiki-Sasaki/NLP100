#!usr/bin/env python
# -*- coding:utf-8 -*-

def count_frequency():
    from collections import Counter
    f = open(txt, "r")
    lines = [line.split("\t")[0] for line in f.readlines()]

    for i in Counter(lines).most_common():
        print(" ".join([i[0], str(i[1])]))


def count_frequency_ver_defaultdict():
    from collections import defaultdict
    f = open(txt, "r")
    prefectures = defaultdict(int)
    
    line = f.readline()
    while line:
        prefectures[line.split("\t")[0]] += 1
        line = f.readline()
    for k, v in sorted(prefectures.items(), key=lambda x: x[1], reverse=True):
        print(" ".join([k, str(v)]))
    

txt = "hightemp.txt"
count_frequency()

print("-------------------------------")
count_frequency_ver_defaultdict()


#  $ cut -f1 hightemp.txt | sort | uniq -c | sort -r