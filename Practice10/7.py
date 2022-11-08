"""
Sudoku Parser 
Create a class Sudoku that takes a string as an argument. 
The string will contain the numbers of a regular 9x9 sudoku board left to right and top to bottom, with zeros filling up the empty cells. 

Methods 

get_row(n): will return the row in position n. 
get_col(n): will return the column in position n. 
get_sqr([n, m]): will return the square in position n if only one argument is given, and the square to which the cell in position (n, m) belongs to if two arguments are given. 
"""

# 417950030000000700060007000050009106800600000000003400900005000000430000200701580

import math
import numpy as np

sudoku_string = input("Enter your string: ")

class Sudoku:

    def __init__(self, sudoku_string):
        temp_1 = 0
        temp_2 = 9
        temp_list = list()
        for i in range(9):
            line = sudoku_string[temp_1: temp_2]
            line_list = list()
            for i in range(9):
                line_list.append(line[i])
            temp_1 +=9
            temp_2 +=9
            temp_list.append(line_list)
        self.arr = np.array(temp_list)

    def get_arr(self):
        return self.arr

    def get_row(self, n):
        return self.arr[n]

    def get_col(self, n):
        return self.arr.T[n]

    def get_sqr(self, *n):
        temp_dict = { 0 : 1, 1 : 4, 2 : 7 }
        temp = math.floor(n[0]/3)
        row = temp_dict[temp]
        if len(n) == 1:
            temp = n[0] % 3
            col = temp_dict[temp]
            temp = list()

            for i in range(row - 1, row + 2):
                for j in range(col -1, col + 2):
                    temp.append(self.arr[i][j])

            return temp
        if len(n) == 2:
            temp = math.floor(n[1]/3)
            col = temp_dict[temp]
            temp = list()

            for i in range(row - 1, row + 2):
                for j in range(col -1, col + 2):
                    temp.append(self.arr[i][j])

            return temp
            
game = Sudoku(sudoku_string)
#print(game.get_arr())
print(game.get_row(0))
print(game.get_col(8))
print(game.get_sqr(1))
print(game.get_sqr(1, 8))
print(game.get_sqr(8, 3))