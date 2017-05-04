#!/usr/bin/env python
#-*- coding:utf-8 -*-

def bi_gram(sen):
    arr = []
    sen = list(sen)
    for i in range(len(sen)-1):
        arr.append("".join(sen[i:i+2]))
    return arr

def intersection(X, Y):
    arr = []
    for i in range(len(X)):
        if not X[i] in arr:
            if X[i] in Y:
                arr.append(X[i])
    return arr

def union(X, Y):
    arr = []
    for i in range(len(X)):
        if not X[i] in arr:
            arr.append(X[i])
    for j in range(len(Y)):
        if not Y[j] in arr:
            arr.append(Y[j])
    return arr

def is_include_se(D):
    if "se" in D: return True
    else: return False

sentence1 = "paraparaparadise"
sentence2 = "paragraph"

X = bi_gram(sentence1)
Y = bi_gram(sentence2)

U = union(X, Y)
I = intersection(X, Y)

print(U)
print(I)

print(is_include_se(X))
print(is_include_se(Y))

#print(set(X) | set(Y))
#print(set(X) & set(Y))
