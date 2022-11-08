"""
Given a rectangular grid of m by n spaces, signaled by 0s, and a number of points, signaled by 1, 2, 3..., return the number of moves for the shortest path that starts at 1 and goes over all the other points in ascending order. 

Examples 

shortest_path([                                    [("001"), ("002"), ("003")]
  ("001"), 
  ("002"), 
  ("003") 
]) ➞ 2 

shortest_path([                                    [("00000"), ("01006"), ("02000"), ("30050"), ("00004")]
  ("00000"), 
  ("01006"), 
  ("02000"), 
  ("30050"), 
  ("00004") 
]) ➞ 13 

shortest_path([                                    [("00020000"), ("01000000")]
  ("00020000"), 
  ("01000000") 
]) ➞ 3 
"""
import numpy as np 

matrix = eval(input("Enter matrix: "))

def shortest_path(matrix):
    temp = list()
    for i in range(len(matrix)):
        x = list()
        for j in range(len(matrix[i])):
            x.append(int(matrix[i][j]))
        temp.append(x)
    
    arr = np.array(temp)
    coor = list()
    i = 1
    while len(np.where(arr == i)[0]) != 0:
        x, y = np.where(arr == i)
        coor.append([x, y])
        i+=1
    cnt = 0
    for i in range(len(coor)-1):
        cnt += abs(coor[i][0] - coor[i+1][0])
        cnt += abs(coor[i][1] - coor[i+1][1])

    return cnt[0]
print(shortest_path(matrix))