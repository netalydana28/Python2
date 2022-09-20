"""
Calculate √x-√y, if x and y are inputs. (0.25 points)
SAMPLE:
x = 1
y = 4
Output: plz enter valid numbers
x = 4
y = 1
Output: 1,732
"""
import math

x = int(input())
y = int(input())

try: 
    math.sqrt(x-math.sqrt(y))
except: 
    print("plz enter valid numbers")
else:
    print(math.sqrt(x-math.sqrt(y)))
