'''Pig Latin Translator 

    Translates English sentences to Pig Latin based on the following set of rules:
        1) For words that begin with a consonant, all letters before the initial vowel are placed at the end
           of the word, then "ay" is added. 
        2) For words that begin with a vowel, just add "way" to the end.
        3) Puntuation is removed.
        4) All characters are lowercase.

    Created by Liam Brew on 03.26.19'''


#Global for ease of modification.
punctuation_list = '.,/:;"()[]<>#@!$%^&|/?'
vowels_list = 'aeiouy'

def main():
    #Loops for ease of use.
    while True:
        #User input.
        string = input("Word: ")
        
        #Empty input catch.
        if len(string) == 0:
            print("Input error: empty input")
            continue

        #Removes punctuation and ensures case compliance on a per-index basis of the string.
        new_string = ""
        for index in string:
            if index not in punctuation_list:
                new_string = new_string + index.lower()     
        string = new_string.split()

        def translator(string):
            '''Translates the input into Pig Latin according to the provided guidelines.'''

            #The word starts with a vowel.
            if string[0] in vowels_list:
                return(string + 'way')
        
            #The first vowel is contained within the word.
            for i in range(1, len(string)):
                if string[i] in vowels_list:
                    return(string[i:] + string[0:i] + 'ay')

        #Translates each word of the string.
        for i in range(0, len(string)):
            print(translator(string[i]))

main()
        



    
