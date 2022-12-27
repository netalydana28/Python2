import numpy as np 
import copy
#import scipy.linalg as linalg 

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

class decompositions:

    def __init__(self, A):
        self.A = A  

    def is_in_ref(self, mat):
        lead_entry = [] 
        
        for i in range(self.n):
            for j in range(self.n):
                if mat[i, j] != 0:
                    lead_entry.append(j)
                    break
        a = True
        for i in range(1, len(lead_entry)):
            if lead_entry[i] <= lead_entry[i-1] :
                a = False
        return a

    def swap_rows(self, a, i1, i2):
        x = []
        for i in range(self.n):
            row = []
            if i == i1:
                for j in range(self.n):
                    row.append(a[i2, j])
            elif i == i2:
                for j in range(self.n):
                    row.append(a[i1, j])
            else:
                for j in range(self.n):
                    row.append(a[i, j])
            x.append(row)
        a = np.asarray(x)
        return a

    def ref(self, mat, l):
        x = mat
        # print("dfg,", x)
        s = 0    
        e = np.zeros((self.n, self.n))
        np.fill_diagonal(e,1)
        e_1=list()
        if not self.is_in_ref(x):
            for j in range(self.n):
                nul_col = True
                for i in range(s, self.n):
                    if x[s,j] == 0:
                        i1 = s
                        if x[i,j] != 0:
                            nul_col = False
                            i2 = i
                            x= self.swap_rows(x,i1, i2)
                            e=self.swap_rows(e,i1, i2)
                            if self.is_in_ref(x):
                                for k in range(self.n):
                                    if any(x[k])==0:
                                        pass
                            else:
                                break
                    else:
                        nul_col = False
                        break
                if not nul_col:
                    for k in range(s+1, self.n):
                        ratio = x[k,j]/x[s,j]
                        #x[k, :] = np.around(x[k, :] - ratio * x[s, :],decimals=1)
                        x[k, :] = (x[k, :] - ratio * x[s, :])
                        e[k, :] = e[k, :] - ratio * e[s, :]
                        if self.is_in_ref(x):
                            for m in range(self.n):
                                if any(x[i])==0:
                                    pass               
                    s+=1
        for i in range(self.n): 
            if any(np.around(x[i],decimals=1))==0: 
                e_1.append(e[i])        
        # print("asd",e_1) 
        return e_1

    def inverse(self):
        
        val, vec = self.qwer(self.mat,1)
        for i in range(self.n):
            self.a_inv[i]=self.b_list[self.n-2][i]/self.coef_pol[self.n-1]
        return self.a_inv

    def eigenvector(self):
        eiv=list()
        eiv2=list()
        r=np.unique(self.eigenvalues)
        r[::-1].sort()
        # print("asdf,", self.mat)
        for i in range(len(r)):
            b=np.subtract(self.mat,(r[i])*self.e)
            eiv.append(self.ref(b.transpose(),1))
        for i in range(len(eiv)):
            eiv2+=eiv[i]
        self.eigenvectors = np.array(eiv2).transpose()

    def qwer(self,x, k):

        b=np.zeros((self.n, self.n))
        p0=0
        diag=np.diagonal(x)
        for i in range(self.n):
            p0=p0+diag[i]
        p=(1/(k))*p0
        self.coef_pol.append(p)
        for j in range(self.n):
            b[j]=x[j]-p*self.e[j]
        self.b_list.append(b)
        k=k+1  
        f=np.matmul(self.mat,b)
        if k==len(self.mat)+1:
            if self.n%2!=0:
                self.coef.append(-1)
                for i in range(self.n):
                    self.coef.append(self.coef_pol[i])
            if self.n%2==0:
                self.coef.append(1)
                for i in range(self.n):
                    self.coef.append(-self.coef_pol[i])
            temp_mat = self.A.copy()
            try: self.A = self.A_TA
            except: pass
            #self.eigenvalues=np.around(np.roots(self.coef),decimals=2)
            self.eigenvalues = np.diag(self.schur())
            self.A = temp_mat
            self.eigenvalues = np.sort(self.eigenvalues)[::-1]
            self.eigenvector()
            return self.eigenvalues, self.eigenvectors
        return self.qwer(f,k)

    def eig(self, mat):
        self.mat = mat
        self.n = len(self.mat)
        self.e = np.zeros((self.n, self.n),dtype=float)
        np.fill_diagonal(self.e, 1) 
        self.coef_pol=list()
        self.coef=list()
        self.a_inv=np.zeros((self.n, self.n))  
        self.b_list=list()
        return self.qwer(self.mat, 1) 

    def coefficients(self):
        self.A_TA = self.A
        val, vec = self.eig(self.A)
        return self.coef   

    def ortogonalize(self):
        k = list()
        for i in range(1, len(self.eigenvectors)):

            for j in range(i):
                if np.dot(self.eigenvectors[j], self.eigenvectors[j]) != 0:
                    temp = np.dot(self.eigenvectors[i], self.eigenvectors[j])/np.dot(self.eigenvectors[j], self.eigenvectors[j])
                else: 
                    temp = 1
                k.append(temp)

            for j in range(len(k)):
                self.eigenvectors[i] -= k[j] * self.eigenvectors[j]
            k.clear()         

    def normalize(self):
        for i in range(len(self.eigenvectors)):
            length_v = 0
            for j in range(len(self.eigenvectors[i])):
                length_v += self.eigenvectors[i][j]**2

            length_v = length_v ** 0.5
            for k in range(len(self.eigenvectors[i])):
                if length_v != 0:
                    self.eigenvectors[i][k] = self.eigenvectors[i][k]/length_v

    def D_find(self):
        #Find A_T * A
        temp1 = np.matmul(self.A, self.A.T)
        temp2 = np.matmul(self.A.T, self.A)
        if len(temp1) >= len(temp2):
            self.A_TA = temp1
        else: 
            self.A_TA = temp2

        #Find eigenvalues of A_TA
        self.eigenvalues, self.eigenvectors = self.eig(self.A_TA)
        self.sigmas = list()
        for i in range(len(self.eigenvalues)):
            if self.eigenvalues[i]**0.5 != 0:
                self.sigmas.append(self.eigenvalues[i]**0.5)
        self.D = np.zeros((len(self.sigmas), len(self.A_TA)) , dtype = float)
        for i in range(len(self.sigmas)):
            self.D[i][i] = self.sigmas[i]

        #print(self.D)
        

    def length(self, v):
        length = 0
        for i in range(len(v)):
            length += v[i]**2
        return round(length**0.5)

    def C_find(self):
        self.eigenvectors = self.eigenvectors.T
        self.ortogonalize()
        self.normalize()
        self.C = self.eigenvectors.T
        #print(self.C)


    def B_find(self):
        temp = list()
        for i in range(min(len(self.sigmas), len(self.eigenvectors))):
            a = 1/self.sigmas[i]
            matrix = a * self.A
            vector = np.matmul(matrix, self.eigenvectors[i])
            temp.append(vector)

        self.B = np.array(temp, dtype = float)

    def SVD(self):
        self.D_find()
        self.C_find()
        self.B_find()
        return self.D, self.C, self.B

    def Q_find(self):
        self.eigenvectors = self.A.copy()
        self.eigenvectors = self.eigenvectors.T
        self.ortogonalize()
        #self.round_eigenvectors()

        self.normalize()
        
        # print("__________")
        # print(self.eigenvectors)
        self.Q = self.eigenvectors.copy()
        self.Q = self.Q.T
            

    def R_find(self):
        k = 0
        self.R = np.zeros((len(self.eigenvectors), len(self.eigenvectors)))
        for i in range(k, len(self.eigenvectors)):
            for j in range(k, len(self.eigenvectors)):
                self.R[i][j] = np.dot(self.eigenvectors[i].T, self.A.T[j])
            k+=1
    
    def QR(self):
        if len(self.A) < len(self.A[0]):
            raise ValueError("Number of columns cannot exceed the number of rows")
        else:
            self.Q_find()
            self.R_find()
            return self.Q, self.R

    def Polar(self):
        self.SVD()

        self.U = np.matmul(self.B, self.C.T)
        self.H = np.matmul(np.matmul(self.C, self.D), self.C.T)
        return self.U, self.H

    def isuppertriangular(self, M):
        for i in range(1, len(M)):
            for j in range(0, i):
                if abs(M[i][j]) > 0.001:
                    return False
        return True

    def round_matrix(self, M):
        for i in range(len(M)):
            for j in range(len(M)):
                M[i][j] = round(M[i][j], 2)
        return M

    def schur(self):
        while not self.isuppertriangular(self.A):
            Q, R = self.QR()
            self.A = np.matmul(R, Q)
        else:
            return self.round_matrix(self.A)

    def positivity_check(self):
        f = decompositions(self.A)
        self.eigenvalues, self.eigenvectors = f.eig(self.A)
        a = self.A == self.A.T
        b = all(elements >= 0 for elements in self.eigenvalues)
        return a.all() and b

    def power(self, n): 
        a = self.positivity_check() 
        b = True if n - int(n) == 0.0 else False 
        if b==False and a==False: 
            raise ValueError('No solution in real space') 
        else: 
            self.M = np.zeros((self.A.shape[0], self.A.shape[1]), dtype = float) 
            for i in range(self.A.shape[0]): 
                self.M[i, i] = self.eigenvalues[i] ** n 
            self.eigenvectors = self.eigenvectors.T  
            self.ortogonalize() 
            self.normalize() 
            self.P = self.eigenvectors 
            self.N = self.eigenvectors.T 
 
            return np.matmul(np.matmul(self.N, self.M), self.P)



