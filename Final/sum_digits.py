# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:32:23 2017

@author: jialilei
"""

#def sum_digits(s):
#    """
#    assumes s a string
#    returns an int that is the sum of all of the digits in s.
#        if there are no digits in s, it raises a ValueError exception.
#    """
#    sum = 0
#    try:
#        for i in s:
#            if i.isdigit():
#                sum+=int(i)
#    except:
#        raise ValueError('no digits in s')
#    return sum
#exception is thrown when error is encountered during the try execution.
#which is why it's not what the spec is asking for.
    
def sum_digits(s):
    # comprehension returns a list of bool in this case.
    if all([not c.isdigit() for c in s]):
        raise ValueError()
    sum = 0
    for i in s:
        if i.isdigit():
            sum+=int(i)
    return sum