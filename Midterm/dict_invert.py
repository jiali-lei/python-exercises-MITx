# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:48:40 2017

@author: jialilei
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    d_inv = {}
    for i in d:
        if d[i] in d_inv:
            d_inv[d[i]].append(i)
        else:
            d_inv[d[i]] = [i]
    for i in d_inv:
        d_inv[i].sort()
    return d_inv