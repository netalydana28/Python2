"""
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the
distance from current position after a sequence of movement and original point. If the
distance is a float, then just print the nearest integer. (1 point)
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be: 2
"""

x0, y0, x1, y1 = 0, 0, 0, 0
UP = eval(input("UP "))
DOWN = eval(input("DOWN "))
LEFT = eval(input("LEFT "))
RIGHT = eval(input("RIGHT "))

def distance(UP, DOWN, LEFT, RIGHT):
    x1 = x0 + RIGHT - LEFT
    y1 = y0 + UP - DOWN
    return round(pow((pow(x1, 2)+pow(y1, 2)), 0.5))

print(distance(UP, DOWN, LEFT, RIGHT))