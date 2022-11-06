"""
Exercise 5: Generate a random Password which meets the following conditions
•	Password length must be 10 characters long.
•	It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
"""

import random as r
import string 

def get_password():
    temp = list() # i create temporary list of chosen symbols
    digits = string.digits
    temp.append(r.choice(digits)) #at least 1 digit condition
    symbols = string.punctuation 
    temp.append(r.choice(symbols)) #at least 1 special symbol condition
    upper_case = string.ascii_uppercase
    temp.append(r.choice(upper_case)) #at least 2 upper case letters
    temp.append(r.choice(upper_case))
    everything = digits + symbols + string.ascii_letters
    for i in range(6): #fill left places with characters
        temp.append(r.choice(everything))

    password = "" #variable for password

    while temp: # arrange characters in random order
        char = r.choice(temp)
        password += char
        temp.remove(char)

    return password

print(get_password())


