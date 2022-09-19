"""
Given a five-digit number (NOT A STRING). Increase by 2 times the numbers in odd positions. (0.25 points)
SAMPLE:
Enter number: 12345
Output: 14385
"""
n = eval(input())

def ans(n):
    n0 = n//10000
    n1 = n//1000 - n0*10
    n2 = n//100 - n0*100 - n1*10
    n3 = n//10 - n0*1000 - n1*100 - n2*10
    n4 = n%(n0*10000 + n1*1000 + n2*100 + n3*10)
    return n0*10000 + n1*2000 + n2*100 + n3*20 + n4
    
print(ans(n))