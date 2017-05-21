#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import re
import json


def pass_through(string):
    return string


def fundamental_extractor(file, func):
    """
    input: file obj, func for remove markups
    output: array of dicts, each dict is fundamental info of a country.
    """

    fundamentals = []
    fundamental = {}
    begin = re.compile(r"\{\{基礎情報 国")
    end = re.compile(r"\}\}")
    row = re.compile(r"^\s?\|?\s?(.+?)\s?=(.*)\|?")
    inside_flg = False

    prev_key = None
    for line in file:
        if begin.match(line):
            inside_flg = True
            continue
        if end.match(line):
            inside_flg = False

        if inside_flg:
            m = row.search(line)
            if m:
                fundamental[m.group(1).strip()] = func(m.group(2).strip())
                prev_key = m.group(1).strip()
            else:
                m2 = re.search(r"(.*)\}\}", line)
                if m2:
                    fundamental[prev_key] += func(m2.group(1).strip())
                    inside_flg = False
                else:
                    fundamental[prev_key] += func(line.strip())
        else:
            if len(fundamental) > 0:
                fundamentals.append(fundamental.copy())
                fundamental.clear()

    return fundamentals


def main():
    f = open('jawiki-england.txt', 'r')
    fundamentals = fundamental_extractor(f, pass_through)
    with open('jawiki-england-fundamentals.json', 'w') as o:
        json.dump(fundamentals, o, ensure_ascii=False)


if __name__ == '__main__':
    main()