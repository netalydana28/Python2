"""
ABC is an integral sided triangle with sides a≤b≤c.
mc is the median connecting C and the midpoint of AB.
F(n) is the number of such triangles with c≤n for which mc has integral length as well.
F(10)=3 and F(50)=165.
Find F(100000).
"""
import math

n = int(input("Enter your n number "))
a, b, c, mc = int, int, int, int

def median(a, b, c): #function to find median
    return math.sqrt((2*b**2 + 2*a**2 - c**2)/4)

def F(n):
    cnt = 0
    for c in range(1, n+1):
        for b in range(1, c+1):
            for a in range(1, b+1):
                if a + b > c and c + b > a and  c + a > b:
                    #print(median(a, b, c))
                    if median(a, b, c) - int(median(a, b, c)) == 0.0: # as i understood integral median is median that is integer number
                        #print(a, b, c)
                        cnt+=1
    print(f"F({n}) = {cnt}")
                    

F(n)