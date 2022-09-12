"""
.Write a Python program to find the median of threevalues.
ExpectedOutput:
Input first number: 15
Input second number: 26
Input third number: 29
The median is 26.0
"""
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
ans = float()
if a > b:
    if a > c:
        if b > c:
            ans = b
        else:
            ans = c
    else:
        ans = a
else:
    if a < c: 
        if c < b:
            ans = c
        else:
            ans = b
    else:
        ans = a

print(f"The median is {ans}")