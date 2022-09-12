"""
Write a Python program to check a triangle is equilateral,isosceles orscalene.
Note : An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
ExpectedOutput:Input lengths of the triangle sides:
x: 6
y: 8
z: 12
Scalene triangle
"""
x, y, z = map(float, input("Input lengths of the triangle sides: " ).split())
if x==y==z:
    print("An equilateral triangle")
elif x==y or x==z or y==z:
    print("An isosceles triangle")
else:
    print("A scalene triangle")
