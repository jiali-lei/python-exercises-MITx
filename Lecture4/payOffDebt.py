# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:39:22 2017

@author: jialilei
"""

# Test Case 1:
balance = 81
annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
minPayment = 0
ub = balance
while ub > 0:
    ub = balance 
    minPayment += 10
    for m in range(12):
        ub = ub - minPayment
        ub = ub + ub * annualInterestRate/12
        print("Month " + str(m+1) + " Remaining balance: " + str(round(ub, 2)))
#print("Remaining balance: " + str(round(ub, 2)))
print("Lowest Payment: " + str(minPayment))
    