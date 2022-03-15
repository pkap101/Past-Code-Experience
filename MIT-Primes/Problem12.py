#Problem 12
#Python version 3.7.6
#Jupyter Notebook Framework
#MacOS platform

import random

#generates a random operation of replacing, deleting, or adding a word to a text file
#uses paramater M - length of text file
def operationRDA(M): 
    #depending on random letter, one of the 3 R/D/A operations is chosen
    rda = random.choice('RDA')
    position = random.randint(1,M)
    randWord = generateWord()
    wordLen = len(randWord)

    #replace operation
    if rda == 'R':
        operation = f"R {position} {wordLen} {randWord}"
        return operation
    
    #delete operation
    if rda == 'D':
        operation = f"D {position} {wordLen}"
        return operation
    
    #add operation
    if rda == 'A':
        operation = f"A {position} {randWord}"
        return operation

    
def generateWord():
    word = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    freqs = [8.54, 1.6, 3.16, 3.87, 12.1, 2.18, 2.09, 4.96, 7.33, 0.22, 0.81, 4.21, 2.53, 7.17, 7.47, 2.07, 0.1, 6.33, 6.73, 8.94, 2.68, 1.06, 1.83, 0.19, 1.72, 0.11]
    randLetter1 = random.choices(letters, freqs)
    word += (randLetter1[0])
    
    #keeps adding letters until word ends - 15% chance to end after each letter
    while True:
        continueOn = random.choices(['continue', 'stop'], [.85, .15])
        if continueOn == ['stop']:
            break
        else:
            word += (random.choices(letters, freqs)[0])
            #print(word)
    
    return (word)
        
#I tested the function with different values of M
#for i in range(10):
#    print(operationRDA(62))