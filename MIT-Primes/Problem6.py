#Problem 6
#Python version 3.7.6
#Jupyter Notebook Framework
#MacOS platform

#test data strings below
# she sells sea shells by the sea shore
# Hello World!
# Peter Piper picked a peck of pickled peppers
# I scream, you scream, we all scream for ice cream
# His palms are sweaty, knees weak, arms are heavy, there’s vomit on his sweater already: Mom’s spaghetti
# If you admire somebody you should go on 'head tell 'em, People never get the flowers while they can still smell 'em

#I put these test strings in the file Problem6InputText.txt
inputText = input("Enter file path for input text:")
#I used english.txt for the alphabet encodings, and changed around some of the symbols and values
alphabetEncodings = input("Enter file path for alphabet encodings:")
#I used Problem6OutputFile_7InputFile.txt
exportFile = input("Enter file path for output file to write encoded text:")

#uses input text file to create str of text without uppercase letters
with open(inputText) as decodedText:
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    text = decodedText.read()
    for char in text:
        if char in uppercase:
            text.replace(char, lowercase[uppercase.index(char)])
    #print(text)
    
#uses input encoding file to create 1 list with symbols, 1 list with corresponding encoding
with open(alphabetEncodings) as alphabetEncodings:
    symbols = []
    encodings = []
    for line in alphabetEncodings:
        symbols.append(line[0])
        encodings.append(line[2:-1])
        
#takes in string of lowercase text, symbols, and encodings, returns string of encoded text        
def encodeText(text, symbols, encodings):
    encodedText = ''
    #adds encoding for each character in text unless the character is not given in the alphabetEncodings file
    for char in text:
        if char in symbols:
            encodedText += encodings[symbols.index(char)]
        else:
            pass
        #print(char, encodedText)
    return encodedText

#writes encoded text onto output file
with open(exportFile, 'w') as outputFile:
    encodedText = encodeText(text, symbols, encodings)
    outputFile.write(encodedText)
