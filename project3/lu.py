import numpy as np
from numpy.linalg import *

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
        P = np.zeros((n,n))
        np.fill_diagonal(P,1)    
        for i in range(n):
            for j in range(i+1, n):
                if U[i][i]!=0:
                    ratio = (U[j][i]/U[i][i])
                    L[j][i]=np.around(ratio, decimals=2)
                    U[j]=np.around(U[j]- ratio * U[i],decimals=2)
                    #print(self.A)
                else:
                    w=tuple(U[i])
                    w_p=tuple(P[i])
                    self.U=self.swap(U,i,w)
                    self.P=self.swap(P,i,w_p)
        d=np.diag(U)
        np.fill_diagonal(D,d)
        
        self.L=L
        self.U=U
        self.D=D
        




a=np.array([[0,0,3],
        [1,0,1],
        [4,0,1]], dtype=float)

d2=Decompositions2(a)
d2.LU()
