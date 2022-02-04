#2
def print_upper_words(words):
    '''This function prints every word in a list of words with each character uppercased'''

    for word in words:
        print(word.upper())


#3 
def print_upper_words(words):
    '''This function prints every word in a list in uppercase only if its first character is 'e' '''
    for word in words:
        if word[0] == 'e':
            print(word.upper())

#4
def print_upper_words(words, letter_1, letter_2):
    '''This function prints every word in a list in upper case if the word starts with any of the letters that are passed in as arguments'''
    for word in words:
        if word[0] == letter_1 or word[0] == letter_2:
            print(word.upper())