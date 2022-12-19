import numpy as np 
import math
#import scipy.linalg as linalg 

class functions:
    #print("asdf")
    def __init__(self, A):
        self.A = A
        self.n = len(self.A)
        self.e = np.zeros((self.n, self.n),dtype=float)
        np.fill_diagonal(self.e, 1) 
        self.coef_pol=list()
        self.coef=list()
        self.a_inv=np.zeros((self.n, self.n))  
        self.b_list=list()

    
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
                                        return e[l+k]
                            else:
                                break
                    else:
                        nul_col = False
                        break
                if not nul_col:
                    for k in range(s+1, self.n):
                        ratio = x[k,j]/x[s,j]
                        x[k, :] = np.around(x[k, :] - ratio * x[s, :],decimals=1)
                        e[k, :] = e[k, :] - ratio * e[s, :]
                        if self.is_in_ref(x):
                            for m in range(self.n):
                                if any(x[i])==0:
                                    e_1.append(e[m])
                                
                    s+=1
        for i in range(self.n):
            if any(x[i])==0:
                e_1.append(e[i])       
        return e_1

    def inverse(self):
        
        val, vec = self.qwer(self.A,1)
        for i in range(self.n):
            self.a_inv[i]=self.b_list[self.n-2][i]/self.coef_pol[self.n-1]
        return self.a_inv

    def eigenvector(self):
        eiv=list()
        eiv2=list()
        r=np.unique(self.eigenvalues)
        r[::-1].sort()
        for i in range(len(r)):
            b=np.subtract(self.A,(r[i])*self.e)
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
        f=np.matmul(self.A,b)
        if k==len(self.A)+1:
            if self.n%2!=0:
                self.coef.append(-1)
                for i in range(self.n):
                    self.coef.append(self.coef_pol[i])
            if self.n%2==0:
                self.coef.append(1)
                for i in range(self.n):
                    self.coef.append(-self.coef_pol[i])
            self.eigenvalues=np.around(np.roots(self.coef),decimals=2)
            self.eigenvalues[::-1].sort()
            self.eigenvector()
            return self.eigenvalues, self.eigenvectors
        return self.qwer(f,k)


class decompositions:

    coef_pol=list()
    coef=list()
    b_list=list()
    y_list=list()

    def __init__(self, A):
        self.A = A
        self.n=len(self.A)
        self.e=np.zeros((self.n,self.n),dtype=float)
        np.fill_diagonal(self.e,1) 
      
      
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
        self.to_print = f"Your matrix:\n {self.A}\n\n"
        #Find A_T * A
        self.A_TA = np.matmul(self.A.T, self.A) 
        #print("as",self.A_TA)
        self.to_print += f"A^T * A:\n {self.A_TA}\n\n"
        
        #Find eigenvalues of A_TA
        self.n = len(self.A_TA)
        self.e=np.zeros((self.n, self.n))
        np.fill_diagonal(self.e,1)
        self.a_inv = np.zeros((self.n, self.n)) 
        self.b_inv = np.zeros((self.n, self.n))
        self.y = np.zeros((self.n,1))
        self.y0 = (self.e[:,[1]])
        #print("ass",self.qwer(self.A_TA, 1))
        self.eigenvalues, self.eigenvectors = pr3.eig(self.A_TA)
        self.eigenvalues
        print(f"!!! {self.eigenvalues, self.eigenvectors}")
        self.D = np.zeros((len(self.A_TA), len(self.A_TA[0])) , dtype = float)
        self.to_print += f"Eigenvalues of A^T*A: {self.eigenvalues}\n\n"

        self.sigmas = list()
        for i in range(len(self.eigenvalues)):
            self.D[i][i] = self.eigenvalues[i]**0.5
            if self.eigenvalues[i]**0.5 != 0:
                self.sigmas.append(self.eigenvalues[i]**0.5)

        #√

        self.to_print += f" D matrix:\n {self.D}\n\n"


    def length(self, v):
        length = 0
        for i in range(len(v)):
            length += v[i]**2
        return round(length**0.5)

    def C_find(self):
        
        self.ortogonalize()

        self.normalize()

        self.C = self.eigenvectors.T
        self.to_print += f"C_T: {self.C}\n\n"

    def B_find(self):
        temp = list()
        for i in range(len(self.sigmas)):
            a = 1/self.sigmas[i]
            matrix = a * self.A
            vector = np.matmul(matrix, self.eigenvectors[i])
            temp.append(vector)

        self.B = np.array(temp, dtype = float)
        self.to_print += f"B: {self.B}\n\n"

    def SVD(self):
        self.D_find()
        self.C_find()
        self.B_find()
        self.to_print += f"SVD:\n {self.B} {self.D} {self.C}\n"
        # print(f"EIGENVECTORS: {self.eigenvectors}")
        # print(self.A_TA)
        # print(self.to_print)
        return self.D, self.C, self.B

    def Q_find(self):
        self.eigenvectors = self.A.copy()
        self.eigenvectors = self.eigenvectors.T
        self.ortogonalize()
        self.normalize()
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
        self.Q_find()
        self.R_find()
        return self.Q, self.R

    def Polar(self):
        self.U = np.matmul(self.B, self.C)
        self.H = np.matmul(np.matmul(self.C.T, self.D), self.C)
        return U, H


class power:

    def __init__(self, A, n):
        self.A = A
        self.n = n

    def positivity_check(self):
        self.eigenvalues, self.eigenvectors = pr3.eig(self.A)
        return self.A == self.A.T and all(elements >= 0 for elements in self.eigenvalues)


class solve:

    def __init__(self, A, b):
        self.A = A
        self.b = b

    def qr_algorithm(self):
        a = decompositions(self.A)
        Q, R = a.QR()
        return np.matmul(np.matmul(np.linalg.inv(R), Q.T), self.b)

