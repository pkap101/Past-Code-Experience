#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:16:24 2019

@author: pranavkapur
"""

s = 'abcdefghijklmnopqrstuvwxyz'
temp = s[0]
longest = ''

for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        temp+=s[i]
    else: 
        if len(temp) > len(longest):
            longest = temp
        temp = s[i]

if len(temp) > len(longest):
    longest = temp
print("Longest substring in alphabetical order is: " + longest)