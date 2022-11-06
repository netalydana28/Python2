"""
Jumping Frog
There are n stones in a pond, numbered 1 to n. Consecutive stones are spaced one unit apart.
A frog sits on stone 1. He wishes to visit each stone exactly once, stopping on stone n. 
However, he can only jump from one stone to another if they are at most 3 units apart. 
In other words, from stone i, he can reach a stone j if 1 ≤ j ≤ n and j is in the set {i-3, i-2, i-1, i+1, i+2, i+3}.

"""
from itertools import permutations
n = int(input("Enter n number: "))
str_n = list()
for i in range(n):
    str_n.append(str(i+1))
permutation = list(permutations(str_n))

ans = list()
for i in range(len(permutation)):
    if permutation[i][0] == "1" and permutation[i][n-1] == str(n):
        ans.append(permutation[i])

def can_jump(n, m):
    ans = list()
    for i in range(1, 4):
        if n - i > 0 and n-i != 1:
            ans.append(n-i)
        if n + i > 0 and n+1 != 1:
            ans.append(n+i)

    return ans

jump_dict = {1: [2, 3, 4]}

for i in range(1, n+1):
    jump_dict[i] = can_jump(i, n)

def check(string):
    for i in range(len(string)-1):
        if int(string[i + 1]) not in jump_dict[int(string[i])]:

            return False
    return True
cnt = 0

for i in range(len(ans)):
    if check(ans[i]):
        cnt+=1

print(cnt)
