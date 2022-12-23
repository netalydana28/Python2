import alg
import numpy as np

# mat=np.array([[1.,0.,5., 2.],
#             [0.,3.,2., 1.],
#             [5.,2.,0., 6.],
#             [2, 1, 0, 0.]])
# a = alg.decompositions(mat)
# Q, R = a.QR()
# print(mat)
# print(Q)
# print(R)

mat = np.array([[1, 1, 0], [0, 0, 1]], dtype = float)
#mat = np.array([[2, 0, 2], [0, -2, 0], [2, 0, -1]], dtype = float)

# mat=np.array([[1.,0.,5., 2.],
#             [0.,3.,2., 1.],
#             [5.,2.,0., 6.],
#             [2, 1, 0, 0.]])



a = alg.decompositions(mat)
D, C, B = a.SVD()
print(mat)
print(C)
print(D)
print(B)

#m = np.array([[1, -3, 4], [4, -7, 8], [6, -7, 7]], dtype = float)
#m = np.array([[1, 1, 2], [0, 3, 2], [1, 3, 9]], dtype = float)
# mat = np.array([[8, 0, 2], 
#              [0, 4, 0],
#              [2, 0, 8]], dtype = float )

# m = np.array([[1, 1, 0], 
#             [0, 2, 1],
#             [0, 2, 3]], dtype = float )
#m = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype= float)
#m = np.array([[3, 1], [2, 4], [-1, -1]], dtype = float)
#m = np.array([[1, 1, 0], [1, 1, 0], [0, 0, 1]], dtype= float)
# m = np.array([[3, 1, -1], [2, 4,- 2], [-1, -1, 3]], dtype= float)
# m = np.array([[-1, 0], [0, -1]], dtype= float)
# m = np.array([[2, 0, 0], [1, 2, 0], [0, 0, 0.5]], dtype= float)
# m = np.array([[0, 6, -2, 2], [-1, 5, -1, 1], [-1, 1, -1, -1], [2, -4, 4, 2]], dtype= float)
# m = np.array([[2, 3, 2], [3, 3, 3], [2, 1, 2]], dtype= float)
#m = np.array([[3, 1, -1], [2, 4,- 2], [-1, -1, 3]], dtype= float)




# def isuppertriangular(M):
#     for i in range(1, len(M)):
#         for j in range(0, i):
#             if M[i][j] > 0.001:
#                 return False
#     return True

# def round_matrix(M):
#     for i in range(len(M)):
#         for j in range(len(M)):
#             M[i][j] = round(M[i][j], 2)
        
#     return M



#mat = np.array([[-1, 2, 4], [5, 6, 6], [-3, 5, 9]], dtype = float)
# b = np.array([1, 2, 3], dtype = float)
# print("--------------------------------------")
# a = alg.decompositions(mat)
# Q, R = a.QR()
# print(Q)
# print(R)
# p = [1, 5, 10, 20]
# for i in range(20):
#     a = alg.decompositions(mat)
#     Q, R = a.QR()
#     mat = np.matmul(R, Q)
#     if isuppertriangular(mat):
#         print(mat)

# while not isuppertriangular(mat):
#     a = alg.decompositions(mat)
#     Q, R = a.QR()
#     mat = np.matmul(R, Q)
# else:
#     print(round_matrix(mat))
# a = alg.decompositions(mat)
# print(a.hessenberg())


# print(np.matmul(Q.T, b))
# a = alg.functions(R)
# print("!!")
# print(a.inverse())

# m = np.array([[1, 1, 2], [0, 3, 2], [1, 3, 9]], dtype = float)
# f=alg.functions(m)
# print(f.inverse())
# print(np.matmul(np.matmul(np.linalg.inv(R), Q.T), b))
# mat=np.array([[7,-4,4],
#            [2,3,2],
#            [2,0,5]],dtype=float)

# eigenvalues, eigenvectors = pr3.eig(m)
# print(f"{eigenvalues} \n {eigenvectors}")




# U, H = a.Polar()
# print(U)
# print(H)

# a = alg.square(m)
# a.positivity_check()

# b = np.zeros(3)
# print(b)

# A = alg.solve(mat, b)
# A.solve_lin_sys()

# w, v = LA.eig(mat)
# print(w)
# print(v)

# a = alg.functions(mat)
# values, vectors = a.qwer(mat, 1)
# print(values, vectors)
# print(values, vectors)

