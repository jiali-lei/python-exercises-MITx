# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:29:50 2017

@author: jialilei
"""

def print_without_vowels(s):
    """
    s: the string to convert
    Finds a version of s without vowels and whose characters apprear in the same order they appear in s.
    Prints this version of s.
    Does not return anything
    """   
    s_list = list(s)
    for i in s_list:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            s_list[s_list.index(i)] = ''
    s_new = ''.join(s_list)
    print(s_new)