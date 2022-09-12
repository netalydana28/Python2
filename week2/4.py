"""
Write a Python program to check whether an alphabetis a vowel or consonant.
Expected Output:Input a letter of the alphabet: k
k is a consonant
"""
letter = input("Input a letter of the alphabet: ")
if letter == "a" or letter == "i" or letter == "o" or letter == "u" or letter == "e":
    print(f"{letter} is vowel")
elif letter == "y":
    print(f"{letter} is technically a consonant, there are many more instances in which it functions as a vowel.")
else:
    print(f"{letter} is constant")