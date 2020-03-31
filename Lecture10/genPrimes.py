# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:40:47 2017

@author: jialilei
"""

def genPrimes():
    next = 2
    pList = []
    while True:
        if len(pList)==0:
            yield next
            pList.append(next)
        else:
            if all(next%p!=0 for p in pList):
                yield next
                pList.append(next)
            next+=1