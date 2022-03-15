#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:11:24 2019

@author: pranavkapur
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count +=1
        else:
            return False
    if count == len(secretWord):
        return True
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    str = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            str += letter + ' '
        else:
            str += '_ '
    return str

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    unguessedLetters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in lettersGuessed:
        if letter in unguessedLetters:
            unguessedLetters = unguessedLetters.replace(letter, '')
    return unguessedLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    length = len(secretWord)
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(length) + ' letters long.')
    guessesLeft = 8
    guessedLetters = []
    while True:
        print('-------------')
        if isWordGuessed(secretWord, guessedLetters) == True:
            print('Congratulations, you won!')
            break
        if guessesLeft == 0:
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
            break
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(guessedLetters))
        guess = input('Please guess a letter: ')
        if guess in guessedLetters:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guessedLetters))
        elif guess in secretWord:
            guessedLetters += guess
            print('Good guess: ' + getGuessedWord(secretWord, guessedLetters))
            
        else: 
            guessedLetters += guess
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, guessedLetters))
            guessesLeft -= 1
        
