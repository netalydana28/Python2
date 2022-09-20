"""
Given a three-digit number (NOT A STR). Is it true that the numbers are arranged in ascending order
SAMPLE:
Enter a number: 123
Yes
Enter a number: 451
NO
"""
n = int(input())

n0 = n//100
n1 = n//10 - n0*10
n2 = n%(n0*100+n1*10)

def ascending(n0, n1, n2):
    if n0<n1 and n1<n2:
        return "Yes"
    else:
        return "No"

print(ascending(n0, n1, n2))