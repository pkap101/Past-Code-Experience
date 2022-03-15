#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:39:12 2019

@author: pranavkapur
"""

s = "eiwbobdbobobwhgbob"
numBob = 0
i = 0

for i in range(len(s)+1):
    if s[i: i+3] == "bob":
        numBob+=1
        
print("Number of times bob occurs is: " + str(numBob))