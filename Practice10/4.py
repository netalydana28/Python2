"""
Frequency by Level of Nesting 

Create a function that takes in a nested list and an element and returns the frequency of that element by nested level. 

Examples 

freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1) 

➞ [[0, 1], [1, 2], [2, 3]] 

# The list has one 1 at level 0, 2 1's at level 1, and 3 1's at level 2. 

 

freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5) 

➞ [[0, 3], [1, 4], [2, 0]] 

 

freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2) 

➞ [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]] 
"""
import numpy as np

mylist = eval(input("Enter list: "))
n = int(input("Enter number: "))
arr = np.array(mylist, dtype=object)

def freq_count(arr, n):
    ans = list()
    index = 0
    temp = list()
    check = True

    def count(arr, n, index):
        temp = list()
        cnt = 0
        for i in range(len(arr)):
            if type(arr[i]) == int:
                if arr[i] == n:
                    cnt += 1
            elif type(arr[i]) == list:
                temp += arr[i]
            if i == len(arr) - 1:
                ans.append([index, cnt])
                index += 1
        arr = temp
        if len(temp)!= 0:
            count(arr, n, index)
    
    count(arr, n, 0)
    print(ans)


freq_count(arr, n)


