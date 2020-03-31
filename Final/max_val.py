# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:07:37 2017

@author: jialilei
"""

def max_val(t): 
    """ 
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t
    """ 
    if isinstance(t, int):
        return t
    max = -float('inf')
    for e in t:
        m = max_val(e)
        if m > max:
            max = m
            print(max)
    return max