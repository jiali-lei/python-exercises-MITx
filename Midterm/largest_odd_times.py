# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:42:46 2017

@author: jialilei
"""

def largest_odd_times(L):
    """ 
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number of times in L. 
    If no such element exists, returns None 
    """
    L_dict = {i:L.count(i) for i in L}
    L_set = set()
    for i in L_dict:
        if not L_dict[i]%2==0:
            L_set.add(i)
    if L_set:
        return max(L_set)
    else:
        return None