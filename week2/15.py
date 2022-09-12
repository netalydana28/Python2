"""
Write a Python program to create the multiplicationtable (from 1 to10) of a number.
Input a number: 6
Expected output:
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
"""
num = int(input("Input a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")