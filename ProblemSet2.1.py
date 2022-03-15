#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:04:37 2019

@author: pranavkapur
"""

balance = 42
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
minMonthlyPaymentRate = 0.04

for i in range(1, 13):
    balance -= balance*minMonthlyPaymentRate
    balance += balance*monthlyInterestRate
balance = round(balance, 2)
print('Remaining balance: ' + str(balance))