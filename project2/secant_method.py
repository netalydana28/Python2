
def f(x):
    f = (1-x)**3 -1 + x
    return f
 
def secant(x1, x2, E):
    n = 0; xm = 0; x0 = 0; c = 0
    if (f(x1) * f(x2) < 0):
        while True:
             
            x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))
            print(x0)
 
            c = f(x1) * f(x0)
 
            x1 = x2
            x2 = x0
            n += 1
 
            if (c == 0):
                break

            xm = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))
             
            if(abs(xm - x0) < E):
                break
         
        print("Root of the given equation =", round(x0))
        print("No. of iterations = ", n)
         
    else:
        pass



secant(-1, 5, 0.0001)

"""    
dx = 4/10

x1 = -1 - dx
E = 0.0001
x2 = x1 + dx
while x2 != 4 + dx:
    
    secant(x1, x2, E)
    x1 = x2
    x2 = x1 + dx


    def secant(self, x1, x2, E):
        n = 0; xm = 0; x0 = 0; c = 0
        if (self.f(x1) * self.f(x2) < 0):
            while True:
                
                x0 = ((x1 * self.f(x2) - x2 * self.f(x1)) / (self.f(x2) - self.f(x1)))
    
                c = self.f(x1) * self.f(x0)
    
                x1 = x2
                x2 = x0
                n += 1
    
                if (c == 0):
                    break
                xm = ((x1 * self.f(x2) - x2 * self.f(x1)) / (self.f(x2) - self.f(x1)))
                
                if(abs(xm - x0) < E):
                    break

            self.eigenvalues.append(round(x0))
            
            print("Root of the given equation =", round(x0))
            print("No. of iterations = ", n)
            
        else:
            pass
"""