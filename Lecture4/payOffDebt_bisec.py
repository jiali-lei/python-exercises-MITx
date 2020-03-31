# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 23:26:26 2017

@author: jialilei
"""

# Test Case 1:
balance = 320000
annualInterestRate = 0.2
lower = balance/12      #monthly payment lower bound
upper = (balance * (1 + annualInterestRate/12)**12)/12      # monthly payment upper bound
ub = balance
while abs(ub) > 0.01:
    ub = balance
    minPayment = (lower + upper)/2.0
    for m in range(12):
        ub = ub - minPayment
        ub = ub + ub * annualInterestRate/12
        print("Month " + str(m+1) + " Remaining balance: " + str(round(ub, 2)))
    if ub == 0:
        break
    elif ub > 0:
        lower = minPayment
    else:
        upper = minPayment
print("Lowest Payment: " + str(round(minPayment, 2)))        
        