class solve:

    def __init__(self, A, b):
        self.A = A
        self.b = b

    def qr_algorithm(self):
        a = decompositions(self.A)
        Q, R = a.QR()
        return np.matmul(np.matmul(np.linalg.inv(R), Q.T), self.b)

class Decompositions2():

    def __init__(self,A):
        self.A=A
        self.n=len(self.A)
    def LDU(self):
        self.qwer()
        try:
            d_inv=inv(self.D)
            self.U1=np.matmul(d_inv,self.U)
            print("LDU*:")
            if np.allclose(self.P,np.eye(self.n)):
                print("A:\n", self.A)
                print("L:\n", self.L)
                print("D:\n",self.D)
                print("U*:\n",self.U1)           
            else:
                print("It can be decomposed as PLU")
                print("P:\n", self.P)
                print("A:\n", self.A) 
                print("L:\n", self.L)
                print("D:\n",self.D)
                print("U*:\n",self.U1)        
            
            print("CHECK:")
            pa=np.matmul(self.P,self.A)
            print("PA:\n",pa)
            lu=np.matmul(self.L,self.D)
            ldu1=np.round(np.matmul(lu,self.U1),2)
            print("LDU*:\n",ldu1)
        except Exception as e:
            print("D is not invertible, LDU decomposition does not exist")


    def LU(self):
        self.qwer()
        print("LU:")
        if np.allclose(self.P,np.eye(self.n)):
            print("A:\n", self.A)
            print("L:\n",self.L)
            print("U:\n", self.U)            
        else:
            print("It can be decomposed as PLU")
            print("P:\n", self.P)
            print("A:\n", self.A)
            print("L:\n",self.L)
            print("U:\n", self.U)
        print("CHECK:")
        pa=np.matmul(self.P,self.A)
        print("PA:\n",pa)
        lu=np.matmul(self.L,self.U)
        print("LU:\n",lu)
    def swap(self,x,k,w):
        n=len(x)
        for i in range (k,n):
            for j in range(n):
                if i+1!=n:
                    x[i][j]=x[i+1][j]
                    x[i+1][j]=w[j]
        return x
    def qwer(self):
        U=np.copy(self.A)
        n=self.n
        L = np.zeros((n,n))
        d=list()
        D = np.zeros((n,n))
        U1= np.zeros((n,n))
        np.fill_diagonal(L,1)
        self.P = np.zeros((n,n))
        np.fill_diagonal(self.P,1)    
        for i in range(n):
            for j in range(i+1, n):
                if U[i][i]!=0:
                    ratio = (U[j][i]/U[i][i])
                    L[j][i]=np.around(ratio, decimals=2)
                    U[j]=np.around(U[j]- ratio * U[i],decimals=2)
                    #print(self.A)
                else:
                    w=tuple(U[i])
                    w_p=tuple(self.P[i])
                    self.U=self.swap(U,i,w)
                    self.P=self.swap(self.P,i,w_p)
        d=np.diag(U)
        np.fill_diagonal(D,d)
        
        self.L=L
        self.U=U
        self.D=D