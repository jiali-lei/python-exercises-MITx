# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 17:29:32 2017

@author: jialilei
"""

s = 'qahlooob'
temp = s[0]
best = ''
for i in range(len(s)-1):
    if s[i]<=s[i+1]:
        temp += s[i+1]
    else:
        if(len(temp)>len(best)):
            best = temp        
        temp = s[i+1]
if(len(temp)>len(best)):
    best = temp 
print(best)