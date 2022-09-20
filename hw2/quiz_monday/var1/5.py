"""
Calculate 1⋅2 + 2⋅3⋅4 + 4*5*6*7*8+... + n⋅ (n + 1) ⋅ ... ⋅2n. (1.5 points)
SAMPLE:
N = 1
Output: 2
N = 2
Output: 26
N = 3
Output: 866
"""

n = int(input())
final_ans = 0
def calculate(n, m, cnt):
    if n == m+1:
        global ans
        ans = cnt
    else:
        cnt = cnt * n
        calculate(n+1, m, cnt)

for i in range(1, n+1):
    calculate(i, 2*i, 1)
    final_ans+=ans

print(final_ans)


