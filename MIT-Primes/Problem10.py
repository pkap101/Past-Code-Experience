#Problem 10
#Python version 3.7.6
#Jupyter Notebook Framework
#MacOS platform

import random

#generates a random operation of replacing, deleting, or adding a character to a text file
#uses paramater M - length of text file
def operationRDA(M): 
    #depending on random letter, one of the 3 r/d/a operations is chosen
    rda = random.choice('rda')
    position = random.randint(1,M)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    randLetter = random.choice(letters)

    #replace operation
    if rda == 'r':
        operation = f"{position} r {randLetter}"
        return operation
    
    #delete operation
    if rda == 'd':
        operation = f"{position} d"
        return operation
    
    #add operation
    if rda == 'a':
        operation = f"{position} a {randLetter}"
        return operation

#I tested the function with different values of M
#for i in range(10):
#    print(operationRDA(118))
