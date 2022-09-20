"""
Create a program that takes a string and replaces each letter with its appropriate position in the alphabet.
Rules:
Replace all letters with position in alphabet.
If anything in the string isn't a letter, ignore it.
a is 1, b is 2, c is 3, etc, etc.
Examples:
"We have a lot of rain in June." ➞ "23 5 8 1 22 5 1 12 15 20 15 6 18 1 9 14 9 14 10 21 14 5"
"The river stole the gods." ➞ "20 8 5 18 9 22 5 18 19 20 15 12 5 20 8 5 7 15 4 19"
"Wow, does that work?" ➞ "23 15 23 4 15 5 19 20 8 1 20 23 15 18 11"
"""
line = input()
ans = ""

for i in line:
    if ord(i.lower()) < 97 or ord(i.lower()) > 122:
        ans += i
    else:
        ans += (str(ord(i.lower())-96) + " ")

print(ans)