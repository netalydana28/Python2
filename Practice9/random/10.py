"""
Create a random alphanumeric string of length ten that must contain at least four digits. 
For example, the output can be anything like 1o32WzUS87, 1P56X9Vh87
"""

import random as r 
import string 

def get_string():
    temp = list()
    digits = string.digits
    letters = string.ascii_letters
    everything = digits + letters
    
    for i in range(4):
        temp.append(r.choice(digits))

    for i in range(6):
        temp.append(r.choice(everything))

    ans = ""
    
    while temp: # arrange characters in random order
        char = r.choice(temp)
        ans += char
        temp.remove(char)
    
    return ans


print(get_string())