#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:57:45 2019

@author: pranavkapur
"""

low = 0
high = 100
guess = (low+high)//2
print("Please think of a number between 0 and 100!")
while True:
    print("Is your secret nunmber " + str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response == 'h':
        high = guess
    elif response == 'l':
        low = guess
    elif response == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
    guess = (low+high)//2
