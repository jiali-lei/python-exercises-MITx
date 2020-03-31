# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 23:39:58 2017

@author: jialilei
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True is k is triangular and false is not
    """
    tri = []
    tri_sum = 0
    for i in range(k+1):
        tri_sum += i
        tri.append(tri_sum)
    if k in tri[1:]:
        return True
    else:
        return False