"""
Given a three-digit number (NOT A STRING). Swipe the first and last digits.

SAMPLE:

Enter number: 341

Output: 143
"""
n = int(input())

n0 = n//100
n1 = n//10 - n0*10
n2 = n%(n0*100 + n1*10)

print(n2*100+n1*10+n0)