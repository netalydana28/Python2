#Given a 647 x 170 rectangle. How many squares with side 30 can be cut from it?

n, m = map(int, input().split())

def squares30(n, m):
    n = n//30
    m = m//30
    return n*m

print(squares30(n, m))
