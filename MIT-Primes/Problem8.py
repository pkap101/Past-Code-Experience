#Problem 8
#Python version 3.7.6
#Jupyter Notebook Framework
#MacOS platform


#For the 1st part of this problem, I use my code from problem 4 to get the encodings for a given alphabet

import sys
import math

#my input file for test data is Problem4TestData.txt and Problem5TestData.txt
filePath = input("Enter file path for input data of alphabet frequencies:")

# uses input file of alphabet/frequencies to create 1 list with letters, 1 list with corresponding frequencies, 
# and 1 list for encodings
with open(filePath) as inputFile:
    letters = []
    freqs = []
    encodings = []
    for line in inputFile:
        letters.append(line[0])
        freqs.append(float(line[2:]))

#checks if total frequencies sum to 100, writes error message and exits program if not        
totalFreq = 0
for i in range(len(freqs)):
    totalFreq+=float(freqs[i])
if totalFreq < 99.999 or totalFreq > 100.001:
    with open(exportFile, 'w') as outputFile:
            outputFile.write("Error: the total frequency of the characters did not equal 100, it was " + str(totalFreq))
    print("Error: the total frequency of the characters did not equal 100, it was " + str(totalFreq))
    sys.exit()
    
#print(letters, freqs)


# Each object created in the class is a node in the huffman tree
class node:
    def __init__(self, freq, char, left=None, right=None):
        # frequency of character
        self.freq = freq

        # character/letter in alphabet
        self.char = char

        # node left of current node (starts at none)
        self.left = left

        # node right of current node (starts at none)
        self.right = right

        # tree direction (0/1)
        self.huff = ''
        
    #used to print and test properties of a node
    def __repr__(self):
        return (str(self.freq) + str(self.char) + str(self.left) + str(self.right) + str(self.huff))
    

#uses huffman tree and node properties to write huffman encoding for each character to output file
#adds encoding for each node to list
def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
  
    # recursively goes through tree until a leaf(character) is reached
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
  
        # if node is a leaf(character) then display its huffman code
    if(not node.left and not node.right):
        encodings.append([newVal, node.char])

# list containing unused nodes
nodes = []
  
# creates node for each letter/corresponding frequency
for x in range(len(letters)):
    nodes.append(node(freqs[x], letters[x]))

# creates tree until 1 node is left by assigning properties to each node
# combines 2 smallest nodes and stores a 0 or 1 to each node
# This allows for a later traversal through the tree where all nodes have a 0 or 1
while len(nodes) > 1:
    # sort all the nodes in ascending order of frequency
    nodes = sorted(nodes, key=lambda x: x.freq)
  
    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]
  
    # assign directional value to these nodes (0 for smaller node, 1 for larger node)
    left.huff = 0
    right.huff = 1
  
    # combines the 2 smallest nodes to create a new object/node as their parent
    newNode = node(left.freq+right.freq, left.char+right.char, left, right)
  
    #removes the 2 nodes and adds their parent as a new node
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
  

#calls print nodes, creates list of encodings for each character
printNodes(nodes[0])

#bubble sort algorithm used to sort encodings based on length
def lengthSort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if len(array[j][0]) > len(array[j + 1][0]):
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#bubble sort algorithm used to sort encodings of equal length in alphabetical order
def lexSort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if (letters.index(array[j][1]) > letters.index(array[j + 1][1])) and (len(array[j][0]) == len(array[j + 1][0])):
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#sorts encodings in short-lex order
encodingsFinal = lexSort(lengthSort(encodings))

#calculates the length of encoded text of 10000 letters distributed according to frequencies.
def findLength(letters, freqs, encodings):
    totalLength = 0
    #multiplies length of encoding by frequency of letter for each letter
    for value in encodingsFinal:
        length = len(value[0])
        freq = freqs[letters.index(value[1])]
        totalLength += (length*freq*100)
        #print(length, value[1], freq)
    return totalLength

#finds compression factor using length of huffman encoded text and equal length encodings
def compressionFactor(totalLength, letters):
    n = len(letters)
    #finds length of each letter for equal encodings
    equalEncodingLength = math.ceil(math.log2(n))
    totalEqualLength = equalEncodingLength*10000
    
    #divides length of huffman encodings by equal encodings
    compressionFactor = totalLength/totalEqualLength
    return compressionFactor

# (part 1) prints length of the encoded text of 10000 letters distributed exactly according to the given frequencies.
lengthHuffmanEncodings = findLength(letters, freqs, encodingsFinal)
print("Length of the encoded text of 10000 letters distributed exactly according to the given frequencies:", lengthHuffmanEncodings)

# (part 2) prints compression factor
compressionFac = compressionFactor(lengthHuffmanEncodings, letters)
print("Compression Factor: ", compressionFac)
