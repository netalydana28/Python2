#Given the coefficients a, b, c of the equation ax2 + bx + c = 0. Find a solution. Please consider exceptions, like no roots

a, b, c = map(int, input().split())

def solution(a, b, c):
    D = pow(b, 2) - 4*a*c
    if D<0:
        return "No solution in real numbers"
    else:
        x1 = (-b-pow(D, 0.5))/2*a
        x2 = (-b+pow(D, 0.5))/2*a
        ans = list()
        ans.append(x1)
        ans.append(x2)
        return ans
    
print(solution(a, b, c))
