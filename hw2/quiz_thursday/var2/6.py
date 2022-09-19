"""
Write a program that takes N. And calculates the result of the following sequence. (1.5 points)
1 + 2 + 3*2*3! + 4*2*4! + ….+n*2*n!
"""

n = int(input())

def factorial(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return n * factorial(n-1)

def ans(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        cnt = 3
        for i in range(3, n+1):
            cnt = n*2*factorial(n)
        return cnt
    
print(ans(n))
