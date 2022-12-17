import numpy as np 
import sympy as sym
import math
import re

class decompositions:

    coef_pol=list()
    coef=list()
    b_list=list()
    y_list=list()

    def __init__(self, A):
        self.A = A
      
      
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
            #print(lead_entry)
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
        x = mat.copy()
        s = 0
        self.e = np.zeros((self.n, self.n))
        np.fill_diagonal(self.e,1)

        if not self.is_in_ref(x):
                #print(x)
            for j in range(self.n):
                    #print('------', j, '----------')
                nul_col = True
                for i in range(s, self.n):
                        #print('6666666',x.value[s,j] == 0., x.value[s,j])
                    if x[s,j] == 0:
                        i1 = s
                        if x[i,j] != 0:
                            nul_col = False
                            i2 = i
                            x = self.swap_rows(x,i1, i2)
                            e = self.swap_rows(e,i1, i2)
                            #print(e)
                            if self.is_in_ref(x):
                                    #print(x)
                                for k in range(self.n):
                                    if any(x[k])==0:
                                    #    print(x[k])
                                        return self.e[l+k]
                            else:
                                break
                    else:
                        nul_col = False
                        break
                if not nul_col:
                    for k in range(s+1, self.n):
                        ratio = x[k,j]/x[s,j]
                        x[k, :] = np.around(x[k, :] - ratio * x[s, :],decimals=1)
                        self.e[k, :] = self.e[k, :] - ratio * self.e[s, :]
                        #print(x)
                        if self.is_in_ref(x):
                            for m in range(self.n):
                                if any(x[m])==0:  
                                    return self.e[m+l]
                    s+=1
        print(x)
        for i in range(self.n):
            if any(x[i])==0:
                return self.e[i+l]

    def inverse(self):
        for i in range(self.n):
            self.a_inv[i]=self.b_list[n-2][i]/self.coef_pol[n-1]
        return self.a_inv

    def eigenvector(self):
        eiv=list()
        for i in range(len(self.eigenvalues)):
            if i-1!=-1 and self.eigenvalues[i] == self.eigenvalues[i-1]:
                b=np.subtract(self.A,(self.eigenvalues[i])*self.e)
                #print(mat,b)
                eiv.append(self.ref(b.transpose(),1))
            else:
                b=np.subtract(self.A,(self.eigenvalues[i])*self.e)
                #print(b)
                eiv.append(self.ref(b.transpose(),0))
        self.eigenvectors = np.array(eiv).transpose()

    def qwer(self, x, k):
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
                for i in range(n):
                    self.coef.append(-self.coef_pol[i])
            self.eigenvalues = np.around(np.roots(self.coef), decimals=2)
            self.eigenvalues.sort()
            print(self.eigenvalues)
            self.eigenvector()
            return True
        return self.qwer(f,k)

    def D_find(self):
        self.to_print = f"Your matrix:\n {self.A}\n\n"
        #Find A_T * A
        self.A_TA = np.matmul(self.A.T, self.A) 
        self.to_print += f"A^T * A:\n {self.A_TA}\n\n"
        
        #Find eigenvalues of A_TA
        self.n = len(self.A_TA)
        self.e = np.zeros((self.n, self.n))
        np.fill_diagonal(self.e,1)
        self.a_inv = np.zeros((self.n, self.n)) 
        self.b_inv = np.zeros((self.n, self.n))
        self.y = np.zeros((self.n,1))
        self.y0 = (self.e[:,[1]])
        self.qwer(self.A_TA, 1)
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
        print(f"EIGENVECTORS: {self.eigenvectors}")
        print(self.A_TA)
        print(self.to_print)
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