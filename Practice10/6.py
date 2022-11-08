"""
Minesweeper I — Grid 

This challenge is based on the game Minesweeper. 
Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot. 
Return a list where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally). 
"""

import numpy as np 

n, m = map(int, input("Enter dimention of matrix: ").split())
temp_list = list()

for i in range(m):
    line = list(input().split())
    if len(line) == n:
        temp_list.append(line)
    else:
        print("Wrong number of elements")

arr = np.array(temp_list)

for i in range(m):
    for j in range(n):
        if arr[i][j] == "#":
            pass
        else: 
            cnt = 0
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j +2):
                    if k >= 0 and l >= 0 and k < m and l < n:
                        if arr[k][l] == "#":
                            cnt +=1
                            #print(f"{k, l} --- {cnt}")

            arr[i][j] = cnt 

            
print(arr)

"""
1)
5 5
- - - - - 
- - - - -
- - # - - 
- - - - -
- - - - -

2)
5 5
- - - - #
- - - - -
- - # - -
- - - - - 
# - - - -

3)
5 5
- - - # #
- # - - - 
- - # - -
- # # - -
- - - - -
"""