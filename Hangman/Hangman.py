'''
Created on Feb 9, 2020

@author: ITAUser
'''

import random

def pick_random_word():
    """
     This function picks a rondom word from the words dictionary
    """
    #open the words dictionary 
    with open("words.txt", 'r') as f:
        words = f.readlines()

    #generate a random index
    #-1 because len(words) is not valid index in the list 'words'
    index = random.randint (0,len (words) - 1)

    #print out the word at that index \
    word = words[index].strip() 
    return word

def ask_user_for_next_letter():
    #this function gets a letter guess from the user
    letter = input ("Guess your letter: ")
    return letter.strip().upper()

def generate_word_string(word, letters_guessed): 
    """
This function generates the word display that shows which letters the user has guessed correctly
    """
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")
       
    return " ".join (output)
 
 #check that the moduele we are using is currently that main module
 
if __name__=='__main__':
 
    WORD = pick_random_word()
 
    letters_to_guess = set(WORD)
    correct_letters_guessed = set ()
    incorrect_letters_guessed = set ()
    num_guesses = 0 
 
    # welcome 
    print("welcome to Hangman!")

    #loop repeats y=the guessing sequence until the user guesses all the letters or  until the user runs out of guesses
    while((len(letters_to_guess) > 0) and num_guesses < 6): 
        guess = ask_user_for_next_letter()
        guess = guess.lower()
        
        #check if we user already guessed that letter
        
        if (guess in correct_letters_guessed or \
            guess in incorrect_letters_guessed):
            print ("You already guessed that letter.")
            continue
            
        #check if the guess was correct 
        if guess in letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess) 
            num_guesses += 1

        #print how much of the word is guessed, and how many letters are left
        word_string = generate_word_string(WORD,correct_letters_guessed)
        print (word_string)
        print("you have {} guesses left.". format (6 - num_guesses))

    #tell the user if they have won or lost
    if num_guesses < 6:
        print ("Conradulations {}".format(WORD))
    else:
        print ("sorry, you loose! Your word was {}".format(WORD))