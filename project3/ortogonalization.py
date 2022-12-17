import numpy as np
"""
def ortogonalize(eigenvectors):
    k = list()
    for i in range(1, len(eigenvectors)):
        print(f"{eigenvectors[i]}, {eigenvectors[i-1]})/np.dot({eigenvectors[i-1]}, {eigenvectors[i-1]})")

        temp = np.dot(eigenvectors[i], eigenvectors[i-1])/np.dot(eigenvectors[i-1], eigenvectors[i-1])
        print(temp)
        k.append(temp)

        for j in range(len(k)):
            print(f"{i} -= {k[j]} * {eigenvectors[j]}")

            eigenvectors[i] -= k[j] * eigenvectors[j]

    print(eigenvectors)
"""
def ortogonalize(eigenvectors):
    k = list()
    for i in range(1, len(eigenvectors)):
        print(f"{eigenvectors[i]}, {eigenvectors[i-1]})/np.dot({eigenvectors[i-1]}, {eigenvectors[i-1]})")
        for j in range(i):
            print(f"{i} -- {j}")
            temp = np.dot(eigenvectors[i], eigenvectors[j])/np.dot(eigenvectors[j], eigenvectors[j])
            k.append(temp)

        print(f"coefficients: {k}")

        for j in range(len(k)):
            print(f"{i} -= {k[j]} * {eigenvectors[j]}")

            eigenvectors[i] -= k[j] * eigenvectors[j]
        k.clear()

    print(eigenvectors)


#a= np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype = float)
#a= np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype = float)
a = np.array([[1, 1, 0], 
             [0, 2, 1],
             [0, 2, 3]], dtype = float )
eigenvectors = a

def normalize(eigenvectors):
    length_v = 0
    for i in range(len(eigenvectors)):
        length_v += eigenvectors[i]**2

    length_v = length_v ** 0.5
    for i in range(len(eigenvectors)):
        eigenvectors[i] = eigenvectors[i]/length_v


ortogonalize(eigenvectors)
normalize(eigenvectors[0])
normalize(eigenvectors[1])
normalize(eigenvectors[2])
print(eigenvectors.T)


print(np.matmul(eigenvectors.T, a))

