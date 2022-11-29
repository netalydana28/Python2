import numpy as np 

matrix = np.array([[0, 0, 1], [1, 1, 0], [-1, 1, 0]], dtype = float)

def normalization(v):
    length_v = 0
    for i in range(len(v)):
        length_v += v[i]**2
    print(length_v)
    length_v = length_v ** 0.5
    print(length_v)
    for i in range(len(v)):
        print(v[i])
        v[i] = v[i]/length_v
    
    print(v)

for i in range(len(matrix)):
    normalization(matrix[i])

print(matrix)
print(1/(2**0.5))