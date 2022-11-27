from tkinter import *
import numpy as np 
import sympy as sym
import math

class online_calculator:

    window = Tk()
    frame = Frame()

    def __init__(self):
        self.window.title("SVD decomposition")
        self.window.geometry("1536x864")

    def change_rows(self):
        self.row_num = self.row.get()
        self.column_num = self.column.get()

        if self.row_num == "3":
            self.A20 = Entry(self.frame)
            self.A20.grid(row = 5, column = 1, pady = 3)
            self.A21 = Entry(self.frame)
            self.A21.grid(row = 5, column = 2, pady = 3)
            self.entry_boxes.append(self.A20)
            self.entry_boxes.append(self.A21)
        elif self.row_num == "2": 
            try: a = self.A20 in self.entry_boxes and self.A21 in self.entry_boxes
            except: pass
            else:
                if self.A20 in self.entry_boxes and self.A21 in self.entry_boxes:
                    self.entry_boxes.remove(self.A20)
                    self.entry_boxes.remove(self.A21)
                    self.A20.destroy()
                    self.A21.destroy()
            
            try: a = self.A22 in self.entry_boxes
            except: pass
            else:
                if self.A22 in self.entry_boxes:
                    self.entry_boxes.remove(self.A22)
                    self.A22.destroy()

        if self.row_num == "3" and self.column_num == "3":
            self.A22 = Entry(self.frame)
            self.A22.grid(row = 5, column = 3, pady = 3)  
            self.entry_boxes.append(self.A22)
        
    def change_columns(self):
        self.row_num = self.row.get()
        self.column_num = self.column.get()

        if self.column_num == "3":
            self.A02 = Entry(self.frame)
            self.A02.grid(row = 3, column = 3, pady = 3)
            self.A12 = Entry(self.frame)
            self.A12.grid(row = 4, column = 3, pady = 3)
            self.entry_boxes.insert(2, self.A02)
            self.entry_boxes.insert(5, self.A12)
        elif self.column_num == "2": 
            try: a = self.A02 in self.entry_boxes and self.A12 in self.entry_boxes
            except: pass
            else:
                if self.A02 in self.entry_boxes and self.A12 in self.entry_boxes:
                    self.entry_boxes.remove(self.A02)
                    self.entry_boxes.remove(self.A12)
                    self.A02.destroy()
                    self.A12.destroy()
            
            try: a = self.A22 in self.entry_boxes
            except: pass
            else:
                if self.A22 in self.entry_boxes:
                    self.entry_boxes.remove(self.A22)
                    self.A22.destroy()

        if self.row_num == "3" and self.column_num == "3":
            self.A22 = Entry(self.frame)
            self.A22.grid(row = 5, column = 3, pady = 3)  
            self.entry_boxes.append(self.A22)

    def get_matrix(self):
        self.row_num = self.row.get()
        self.column_num = self.column.get()
        matrix = list()
        for i in range(len(self.entry_boxes)):
            matrix.append(self.entry_boxes[i].get())
        self.A = np.array(np.array(matrix).reshape(int(self.row_num), int(self.column_num)), dtype = float)
        self.SVD()
    
    def main_frame(self, event =''):
        self.frame = Frame(self.window)
        self.frame.pack() 

        #Labels
        title_label = Label(self.frame, text = "SINGULAR VALUE DECOMPOSITION CALCULATOR", font=("Arial Bold", 20))
        size_label = Label(self.frame, text = "Size of the matrix: ", font=("Arial Bold", 16))
        matrix_label = Label(self.frame, text = "Matrix: ", font=("Arial Bold", 16))

        Label(self.frame).grid(row=0, column=0, padx=280, pady=60)
        title_label.grid(row=1, column=0, columns = 4, pady = 3)
        size_label.grid(row = 2, column = 0, pady = 3)
        matrix_label.grid(row = 3, column = 0, pady = 3)

        #SpinBoxes
        self.row = Spinbox(self.frame, from_ = 2, to = 3, command = self.change_rows )
        self.column = Spinbox(self.frame, from_ = 2, to = 3, command=self.change_columns)
        self.row.grid(row = 2, column = 1, pady = 3)
        self.column.grid(row = 2, column = 2, pady = 3)

        #Entry
        self.A00 = Entry(self.frame)
        self.A00.grid(row = 3, column = 1, pady = 3)
        self.A01 = Entry(self.frame)
        self.A01.grid(row = 3, column = 2, pady = 3)
        self.A10 = Entry(self.frame)
        self.A10.grid(row = 4, column = 1, pady = 3)
        self.A11 = Entry(self.frame)
        self.A11.grid(row = 4, column = 2, pady = 3)
        self.entry_boxes = [self.A00, self.A01, self.A10, self.A11]

        #Buttons 
        self.calculate = Button(self.frame, text = "Calculate", font=("Arial Bold", 12), command = self.get_matrix).grid(row = 6, column = 0, pady =3)

        self.window.mainloop()

    def eigenvalues(self):
        x = sym.Symbol('x') # variable of eigenvalue
        det = 1 
        for i in range(len(self.A_TA)):
            det *= self.A_TA[i][i] - x
        
        if len(self.A_TA) == 2:
            det -= math.prod(np.diag(np.fliplr(self.A_TA)))
        elif len(self.A_TA) == 3:
            det += (math.prod([self.A_TA[2][0], self.A_TA[0][1], self.A_TA[1][2]]) + math.prod([self.A_TA[1][0], self.A_TA[2][1], self.A_TA[0][2]]))
            det -= (math.prod([self.A_TA[1][1] - x, self.A_TA[0][2], self.A_TA[2][0]]) + math.prod([self.A_TA[0][1], self.A_TA[1][0], self.A_TA[2][2]-x]) + math.prod([self.A_TA[0][0]-x, self.A_TA[2][1], self.A_TA[1][2]]))
        self.to_print += f"Characteristic polynomial: {det}\n\n"
        self.eigenvalues = list(sym.solveset(sym.expand(det), x))
        self.eigenvalues.sort(key=lambda x: x == 0) #transfer zeros in the end of the list

    def D(self):
        self.to_print = f"Your matrix:\n {self.A}\n\n"
        #Find A_T * A
        self.A_TA = np.matmul(self.A.T, self.A)
        self.to_print += f"A^T * A:\n {self.A_TA}\n\n"

        #Find eigenvalues of A_TA
        self.eigenvalues()
        self.D = np.zeros((len(self.A_TA), len(self.A_TA[0])) , dtype = float)
        self.to_print += f"Eigenvalues of A^T*A: {self.eigenvalues}\n\n"
        for i in range(len(self.eigenvalues)):
            self.D[i][i] = self.eigenvalues[i]**0.5

        self.to_print += f" D matrix:\n {self.D}\n\n"

    def det(self, A):
        det = 0
        det += math.prod(np.diag(A))
        det -= math.prod(np.diag(np.fliplr(A)))
        if len(A) == 3:
            det += (math.prod([A[2][0], A[0][1], A[1][2]]) + math.prod([A[1][0], A[2][1], A[0][2]]))
            det -= (math.prod([A[1][1], A[0][2], A[2][0]]) + math.prod([A[0][1], A[1][0], A[2][2]]) + math.prod([A[0][0], A[2][1], A[1][2]]))
            return det
        return det

    def eigenvectors(self):
        diag = list(np.diag(self.A_TA))
        D = list()
        for i in range(len(self.eigenvalues)):
            for j in range(len(self.A_TA)):
                self.A_TA[j][j] = self.A_TA[j][j] - self.eigenvalues[i]

            x = sym.Symbol('x')
            y = sym.Symbol('y')
            z = sym.Symbol('z')
            to_solve = np.matmul(self.A_TA, [x, y, z])

            
            D.append(self.det(self.A_TA))

            for j in range(len(self.A_TA)):
                self.A_TA[j][j] = diag[j]

    def SVD(self):
        self.D()
        self.eigenvectors()
        print(self.to_print)
        
        scroll_bar = Scrollbar(self.frame, orient = "vertical") # Create a scroll bar
        text_widget = Text(self.frame, yscrollcommand=scroll_bar.set) # Create a text_widget 
        scroll_bar.grid(row = 7, column = 4, rowspan = 4) # Pack the scroll bar
        self.to_print += "1\n1\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n"
        scroll_bar.config(command=text_widget.yview) # Attach the scrollbar with the text widget
        text_widget.grid(row = 7, column = 0, rowspan = 4, columnspan = 4) # Pack the text widget
        text_widget.insert(END, self.to_print)# Insert text into the text widget

if __name__ == "__main__":
    start = online_calculator()
    start.main_frame()