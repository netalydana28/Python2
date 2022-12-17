import numpy as np

coefficients = list()
def ortogonalize(eigenvectors):
    k = list()
    for i in range(1, len(eigenvectors)):
        for j in range(i):
            
            temp = np.dot(eigenvectors[i], eigenvectors[j])/np.dot(eigenvectors[j], eigenvectors[j])
            k.append(temp)

        for j in range(len(k)):

            eigenvectors[i] -= k[j] * eigenvectors[j]
        k.clear()

#a= np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype = float)
#a= np.array([[1, -3, 4], [4, -7, 8], [6, -7, 7]], dtype = float)
#a= np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype = float)
a = np.array([[7, 0, 2], 
             [0, 4, 0],
             [2, 0, 5]], dtype = float )
#a = np.array([[3, 1, -1], [2, 4,- 2], [-1, -1, 3]], dtype = float)
#a = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype= float)
eigenvectors = a.copy()
eigenvectors = eigenvectors.T

length = list()
def normalize(eigenvectors):
    length_v = 0
    for i in range(len(eigenvectors)):
        length_v += eigenvectors[i]**2

    length_v = length_v ** 0.5
    length.append(length_v)
    for i in range(len(eigenvectors)):
        eigenvectors[i] = eigenvectors[i]/length_v


ortogonalize(eigenvectors)
print(eigenvectors)
normalize(eigenvectors[0])
normalize(eigenvectors[1])
normalize(eigenvectors[2])
print(eigenvectors.T)

k = 0

R = np.zeros((len(eigenvectors), len(eigenvectors)))
for i in range(k, len(eigenvectors)):
    for j in range(k, len(eigenvectors)):
            R[i][j] = np.dot(eigenvectors[i].T, a.T[j])
            
    k+=1

print(R)
print(a)