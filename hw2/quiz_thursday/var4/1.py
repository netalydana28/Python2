"""
The user enters six numbers at once. Find the smallest odd number among them.
If it does not exist, output the phrase "not found" (0.25 points)

SAMPLE:

Enter numbers: [2, 4, 5, 6, 1, 9]

Output: 1

Enter numbers: [2, 6, 8, 8, 8, 4]

Output: not found
"""
a = eval(input())
odd_list = list()
for i in range(len(a)):
    if a[i]%2 != 0:
        odd_list.append(a[i])

if not odd_list:
    print("not found")
else:
    ans = odd_list[0]
    for i in range(1, len(odd_list)):
        if odd_list[i] < ans:
            ans = odd_list[i]
    print(ans)