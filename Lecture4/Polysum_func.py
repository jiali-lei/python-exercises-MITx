# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 16:11:41 2017

@author: jialilei
"""

import math
def polysum(n, s):
    """
    n: int, number of sides of a regular polygon
    s: int, the length of each side for a regular polygon
    
    return: float w/4 decimal places,
    the rum of area + square of perimeter of regular polygon
    """
    area = 0.25*n*s**2/math.tan(math.pi/n)
    perimeter = n*s
    return round(area+perimeter**2, 4)