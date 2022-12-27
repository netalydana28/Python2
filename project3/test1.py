from alg import matrix
import numpy as np

a1=np.array([[1,0,2],
            [2,-1,3],
            [5,0,2]])
a2=np.array([[1,9,2],
            [12,-1,-3],
            [5,5,2]])
c1=np.array([[9,4,-2],
            [8,-1,3]])
c2=np.array([[2,9,2],
            [3,-11,13]])
a=np.array([[1.2,0.,2.1, 4.2],
            [2.2,-1.4,3.9, 8.]])
c=np.array([[9.1,4.,-2.4],
            [8.,-1.4, 3.5],
            [2.1,3.,7.],
            [0.,2.2,3.]])
z=np.array([[-5.,6.,8.,5.],
            [9.,0.,4.,6],
            [8.,4.,1.,3.],
            [7.,5.,-1.,2.]])
z1=np.array([[-5.,6.,8.,5.],
            [9.,0.,4.,6],
            [8.,4.,1.,3.],
            [7.,5.,-1.,2.]])
z2=np.array([[-5.,6.,8.],
            [9.,0.,4.],
            [8.,4.,1.],
            [7.,5.,-1.]])
z3=np.array([[0., 6., -2., 3.],
        [6., 2., 3., -1],
        [0., 2., 9., 2]])

m1 = matrix(a)
m2 = matrix(c)
m3 = matrix(a1)
m4 = matrix(c1)
m5 = matrix(z)
m6 = matrix(z1)
m7 = matrix(z2)
m10 = matrix(z3)
m12 = matrix(a2)
m13 = matrix(c2)
m8=matrix(np.array([[1.,2.,3.],
            [2.,5.,7.],
            [4.,9.,13.]]))
t=matrix(np.array([[-3.,6.,-1.,1.,-7.],
        [1.,-2.,2.,3.,-1.],
        [2.,-4.,5.,8.,-4.]]))
m9=matrix(np.array([[1.,2.,3.],
            [2.,5.,4.],
            [1.,1.,5.]]))

m11=matrix(np.array([[2.,2.,1.],
            [0.,1.,7.],
            [-5.,11.,-2.]]))
#print('Subtraction for matrices')
#print(f'{m1}-{m2}={m1-m2}')
#print()
print('Subtraction for matrices')
print(f'A = \n{m3}')
print(f'B = \n{m12}')
print(f'answer is \n{m3-m12}')
print('---------------------')
print('Subtraction for matrices')
print(f'A = \n{m4}')
print(f'B = \n{m13}')
print(f'answer is \n{m4-m13}')
print('---------------------')
#print('Addition for matrices')
#print(f'{m1}+{m2}={m1+m2}')
#print()
print('Addition for matrices')
print(f'A = \n{m3}')
print(f'B = \n{m12}')
print(f'answer is \n{m3+m12}')
print('---------------------')
print('Addition for matrices')
print(f'A = \n{m4}')
print(f'B = \n{m13}')
print(f'answer is \n{m4+m13}')
print('---------------------')
print('Multiplication for matrices')
print(f'A = \n{m1}')
print(f'B = \n{m2}')
print(f'answer is \n{m1*m2}')
print('---------------------')
print('Multiplication for matrices')
print(f'A = \n{m3}')
print(f'B = \n{m12}')
print(f'answer is \n{m3*m12}')
print('---------------------')
#print('Multiplication for matrices')
#print(f'{m1}*{m4}={m1*m4}')
#print()
print('Determinant of matrices')
print(f'det{m5} = {m5.det()}')
print('---------------------')
print('Determinant of matrices')
print(f'det{m3} = {m3.det()}')
print('---------------------')
print('Transpose of matrix')
print(f'{m5}')
print('is')
print(f'{m5.T()}')
print('---------------------')
print('Transpose of matrix')
print(f'{m10}')
print('is')
print(f'{m10.T()}')
print('---------------------')
print('Swap rows 1 and 2')
print(f'before \n{m5}')
m5.swap_rows(1,2)
print(f'after \n{m5}')
print('---------------------')
print('Swap rows 0 and 2')
print(f'before \n{m3}')
m3.swap_rows(0,2)
print(f'after \n{m3}')
print('---------------------')
print('Rank')
print(f'rank{m6}')
print(m6.rank())
print('---------------------')
print('Rank')
print(f'rank{m7}')
print(m7.rank())
print('---------------------')
print('ref')
print(f'before \n{m6}')
print(f'after \n{m6.ref()}')
print('---------------------')
print('ref')
print(f'before \n{m7}')
print(f'after \n{m7.ref()}')

print('---------------------')
print('rref')
print(f'before \n{m8}')
print(f'after \n{m8.rref()}')
print('---------------------')
print('rref')
print(f'before \n{t}')
print(f'after \n{t.rref()}')
print('---------------------')
print('Column space')
print(f'A = \n{m9}')
print(m9.col_sp())
print('---------------------')
print('Column space')
print(f'A = \n{m10}')
print(m10.col_sp())
print('---------------------')
print('Null Space')
print(f'A = \n{t}')
print(t.nul_sp())
print('---------------------')
print('Null Space')
print(f'A = \n{m11}')
print(m11.nul_sp())
print('---------------------')
print('Solve system')
print(t)
print(t.solve_sys())
print('---------------------')
print('Solve system')
print(m11)
print(m11.solve_sys())