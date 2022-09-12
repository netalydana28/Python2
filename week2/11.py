"""
Write a Python program to display the sign ofthe Chinese Zodiac forgiven year in which you were born.
ExpectedOutput:Input your birth year: 1986
Your Zodiac sign: Tiger
"""

zodiac = {
    1: "Rooster",
    2: "Dog",
    3: "Pig",
    4: "Rat",
    5: "Ox",
    6: "Tiger",
    7: "Raggit",
    8: "Dragon",
    9: "Snake",
    10: "Horse",
    11: "Goat",
    0: "Monkey",
}

birthyear = int(input("Input your birth year: "))
print(f"Your Zodiac sign: {zodiac[birthyear%12]}")