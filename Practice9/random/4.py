"""
Generate random String of length 5
Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
"""

import random as r
import string

def get_random_string():
    ans = ''.join(r.choice(string.ascii_letters) for i in range(5))
    return ans

for i in range(5):
    print(get_random_string())