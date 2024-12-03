import sys 
from spellchecker import SpellChecker
from nltk import word_tokenize

# import nltk
# print(nltk.data.find('tokenizers/punkt'))

import nltk
nltk.download('punkt')
print(nltk.data.find('tokenizers/punkt'))


# Create an instance of the spell checker 
spell = SpellChecker()

# token --> stores the tokenize words 
tokens = []

def readTextFile(textFilename):
    '''This function is used to read the input file '''
    global tokens
    words = []
    with open(textFilename,'r') as inputFile:
        tokens=word_tokenize(inputFile.read())
        # Create a list of words from these tokens checking if the word is alphanumeric
        words = [word for word in tokens if word.isalpha()]
        inputFile.close()
    return words

def findErrors(textwords):
    '''This function is used to detect the errors in file if any'''
    missspell_words = []
    for word in textwords:
        if spell.correction(word)!=word:
            missspell_words.append()
    return missspell_words

def printerrors(errorlist):
    '''This function is used to print the errors'''
    print("---------------------")
    print("Misspelled words are:")
    print("---------------------")
    for word in errorlist:
        print(f"{word} : {spell.candidates(word)}")
        
        
def correctErrors(errorList):
    '''This function is used to correct the errors and
    write the corrected text in output.txt file'''
    # open a new file to write the corrected text
    for i in range(len(tokens)):
        if tokens[i] in errorList:
            tokens[i] = spell.correction(tokens[i])
            
    with open("output.txt", "w") as outputFile:
        outputFile.write(" ".join(tokens))
        outputFile.close()
    
def main():
    textFile = input("Enter the File:")
    
    textList=readTextFile(textFile)
    errorList=findErrors(textList)
    
    # if there are no errors 
    if len(errorList) == 0:
        print("No error detected")
        return
    print(errorList)
    
    user_answer = input("Do you want to auto correct the errors Y/N?")
    
    if user_answer.lower() == "y" or user_answer.lower() == "n":
        correctErrors(errorList)
        print("-------------------------------------------------")
        print("Check the output.txt file for the corrected text.")
        print("-------------------------------------------------")
        print("Thankyou for using spelling checker program.")
    else:
        print("--------------------------------------------")
        print("Thankyou for using spelling checker program.")
        print("--------------------------------------------")
        

main()
    
         
    
