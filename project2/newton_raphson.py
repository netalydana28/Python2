def func( x ):
    return -x**3 + 3*x**2 - 2*x
# Derivative of the above function
# which is 3*x^x - 2*x
def derivFunc( x ):
    return -3*x**2 + 6*x -2

    # Function to find the root
def newtonRaphson( x ):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
    print("The value of the root is : ", "%.4f"% x)
# Driver program to test above
x0 = 0.75 # Initial values assumed
newtonRaphson(x0)
# This code is contributed by "Sharad_Bhardwaj"