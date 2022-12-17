import numpy as np
from fractions import Fraction
import copy



'''mat=np.array([[5,-4,4],
            [2,1,2],
            [2,1,3]],dtype=float) '''



mat=np.array([[7,-4,4],
            [2,3,2],
            [2,0,5]],dtype=float)
#print(m1.ref())
n=len(mat)
e=np.zeros((n,n),dtype=float)
np.fill_diagonal(e,1) 

coef_pol=list()
coef=list()
a_inv=np.zeros((n,n)) 
b_inv=np.zeros((n,n)) 
b_list=list()
y=np.zeros((n,1))
y0=(e[:,[1]])
y_list=list()

def is_in_ref(mat):
    lead_entry = [] 
    
    for i in range(n):
        for j in range(n):
            if mat[i, j] != 0:
                lead_entry.append(j)
                break
    a = True
    for i in range(1, len(lead_entry)):
        if lead_entry[i] <= lead_entry[i-1] :
            a = False
        #print(lead_entry)
    return a
def swap_rows(a,i1, i2):
    x = []
    for i in range(n):
        row = []
        if i == i1:
            for j in range(n):
                row.append(a[i2, j])
        elif i == i2:
            for j in range(n):
                row.append(a[i1, j])
        else:
            for j in range(n):
                row.append(a[i, j])
        x.append(row)
    a = np.asarray(x)
    return a
def ref(mat,l):
    x = mat
    s = 0
    e=np.zeros((n,n))
    np.fill_diagonal(e,1)
    #print(x)
    if not is_in_ref(x):
            #print(x)
        for j in range(n):
                #print('------', j, '----------')
            nul_col = True
            for i in range(s, n):
                    #print('6666666',x.value[s,j] == 0., x.value[s,j])
                if x[s,j] == 0:
                    i1 = s
                    if x[i,j] != 0:
                        nul_col = False
                        i2 = i
                        x=swap_rows(x,i1, i2)
                        e=swap_rows(e,i1, i2)
                        #print(e)
                        if is_in_ref(x):
                                #print(x)
                            for k in range(n):
                                if any(x[k])==0:
                                #    print(x[k])
                                    return e[l+k]
                        else:
                            break
                else:
                    nul_col = False
                    break
            if not nul_col:
                for k in range(s+1, n):
                    ratio = x[k,j]/x[s,j]
                    x[k, :] = np.around(x[k, :] - ratio * x[s, :],decimals=1)
                    e[k, :] = e[k, :] - ratio * e[s, :]
                    #print(x)
                    if is_in_ref(x):
                        for m in range(n):
                            if any(x[m])==0:  
                                return e[m+l]
                s+=1
    print(x)
    for i in range(n):
        if any(x[i])==0:
            return e[i+l]

def ortogonalize(x_ev2):
    x_ev=np.transpose(x_ev2)
    #x_ev2=list(size=len(x_ev))
    k = list()
    for i in range(1, len(x_ev)):
        for j in range(i):
            temp = np.dot(x_ev[i], x_ev[j])/np.dot(x_ev[j], x_ev[j])
            k.append(temp)
            #print(type(x_ev))
        
        #for l in range(len(x_ev[i])):
        for m in range(len(k)):
        #        print(l)
            x_ev[i] -= k[m] * x_ev[m]
        k.clear()
    return normalize(np.transpose(x_ev))
def normalize(v):
    length_v = 0
    for i in range(len(v)):
        length_v += v[i]**2
    length_v = length_v ** 0.5

    for k in range(len(v)):
        v[k] = v[k]/length_v    
    print(v) 
def inverse(b_list,coef_pol):
    for i in range(n):
        a_inv[i]=b_list[n-2][i]/coef_pol[n-1]
    return a_inv
def eigenvector(roots):
    eiv=list()
    for i in range(len(roots)):
        if i-1!=-1 and roots[i]==roots[i-1]:
            b=np.subtract(mat,(roots[i])*e)
            #print(mat,b)
            eiv.append(ref(b.transpose(),1))
        else:
            b=np.subtract(mat,(roots[i])*e)
            #print(b)
            eiv.append(ref(b.transpose(),0))
    print((np.array(eiv).transpose()))
def qwer(x,k):
    #global a
    b=np.zeros((n,n))
    p0=0
    diag=np.diagonal(x)
    for i in range(n):
        p0=p0+diag[i]
    p=(1/(k))*p0
    coef_pol.append(p)
    for j in range(n):
        b[j]=x[j]-p*e[j]
    b_list.append(b)
    k=k+1  
    f=np.matmul(mat,b)
    if k==len(mat)+1:
        if n%2!=0:
            coef.append(-1)
            for i in range(n):
                coef.append(coef_pol[i])
        if n%2==0:
            coef.append(1)
            for i in range(n):
                coef.append(-coef_pol[i])
        roots=np.around(np.roots(coef),decimals=2)
        roots.sort()
        print(roots)
        eigenvector(roots)
        return True
    return qwer(f,k)


print(qwer(mat,1))
