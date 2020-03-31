# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    """
    pseudo code:
    for all letters in secretWord:
        if letter is not in letterGuessed:
            return False
    return True
    """
    l_sW = list(secretWord) # convert string to list
    for i in l_sW:
        if i not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    """
    pseudo code:
    word = ""
    for all letters in secretWord:
        if letter is in letterGuessed:
            concatenate the letter onto word
        otherwise
            concatenate a "_ " onto word
    return word
    """
    word = ""    # create a empty list, ready to append letters to it
    l_sW = list(secretWord)
    for i in l_sW:
        if i in lettersGuessed:
            word += i
        else:
            word += "_ "
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    """
    pseudo code:
    import string
    alphabet = string.ascii_lowercase
    for any letter in lettersGuessed:
        remove that letter from alphabet
    report that result to who called you
    """
    import string
    alphabet = string.ascii_lowercase
    l_alpha = list(alphabet)
    for i in lettersGuessed:
        l_alpha.remove(i)
    return ''.join(l_alpha)
    
    
        
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
    # FILL IN YOUR CODE HERE...
    """
    pseudo code:
    declare necessary variables
    greeting
    game
        while (either the player has remaining guesses)
        report remaining guesses, available letters, then prompt for input
        evaluate iput
            if player guesses a letter in word:
                add that letter to lettersGuessed
                report Good guess: _ a_ _
                if they have guessed all letters:
                    then break
                remaining guesses stay the same
            else if player guesses letter already guessed:
                report Oops! you've already guessed the letter: _ a_ _
                remaining guesses stay the same
            otherwise:
                player guesses a letter not in word
                add that letter to lettersGuessed
                report Oops! that letter is not in my word: _ a_ _
        continue play until either
            player has no remaining guesses
            player guesses all letters in word: yay!
    """
    
    # welcome message and inform user length of secretWord
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", str(len(secretWord)), "letters long.")
    print("---------------")
    n = 8       # declare a variable to count guesses
    lettersGuessed = []     # declare lettersGuessed as a list
    while (n>0):    # continue play until player has no remaining guesses
        # report remaining guesses, available letters, then prompt for input        
        print("You have", str(n), "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter: ")
        # ensure user-input letter to be lower case        
        low_letter = letter.lower()
        
        # if player guesses letter already guessed
        if low_letter in lettersGuessed:
            print("Oops! You've already guessed that letter:", str(getGuessedWord(secretWord, lettersGuessed)))            
            print("----------------")              
            n = n        
        # if player guesses letter in word
        elif low_letter in list(secretWord):        
            lettersGuessed += low_letter
            print("Good guess:", str(getGuessedWord(secretWord, lettersGuessed)))
            print("----------------")            
            if isWordGuessed(secretWord, lettersGuessed)==True:
                break
            n = n
        # otherwise player guesses a letter not in word
        else:
            lettersGuessed += low_letter
            print("Oops! That letter is not in my word:", str(getGuessedWord(secretWord, lettersGuessed)))
            print("----------------")             
            n -= 1  # update the remaining guesses
    if getGuessedWord(secretWord, lettersGuessed) == secretWord:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was else.")




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
