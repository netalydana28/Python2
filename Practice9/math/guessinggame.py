"""
Guessing Game
•	"Your guess is lower than the hidden number" (and you incur a cost of a), or
•	"Your guess is higher than the hidden number" (and you incur a cost of b), or
•	"Yes, that's it!" (and the game ends).
"""

"""
I started solving this task then i noticed that 
C(5,2,3)=5
C(500,2,3)=13.22073197…
C(20000,5,7)=82
C(2000000,5,7)=49.63755955…

Here we get floats. I guess i didn't understand the task
"""
n = int(input("Enter n: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

ans = {}

def guess(n, i, a, b):
    global ans
    cost = 0 
    guess = 2
    while guess != i:
        if guess < i and i + 1 == n:
            guess += 1 
            print(f"{guess} -- {cost}")
        elif guess < i:
            cost += a
            guess += 2
            print(f"{guess} -- {cost}")
        elif guess > i:
            guess -= 1
            cost += b
            print(f"{guess} -- {cost}")    
    else:
        ans[guess] = cost


def C(n, a, b):
    global ans
    number = list()
    for i in range(1, n+1):
        print(i)
        guess(n, i, a, b)

    print(ans)


C(n, a, b)