def func( x ):
    return -x**3.0 + 3.0*x**2.0 - 2.0*x

def central_difference(x0, h):
    return round((func(x0 + h) - func(x0 - h))/ 2*h)


def newtonRaphson( x ):
    h = func(x) / central_difference(x, 0.0001)
    while abs(h) >= 0.0000001:
        h = func(x)/central_difference(x, 0.001)
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
    return round(x)

x0 = 0.75 # my initial guess
print(newtonRaphson(x0))