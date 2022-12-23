import numpy as np
from fractions import Fraction
import copy
class matrix:
    def __init__(self, value):
        self.value = value
    def __add__(self, m):
        if self.value.shape == m.value.shape:
            s = matrix(np.zeros((m.value.shape)))
            for i in range(m.value.shape[0]):
                for j in range(m.value.shape[1]):
                    s.value[i, j] = self.value[i, j] + m.value[i, j]
            return s
        else:
            return 'It is impossible to add matrices because they have different sizes'
    def __call__(self, i, j):
        return self.a[i, j]
    def __sub__(self, m):
        if self.shape() == m.shape():
            s = matrix(np.zeros((m.shape())))
            print(s.shape())
            for i in range(s.shape()[0]):
                for j in range(s.shape()[1]):
                    s.value[i, j] = self.value[i, j] - m.value[i, j]
            return s
        else:
            return 'It is impossible to substruct matrices because they have different sizes'
            
    def __mul__(self, m):
        if isinstance(m, int) or isinstance(m, float):
            x = []
            for i in range(self.value.shape[0]):
                row = []
                for j in range(self.value.shape[1]):
                    row.append(m * self.value[i, j])
                x.append(row)
            return matrix(np.asarray(x))
        else:
            if self.value.shape[1] == m.value.shape[0]:
                s = matrix(np.zeros((self.value.shape[0], m.value.shape[1])))
                for i in range(s.value.shape[0]):
                    row = self.value[i]
                    for j in range(m.T().value.shape[0]):
                        col = m.value[:, j]
                        s.value[i, j] = sum([row[k] * col[k] for k in range(len(row))])
                return matrix(s)
            else:
                return 'It is impossible to multiply matrices because they do not have suitable sizes'
    
    def __repr__(self):
        return f'{self.value}'
    def del_col(self, j1):
        x = []
        for i in range(self.value.shape[0]):
            row = []
            for j in range(self.value.shape[1]):
                if j == j1:
                    pass
                else:
                    row.append(self.value[i, j])
            x.append(row)
        self.value = np.asarray(x)
    def del_row(self, i1):
        x = []
        for i in range(self.value.shape[0]):
            if i == i1:
                pass
            else:
                row = []
                for j in range(self.value.shape[1]):
                    row.append(self.value[i, j])
                x.append(row)
        self.value = np.asarray(x)
    def col(self, j):
        return self.value[:,j]
    def row(self, i):
        return self.value[i, :]
    def rank(self):
        x = self.ref()
        r = 0
        for i in range(self.value.shape[0]):
            s = 0
            for j in range(self.value.shape[1]):
                if x.value[i,j] != 0:
                    s+=1
            if s != 0:
                r += 1
        return r
    def is_in_ref(self):
        lead_entry = [] 
        for i in range(self.value.shape[0]):
            for j in range(self.value.shape[1]):
                if self.value[i, j] != 0:
                    lead_entry.append(j)
                    break
        a = True
        for i in range(1, len(lead_entry)):
            if lead_entry[i] <= lead_entry[i-1] :
                a = False
        return a
    def T(self):
        x = []
        for j in range(self.value.shape[1]):
            col = []
            for i in range(self.value.shape[0]):
                col.append(self.value[i, j])
            x.append(col)
        return matrix(np.asarray(x))

    def det(self):
        if self.value.shape[0] != self.value.shape[1]:
            return 'It is impossible to calculate determinant'
        else:
            d = 1
            if self.is_in_ref():
                x = self.value
            else:
                x = self.ref().value
            for i in range(self.value.shape[0]):
                d *= x[i, i]
            print('d = ', d)
            return round(d,3)
        
    def swap_rows(self, i1, i2):
        x = []
        for i in range(self.value.shape[0]):
            row = []
            if i == i1:
                for j in range(self.value.shape[1]):
                    row.append(self.value[i2, j])
            elif i == i2:
                for j in range(self.value.shape[1]):
                    row.append(self.value[i1, j])
            else:
                for j in range(self.value.shape[1]):
                    row.append(self.value[i, j])
            x.append(row)
        self.value = np.asarray(x)
    def ref(self):
        x = self
        s = 0
        if not x.is_in_ref():
            #print(x)
            for j in range(self.value.shape[1]):
                nul_col = True
                for i in range(s, self.value.shape[0]):
                    if x.value[s,j] == 0:
                        i1 = s
                        if x.value[i,j] != 0:
                            nul_col = False
                            i2 = i
                            x.swap_rows(i1, i2)
                            if x.is_in_ref():
                                return matrix(np.round(x.value, 3))
                            else:
                                break
                    else:
                        nul_col = False
                        break
                if not nul_col:
                    for k in range(s+1, self.value.shape[0]):
                        ratio = x.value[k,j]/x.value[s,j]
                        x.value[k, :] = x.value[k, :] - ratio * x.value[s, :]
                       
                        if x.is_in_ref():
                            return matrix(np.round(x.value, 3))
                    s+=1
        return matrix(np.round(x.value, 2))
                    
                
    def rref(self):
        x = matrix(copy.deepcopy(self.value))
        x = x.ref()
        lead_entry = {}
        for i in range(self.value.shape[0]):
            for j in range( self.value.shape[1]):
                if x.value[i,j] != 0:
                    s = x.value[i,j]
                    lead_entry[i] = j
                    x.value[i, :] = x.value[i, :] / s
                    break
        n = len(lead_entry)
        for j in range(n-1, -1, -1):
            for i in range(j-1, -1, -1):
                ratio = x.value[i, lead_entry[j]]/x.value[j, lead_entry[j]]
                x.value[i, :] = x.value[i, :] - ratio * x.value[j, :]
        return matrix(np.round(x.value, 2))
    
    
    def pivot_col(self):
        self = self.rref()
        lead_entry = []
        for i in range(self.value.shape[0]):
            for j in range(self.value.shape[1]):
                if self.value[i, j] != 0:
                    lead_entry.append(j)
                    break
        return lead_entry

    def col_sp(self):
        x = copy.deepcopy(self.value)
        self = self.rref()
        col_space = {}
        lead_entry = self.pivot_col()
        for i in range(len(lead_entry)):
            col_space[f'v{i+1}'] = list(x[:,i])
        return col_space
    def nul_sp(self):
        x = matrix(copy.deepcopy(self.value))
        x = x.rref()
        lead_entry = []
        for i in range(self.value.shape[0]):
            for j in range(self.value.shape[1]):
                if x.value[i, j] != 0:
                    lead_entry.append(j)
                    break
        span_set = [[] * x for x in range(self.value.shape[1] - len(lead_entry) + 1)]
        d = {}
        for i in range(self.value.shape[1]):
            if i not in lead_entry:
                d[i] = [0 for i in range(self.value.shape[1])]
        for i in range(len(lead_entry)):
            for j in range(lead_entry[i] + 1, self.value.shape[1]):
                for c in d.keys():
                    d[c][c] = 1
                if j not in lead_entry:
                    d[j][lead_entry[i]] = (-1 * x.value[i, j])
        if len(d) == 0:
            ans = [0 for i1 in range(self.value.shape[1])]
            return ans       
        return d
