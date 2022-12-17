import numpy as np

a=np.array([[2.2,1,0.5,2],
            [1,1.3,2,1],
            [0.5,2,0.5,1.6],
            [2,1,1.6,2]])
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
def ortogonalize(x_ev):
    k = list()
    for i in range(1, len(x_ev)):
        temp = np.dot(x_ev[i], x_ev[i-1])/np.dot(x_ev[i-1], x_ev[i-1])
        k.append(temp)

    for j in range(len(k)):
        x_ev[i] -= k[j] * x_ev[j]
    return x_ev
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
    for i in range(len(roots)):
        x_ev.append(eig2(roots[i],y0,1))
        y_list.clear()
    x_ev2=np.array(x_ev)
    print(x_ev2)
    #print(ortogonalize(x_ev2))
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
        roots.sort()
        #print(roots)
        eigenvector(roots)
        #print(b_list[1][:,[0]])
        #print(inverse(b_list, coef_pol))
        return True
    return qwer(f,k)


print(qwer(a,1))