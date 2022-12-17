import alg
import numpy as np

m = np.array([[1, -3, 4], [4, -7, 8], [6, -7, 7]], dtype = float)
#m = np.array([[1, 1, 2], [0, 3, 2], [1, 3, 9]], dtype = float)
mat = np.array([[7, 0, 2], 
             [0, 4, 0],
             [2, 0, 5]], dtype = float )

#m = np.array([[1, 1, 0], 
#             [0, 2, 1],
#             [0, 2, 3]], dtype = float )
#m = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype= float)
#m = np.array([[3, 1], [2, 4], [-1, -1]], dtype = float)
#m = np.array([[1, 1, 0], [1, 1, 0], [0, 0, 1]], dtype= float)
m = np.array([[3, 1, -1], [2, 4,- 2], [-1, -1, 3]], dtype= float)
m = np.array([[-1, 0], [0, -1]], dtype= float)
m = np.array([[2, 0, 0], [1, 2, 0], [0, 0, 0.5]], dtype= float)
m = np.array([[0, 6, -2, 2], [-1, 5, -1, 1], [-1, 1, -1, -1], [2, -4, 4, 2]], dtype= float)
m = np.array([[2, 3, 2], [3, 3, 3], [2, 1, 2]], dtype= float)
m = np.array([[3, 1, -1], [2, 4,- 2], [-1, -1, 3]], dtype= float)





def isuppertriangular(M):
    for i in range(1, len(M)):
        for j in range(0, i):
            if(round(M[i][j], 1) != 0):
                return False
    return True

a = alg.decompositions(m)
Q, R = a.QR()


print("--------------------------------------")

#mat=np.array([[7,-4,4],
#            [2,3,2],
#            [2,0,5]],dtype=float)
        
a = alg.decompositions(mat)
D, C, B = a.SVD()
print(D)
print(C)
print(b)


