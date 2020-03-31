# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:10:58 2017

@author: jialilei
"""

def cipher(map_from, map_to, code):
    """ 
    map_from, map_to: strings where each contain N unique lowercase letters. 
    code: string (assume it only contains letters also in map_from)
    
    Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
    each key is a letter in map_from at index i and the corresponding 
    value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
    of code using the key_code mapping. 
    """
    dict1 = {}
    for i in range(len(map_from)):
        dict1[map_from[i]] = map_to[i]
    print(dict1)
    
    decoded = ''     
    for e in code:
        decoded += dict1[e]
    return (dict1, decoded)