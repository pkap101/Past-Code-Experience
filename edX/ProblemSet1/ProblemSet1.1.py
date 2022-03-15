#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:57:14 2019

@author: pranavkapur
"""

s = 'ihdkflehfofipefufqohhbc'
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1

print('Number of vowels: ' + str(numVowels))
