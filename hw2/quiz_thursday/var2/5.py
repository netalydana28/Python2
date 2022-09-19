"""
Let’s say the word the player has to guess is “EVAPORATE”. 
For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. 
For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. 
Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!

_ _ _ _ _ _ _ _ _

>>> Guess your letter: S

Incorrect!

>>> Guess your letter: E

E _ _ _ _ _ _ _ E

...

And so on, until the player gets the word
"""
guess_word = "EVAPORATE"
print(">>> Welcome to Hangman!")
d = {"E": "_", "V": "_", "A": "_", "P": "_", "O": "_", "T": "_", "R" : "_"}

def show(d):
    guessed = ""
    for i in range(len(guess_word)):
        guessed += (d[guess_word[i]] + " ")
    return guessed

def check(d):
    if list(d.keys()) == list(d.values()):
        return True
    else:
        return False

print(show(d))
while not check(d):
    guess_letter = input("Guess your letter: ")
    if guess_letter in d.keys():
        d[guess_letter] = guess_letter
    print(show(d))
    
if(check(d)):
    print("Word is guessed")

