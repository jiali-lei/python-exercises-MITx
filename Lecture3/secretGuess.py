# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:52:07 2017

@author: jialilei
"""

low = 0
high = 100
ans = (high + low)//2
x = ''

print("Please think of a number between 0 and 100!")
while x != 'c':
    print("Is your secret number " + str(ans) + "?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if x not in ('h', 'l', 'c'):
        print("Sorry, I did not understand your input.")
    else:
        if x == 'h':
            high = ans
        elif x == 'l':
            low = ans
        ans = (high + low)//2
print("Game over. Your secret number was: " + str(ans))
