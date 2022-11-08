"""
Find out a wrong number in a 2D list. 

The end number of each row is the sum of each row's previous numbers. 

The end number of each column is the sum of each column's previous numbers.

"""
import numpy as np
import array as arr

n = 4

a = np.array([(2, 2, 3, 6), (4, 5, 6, 15), (7, 8, 9, 24), (12, 15, 18, 45)])


wrong_row = list()
wrong_column = list()

for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(n):
        if j == n-1:
            if cnt1 != a[i][j]:
                wrong_row.append(i)
        else:
            cnt1 += a[i][j]

        if j == n-1:
            if cnt2 != a[j][i]:
                wrong_column.append(i)
        else:
            cnt2 += a[j][i]

for i in range(len(wrong_row)):
    if wrong_column[i] == n-1:
        ans = 0
        for j in range(n-1):
            ans += a[wrong_row[i]][j]
    else:
        ans = a[wrong_column[i]][n-1]
        for j in range(n-2, 0, -1):
            ans -= a[wrong_row[i]][j]

    print(f"wrong number(arr{wrong_row[i]+1}) -- {ans}")


