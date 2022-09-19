"""
Three numbers are given from the user at once. Write "yes" if you can take any two of them and get the third in total.
SAMPLE:
Enter numbers: [2, 3, 1]
Output: yes
Enter numbers: [5,5,4]
Output: no
"""

a = eval(input())

def check(a):
    if a[0] == a[1] + a[2] or a[1] == a[0] + a[2] or a[2] == a[1] + a[0]:
        return "yes"
    else:
        return "no"

print(check(a))