"""
Find three-digit numbers equal to the sum of the cubes of their numbers
SAMPLE:
153
370
371
407
"""
a = True
nums = list()
while a:
    n = int(input())
    if n == 0:
        a = False
    else:
        nums.append(n)


def get_numbers(n):
    n0 = n//100
    n1 = n//10 - n0*10
    n2 = n%(n0*100+n1*10)
    return n0, n1, n2

def check(n):
    n0, n1, n2 = get_numbers(n)
    if n == pow(n0, 3) + pow(n1, 3) + pow(n2, 3):
        return True
    else:
        return False

for i in range(len(nums)):
    print(f" {nums[i]} --> {check(nums[i])}")
