# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:47:45 2017

@author: jialilei
"""

def genSubsets(L):
    res = []
    if len(L) ==0:
        return [[]]
    smaller = genSubsets(L[:-1])
    print("smaller: ", smaller)
    extra = L[-1:]
    print("extra: ", extra)
    new = []
    for small in smaller:
        new.append(small+extra)
        print("new: ", new)
    return smaller+new