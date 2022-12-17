import numpy as np

#a=np.array([[2.2,1,0.5,2],
#            [1,1.3,2,1],
#            [0.5,2,0.5,1.6],
#            [2,1,1.6,2]])
"""
a=np.array([[2,1,1],
            [1,2.5,1],
            [1,1,3]])
"""
#a = np.array([[1, 1, 0], [1, 1, 0], [0, 0, 1]], dtype = float)
a = np.array([[6, 7, 22], [7, 13, 27], [22, 27, 91]], dtype = float)


n=len(a)
e=np.zeros((n,n))
np.fill_diagonal(e,1)
coef_pol=list()
coef=list()
a_inv=np.zeros((n,n)) 
b_inv=np.zeros((n,n)) 
b_list=list()
y=np.zeros((n,1))
y0=(e[:,[0]])
y_list=list()
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
    return v
def inverse(b_list,coef_pol):
    for i in range(n):
        a_inv[i]=b_list[n-2][i]/coef_pol[n-1]
    return a_inv
def eig2(root,y0,k):
  
    y=root*y0+b_list[k-1][:,[0]]
    #print(y)
    y_list.append(y)
    if k==n-1:
        return y_list[n-2]
    k=k+1

    return eig2(root,y,k)
def eigenvector(roots):
    x_ev=list()
    #x_ev3=list(size=len(roots))
    for i in range(len(roots)):
        x_ev.append(eig2(roots[i],y0,1))
        y_list.clear()
    x_ev3=list()
    
    for i in range(len(x_ev)):
       # x_ev4.clear()
        x_ev4=list()
        for j in range(len(x_ev)):
            x_ev4.append(x_ev[j][i][0])
        x_ev3.append(x_ev4)        
    x_ev2=np.array(x_ev3)
    #print(x_ev2)
    print(x_ev2)
    print(ortogonalize(x_ev2))
def qwer(x,k):
    global a
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
    #print(b)


    k=k+1  

    f=np.matmul(a,b)

    if k==len(a)+1:
        if n%2!=0:
            coef.append(-1)
            for i in range(n):
                coef.append(coef_pol[i])
        if n%2==0:
            coef.append(1)
            for i in range(n):
                coef.append(-coef_pol[i])
        roots=np.roots(coef)
        print(roots)
        roots.sort()
        #print(roots)
        eigenvector(roots)
        #print(b_list[1][:,[0]])
        #print(inverse(b_list, coef_pol))
        return True
    return qwer(f,k)


print(qwer(a,1))