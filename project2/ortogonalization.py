import numpy as np 

matrix = np.array([[-1, 1, 0], [-1, 0, 1], [1, 1, 1]], dtype = float)


def ortogonalize(matrix):
    k = list()
    for i in range(1, len(matrix)):
        temp = np.dot(matrix[i], matrix[i-1])/np.dot(matrix[i-1], matrix[i-1])
        k.append(temp)

        for j in range(len(k)):
            print(matrix[i])
            matrix[i] -= k[j] * matrix[j]
            print("\n")
        print(matrix[i])
        print("\n")

if np.dot(matrix[0], matrix[1]) != 0 or np.dot(matrix[1], matrix[2]) != 0 or np.dot(matrix[0], matrix[2]) != 0:
    ortogonalize(matrix)

print(matrix)