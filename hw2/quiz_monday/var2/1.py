"""
Given the leg (катеты) of a right triangle (прямоугольный). Find the area, perimeter and hypotenuse of the triangle. (0.25 point)
SAMPLE:
a = 3, b = 4
c = 5 S = 6 P = 12
"""
a = int(input())
b = int(input())

c = pow((pow(a, 2)+ pow(b, 2)), 0.5)
A = (a*b)/2
P = a+b+c
print(f"c = {c} \nA = {A} \nP = {P}")