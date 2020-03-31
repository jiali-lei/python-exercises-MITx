# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:29:30 2017

@author: jialilei
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
    If they are permutations of each other, 
        returns a tuple of 3 items in this order: 
        the element occurring most, how many times it occurs, and its type
    '''
    if len(L1)==0 and len(L2)==0:
        return (None, None, None)
    elif not len(L1)==len(L2):
        return False
    else:
        L1_dict = {i:L1.count(i) for i in L1}
        L2_dict = {i:L2.count(i) for i in L2}
        # print(L1_dict, L2_dict)        
        a = max(L1_dict.values()) 
        # print(a)
        if L1_dict == L2_dict:
            for i in L1_dict:
                if L1_dict[i] == a:
                    return (i, a, type(i))
        else:
            return False