a=np.array([[2.2,1,0.5,2],
            [1,1.3,2,1],
            [0.5,2,0.5,1.6],
            [2,1,1.6,2]])
b=np.array([[3.2,1,0.5,2],
            [1,1.3,2,1],
            [0.5,2,0.5,1.6],
            [2,1,1.6,2]])
c=np.array([[3.2,1,0.5,2],
            [1,1.3,2,1],
            [0.5,2,0.5,1.6]])
d=np.array([[3,1],
            [1,1],
            [0,2]])
e=np.array([[2,0,2],
            [1,3,2]])
f=np.array([[1,0,2],
            [2,-1,3],
            [5,0,2]])
g=np.array([[1,0,5,2],
            [0,3,2,1],
            [5,2,0,6],
            [2,1,0,0]])
h=np.array([[1.,0.,5.,2.],
            [0.,3.,2.,1.],
            [5.,2.,0.,6.],
            [2.,1.,0.,0.]])
k=np.array([[1,7,5,2],
            [0,3,2,1],
            [0,0,2,6],
            [0,0,0,-1]])
l=np.array([[1,2,3,7],
        [2,5,9,6],
        [2,7,3,5]], dtype = float)
n=np.array([[1,2,3,7,6,7],
        [2,5,9,6,2,3],
        [2,7,3,5,0,9]])
p=np.array([[1.,2.,3.,7.,6.,7.],
        [1.,2.,3.,7.,6.,8.],
        [2.,4.,6.,14.,12.,19.]])
r=np.array([[1.,2.,3.,7.,6.,7.],
        [0.,0.,0.,0.,9.,8.],
        [0.,0.,0.,0.,0.,19.]])
s=np.array([[1.,2.,3.,7.],
        [0.,0.,0.,9.],
        [0.,0.,0.,19.]])
t=np.array([[-3.,6.,-1.,1.,-7.],
        [1.,-2.,2.,3.,-1.],
        [2.,-4.,5.,8.,-4.]])
j=np.array([[2.,3.,-2.,0.],
        [1.,0.,1.,0.],
        [0.,3.,-3.,8.]])
w=np.array([[0., -1., -1.],
        [0., -1., -1.],
        [0., -1., -1.]])
u=np.array([[0., 0., 0.],
        [0., -4., 0.],
        [0., 0., 0.]])
z=np.array([[0., 6., -2., 3.],
        [6., 2., 3., -1],
        [0., 2., 9., 2]])
z1=np.array([[1., 2., 3.],
        [2., 5., 9.],
        [2., 7., 3],
        [1., 2., 4.]])
z2=np.array([[2., 5., 1., 8],
        [-5., 7., 0., 3.]])
z3=np.array([[1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]])
z4=np.array([[1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.]])
m1 = matrix(a)
m2 = matrix(b)
m3 = matrix(h)
m4 = matrix(k)
m5 = matrix(n)
m6 = matrix(p)
m7 = matrix(r)
m8 = matrix(s)
m9 = matrix(t)
m10 = matrix(w)
m11 = matrix(f)
m12 = matrix(u)
m13 = matrix(z)
m14 = matrix(l)
m15 = matrix(z1)
m16 = matrix(z2)
m17 = matrix(z3)
m18 = matrix(z4)
print(m13)
print(m13.col_sp())
print(m13.nul_sp())
print(m13)
print(m1+m2)
print(m1)
print(m2)
print(m14.solve_sys())
#print(m16.solve_sys())
#print(m17.nul_sp())
#print(m18.nul_sp())

                   

            