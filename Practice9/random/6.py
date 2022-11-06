"""
Calculate multiplication of two random float numbers
Note:
•	First random float number must be between 0.1 and 1
•	Second random float number must be between 9.5 and 99.5
"""

import random as r

first_random = r.uniform(0.1, 1)
second_random = r.uniform(9.5, 99.5)

print(f"First random: {first_random}")
print(f"Second random: {second_random}")
print(f"Multiplication of two random float numbers: {first_random * second_random}")