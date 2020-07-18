# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

print("Welcome to the game, Hangman!")
print("I am thinking of a word that is " + str(len(secretWord))+" letters long.")
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
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
    ans = []
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                ans.append(i)
                break
    return len(ans) == len(secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = []
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                ans.append(i)
                break
        if len(lettersGuessed) == 0:
            ans.append("_ ")
        elif i != j:
           ans.append("_ ")
    return ''.join(ans)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ans = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        for j in lettersGuessed:
            if i == j:
                break
        if len(lettersGuessed) == 0 or i != j:
            ans.append(i)
    return ''.join(ans)
    


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

    mistakesMade = 8
    availableLetters = ""
    guessedLetters = ""
    
    while mistakesMade > 0:
        print("You have " + str(mistakesMade) + " guesses left.")
        print("Available letters: " + (getAvailableLetters(availableLetters)))
        lettersGuessed = input("Please guess a letter: ")
        lettersAllLower = lettersGuessed.lower()
        
        print(len(lettersAllLower))
        
        if len(lettersAllLower) == 0 or len(lettersAllLower) > 1 or not lettersAllLower.isalpha():
            print("Please enter one letter!")
            break

        
        count = 0
        for letter in secretWord:
            if lettersAllLower == letter:
                guessedLetters += lettersAllLower
                if lettersAllLower in availableLetters:
                    print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, availableLetters))
                    print("-----------")
                    mistakesMade += 1
                else:
                    print("Good guess: " + getGuessedWord(secretWord, guessedLetters))
                    print("-----------")
                    mistakesMade += 1
                    break
            else:
                count += 1
            if count == len(secretWord):
                if lettersAllLower in availableLetters:
                    print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, availableLetters))
                    print("-----------")
                    mistakesMade += 1
                else:
                    print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, guessedLetters))
                    print("-----------")
        if availableLetters != "":
            if lettersAllLower in availableLetters:
                availableLetters = availableLetters
            else:
                availableLetters += lettersAllLower
        else:
            availableLetters = lettersAllLower  

        mistakesMade -= 1
    
        if isWordGuessed(secretWord, guessedLetters):
            print("Congratulations, you won!")
            break
        elif mistakesMade == 0:
            print("Sorry, you ran out of guesses. The word was "+secretWord+".")

