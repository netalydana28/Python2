#Exercise 3: Pick a random character from a given string

import random as r

given_string = input()

random_character = r.choice(given_string)

print(f"String: {given_string}\n Chosen character: {random_character}")