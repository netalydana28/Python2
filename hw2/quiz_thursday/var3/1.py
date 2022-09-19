"""
Display a rectangle filled with letters A. The number of rows in the rectangle is n, the number of columns is m
"""

n, m = map(int, input().split())

def rect(n, m):
    for i in range(n):
        print("A"*m)

rect(n, m)