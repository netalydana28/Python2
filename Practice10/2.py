"""
Concert Seats 

Create a function that determines whether each seat can "see" the front-stage. 
A number can "see" the front-stage if it is strictly greater than the number before it. 
"""

import numpy as np

a = np.array([ 

  [1, 2, 3], 

  [4, 5, 6], 

  [7, 8, 9] 

])

t_a = a.T
def check():
    for i in range(len(t_a)):
        for j in range(len(t_a[i])-1):
            if t_a[i][j] >= t_a[i][j+1]:
                return False
    return True

print(check())


"""
can_see_stage([ 

  [1, 2, 3], 

  [4, 5, 6], 

  [7, 8, 9] 

]) ➞ True 

 

can_see_stage([ 

  [0, 0, 0], 

  [1, 1, 1], 

  [2, 2, 2] 

]) ➞ True 

 

can_see_stage([ 

  [2, 0, 0],  

  [1, 1, 1],  

  [2, 2, 2] 

]) ➞ False 

 

can_see_stage([ 

  [1, 0, 0], 

  [1, 1, 1], 

  [2, 2, 2] 

]) ➞ False 
"""
