import numpy as np

def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n

x = np.array([1, 0, 0])
a = np.array([[8, 0, 2], 
             [0, 4, 0],
             [2, 0, 5]])

for i in range(8):
    x = np.dot(a, x)
    lambda_1, x = normalize(x)
    
print('Eigenvalue:', lambda_1)
print('Eigenvector:', x)

a = a - lambda_1 * np.eye(len(a))
print(a)

for i in range(8):
    x = np.dot(a, x)
    print(x)
    lambda_1, x = normalize(x)
    
print('Eigenvalue:', lambda_1)
print('Eigenvector:', x)