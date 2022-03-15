#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:55:29 2019

@author: pranavkapur
"""

balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
bal = balance
low = balance/12
high = (balance*(1+annualInterestRate))/12
mid = (high+low)/2
epsilon = 0.001

while True:
    balance = bal
    for i in range(12):
        balance -= mid
        balance += balance*monthlyInterestRate
    if abs(balance) <= epsilon:
        break
    elif balance<0:
        high = mid
        mid = (high+low)/2
    else:
        low = mid
        mid = (high+low)/2
mid = round(mid, 2)
print('Lowest Payment: ' + str(mid))
