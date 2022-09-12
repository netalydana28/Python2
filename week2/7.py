"""
Write a Python program to check a string representan integer or not.
ExpectedOutput:Input a string: KBTU
The string is not an integer.
"""

a = input("Input a string: ")

try:
    type(int(a))
    print("The string is an integer.")
except:
    type(a)
    print("The string is NOT an integer.")