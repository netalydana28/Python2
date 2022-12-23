import numpy as np 
import math
#import re
#import pr3
#import copy
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


m = np.array([[8, 0, 2], [0, 4, 0], [2, 0, 5]], dtype = float)
f=functions(m)
print(f.qwer(m, 1))