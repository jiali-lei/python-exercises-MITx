# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:09:42 2017

@author: jialilei
"""

def general_poly (L):
    """ 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """    
    def f(x):
        a=0       
        for i in range(len(L)):
            a += L[i]*x**(len(L)-1-i)
        return a
    return f
    