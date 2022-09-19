"""
The computer makes a number from 1 to 100. 
The user has three attempts to guess. After each unsuccessful attempt, the computer reports fewer or more numbers.
SAMPLE:
Numbers: 76
Guess: 5
The number is more
Guess: 100
The number is fewer
Guess 76
BINGO!
"""

import random

n = random.randint(1, 100)
ans = False
guess1 = int(input("Your guess: "))

def check(guess):
    if n == guess:
        print("Bingo")
        ans = True
    elif n < guess:
        print("The number is fewer")
    else:
        print("The number is more")
    
check(guess1)

if not ans:
    guess2 = int(input("Your guess: "))
    check(guess2)

if not ans:
    guess3 = int(input("Your guess: "))
    check(guess3)

if not ans:
    print(n)
