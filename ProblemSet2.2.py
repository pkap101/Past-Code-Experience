#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:19:14 2019

@author: pranavkapur
"""

balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
lmp = 10
bal = balance

while True:
    balance = bal
    for i in range(1, 13):
        balance -= lmp
        balance += balance*monthlyInterestRate
    if balance <= 0:
        break
    else:
        lmp += 10
        
print('Lowest Payment: ' + str(lmp))
