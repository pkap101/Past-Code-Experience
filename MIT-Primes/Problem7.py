#Problem 7
#Python version 3.7.6
#Jupyter Notebook Framework
#MacOS platform

#test data: used the encoded strings from Problem 6

#I put these test strings in the file Problem6InputText.txt
inputText = input("Enter file path for encoded text:")
#I used english.txt for the alphabet encodings, and changed around some of the symbols and values
alphabetEncodings = input("Enter file path for alphabet encodings:")
#I used Problem6OutputFile_7InputFile.txt
exportFile = input("Enter file path for output file to write decoded text:")

#assigns variable to string of encoded text
with open(inputText) as encodedText:
    text = encodedText.read()
    #print(text)

#uses input encoding file to create 1 list with symbols, 1 list with corresponding encoding
with open(alphabetEncodings) as alphabetEncodings:
    symbols = []
    encodings = []
    for line in alphabetEncodings:
        symbols.append(line[0])
        encodings.append(line[2:-1])

#takes in string of binary encoded text, symbols, and encodings, returns lowercase string of decoded text                
def decodeText(text, symbols, encodings):
    decodedText = ''
    pos = 0
    
    #goes through text and adds symbol for each encoding
    for i in range (len(text)):
        #if symbol encoding is 1 digit long
        if text[i-pos:i+1] in encodings:
            decodedText += symbols[encodings.index(text[i-pos:i+1])]
            pos = 0
        else:
            pos +=1
        #print(pos, decodedText)
    return decodedText
                                   
#writes decoded text onto output file
with open(exportFile, 'w') as outputFile:
    decodedText = decodeText(text, symbols, encodings)
    outputFile.write(decodedText)
                                   
        