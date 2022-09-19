"""
Given a four-digit number. If it is read from left to right and from right to left equally, then output yes, otherwise no.
SAMPLE:
Enter a 4 digit number: 4334
Yes
Enter a 4 digit number: 1234
No
"""

n = int(input())

n0 = n//1000
n1 = n//100 - n0*10
n2 = n//10 - n0*100 - n1*10
n3 = n%(n0*1000 + n1*100 + n2*10)

if n0 == n3 and n1 == n2:
    print("Yes")
else:
    print("No")