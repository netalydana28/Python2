"""
Sum of Squares
Consider equations of the form: a2+b2=N, 0 ≤a≤b, a, b and N integer.
For N=65 there are two solutions:
a=1, b=8 and a=4, b=7.
We call S(N) the sum of the values of a of all solutions of a2+b2=N, 0≤a≤b, a, b and N integer.
Thus S(65) = 1 + 4 = 5.
Find ∑ S(N), for all square free N only divisible by primes of the form 4k+1 with 4k+1<150.

"""
import math

def find_as(N): #find all a numbers that satisfy a2+b2=N, 0 ≤a≤b
    stop = int(math.sqrt(N))
    bs = list()
    for i in range(2, stop+1):
        bs.append(i)

    ans = set()

    for i in range(len(bs)):
        for j in range(1, bs[i]):
            if j**2 + bs[i]**2 == N:
                ans.add(j)

    ans = list(ans)
    return ans

def S(N): # function to find summ of all a numbers
    ans = 0
    my_list = find_as(N)
    for i in range(len(my_list)):
        ans+=my_list[i]

    return ans

def prime_check(n): # function to check if number is prime 
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

my_Ns = list()

for i in range(2, 150): # find all N numbers that satisfy "all square free N only divisible by primes of the form 4k+1 with 4k+1<150"
    if i%4 == 1 and prime_check(i):
        my_Ns.append(i)

for i in range(len(my_Ns)):
    print(f"N: {my_Ns[i]} ---> S(N): {S(my_Ns[i])}")