from tkinter import *
import numpy as np 
import sympy as sym
import math
import re

class online_calculator:

    window = Tk()
    frame = Frame()

    def __init__(self):
        self.window.title("SVD decomposition")
        self.window.geometry("1536x864")

    def Z5(n):
        pass

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
    
    def clear_page(self):
        for i in range(len(self.entry_boxes)):
            self.entry_boxes[i].delete(0, END)
        self.to_print = ""
        self.text_widget.delete(1.0, END)

    
    def main_frame(self):
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
        self.clear = Button(self.frame, text = "Clear", font=("Arial Bold", 12), command = self.clear_page).grid(row = 6, column = 1, pady =3)

        self.window.mainloop()

    def solve_square_eq(self, a, b, c):
        D = b**2 - 4 * a * c
        x1 = (-b + D**0.5)/2*a
        self.eigenvalues.append(x1)
        x2 = (-b - D**0.5)/2*a
        self.eigenvalues.append(x2)

    def gorner(self, x0, a, b, c, d):
        if a == 0:
            self.eigenvalues.pop(0)
            self.solve_square_eq(b, c, d)
        else:
            asq = a
            bsq = x0 * a + b
            csq = x0 * bsq + c
            if x0 * csq + d == 0:
                self.solve_square_eq(asq, bsq, csq)
            else:
                print("ERROR")

    def newtonRaphson(self, x):
        h = self.f(x) / self.df(x)

        while abs(h) >= 0.0000001:
            h = self.f(x)/self.df(x)
            # x(i+1) = x(i) - f(x) / f'(x)
            x = x - h

        return round(x)

    def eigenvalues_find(self):
        if len(self.A_TA) == 2:
            a = 0
            b = -1
            c = sum(np.diag(self.A_TA))
            d = -1 * self.det(self.A_TA)

            ch_pol = f"{b}x² + ({c})x + ({d})"
        elif len(self.A_TA) == 3:
            a = -1 
            b = sum(np.diag(self.A_TA))
            c = -1 * sum([self.det(self.A_TA[:2, :2]), self.det(self.A_TA[1:3, 1:3]), self.det(self.A_TA[::2, ::2])])
            d = self.det(self.A_TA)

            ch_pol = f"{a}x³ + ({b})x² + ({c})x + ({d})"
           
        self.to_print += f"Characteristic polynomial: {ch_pol}\n\n"

        x = sym.Symbol('x') # variable of eigenvalue
        det = 1 
        for i in range(len(self.A_TA)):
            det *= self.A_TA[i][i] - x

        if len(self.A_TA) == 2:
            det -= math.prod(np.diag(np.fliplr(self.A_TA)))
        elif len(self.A_TA) == 3:
            det += (math.prod([self.A_TA[2][0], self.A_TA[0][1], self.A_TA[1][2]]) + math.prod([self.A_TA[1][0], self.A_TA[2][1], self.A_TA[0][2]]))
            det -= (math.prod([self.A_TA[1][1] - x, self.A_TA[0][2], self.A_TA[2][0]]) + math.prod([self.A_TA[0][1], self.A_TA[1][0], self.A_TA[2][2]-x]) + math.prod([self.A_TA[0][0]-x, self.A_TA[2][1], self.A_TA[1][2]]))
        det = sym.expand(det)
        #self.to_print += f"Characteristic polynomial: {det}\n\n"
        self.f = lambda y: det.subs(x, y) 
        self.df = lambda y: sym.diff(det, x).subs(x, y)
        self.eigenvalues = list()

        x0 = 0.75 #Initial guess
        self.eigenvalues.append(float(self.newtonRaphson(x0)))
        """
        patterns = ["\+{1}\s?[0-9]*\.*[0-9]*\**x\*\*3|-{1}\s?[0-9]*\.*[0-9]*\**x\*\*3", "\+{1}\s?[0-9]*\.*[0-9]*\**x\*\*2|-{1}\s?[0-9]*\.*[0-9]*\**x\*\*2", "\+{1}\s?[0-9]*\.*[0-9]*\**x{1}|-{1}\s?[0-9]*\.*[0-9]*\**x{1}", "-{1}\s?[0-9]+\.*[0-9]*$|\+{1}\s?[0-9]+\.*[0-9]*$"]
        coeffs = list()
    
        for i in range(len(patterns)):
            temp = re.findall(patterns[i], str(det))
            
            if len(temp) != 0:
                num_existence = re.findall("\+{1}\s?[0-9]+\.*[0-9]*|-{1}\s?[0-9]+\.*[0-9]*", temp[len(temp)-1])
                if len(num_existence) == 0:
                    minus_existens = re.findall("-", temp[len(temp)-1])
                    to_append = -1.0 if len(minus_existens) !=0 else 1.0
                    coeffs.append(to_append)
                else:
                    num_existence = re.findall("-*\s?[0-9]+\.*[0-9]*$", num_existence[0])
                    num_existence = re.sub("\s", "", num_existence[0])
                    coeffs.append(float((num_existence)))    
            else:
                coeffs.append(0.0)       
    
        a, b, c, d = coeffs[0], coeffs[1], coeffs[2], coeffs[3]
        """
        self.gorner(self.eigenvalues[0], a, b, c, d)
        print(f"EIGVALUES: {self.eigenvalues}")
        self.eigenvalues.sort(reverse = True) 
        print(f"EIGVALUES: {self.eigenvalues}")

    def D_find(self):
        self.to_print = f"Your matrix:\n {self.A}\n\n"
        #Find A_T * A
        self.A_TA = np.matmul(self.A.T, self.A)
        self.to_print += f"A^T * A:\n {self.A_TA}\n\n"
        
        #Find eigenvalues of A_TA
        self.eigenvalues_find()
        self.D = np.zeros((len(self.A_TA), len(self.A_TA[0])) , dtype = float)
        self.to_print += f"Eigenvalues of A^T*A: {self.eigenvalues}\n\n"

        self.sigmas = list()
        for i in range(len(self.eigenvalues)):
            self.D[i][i] = self.eigenvalues[i]**0.5
            if self.eigenvalues[i]**0.5 != 0:
                self.sigmas.append(self.eigenvalues[i]**0.5)

        #√

        self.to_print += f" D matrix:\n {self.D}\n\n"

    def det(self, A):
        det = 0
        det += math.prod(np.diag(A))
        det -= math.prod(np.diag(np.fliplr(A)))
        if len(A) == 3:
            det += (math.prod([A[2][0], A[0][1], A[1][2]]) + math.prod([A[1][0], A[2][1], A[0][2]]))
            det -= (math.prod([A[0][1], A[1][0], A[2][2]]) + math.prod([A[0][0], A[2][1], A[1][2]]))
            return det
        return det

    def adjoint(self):
        temp = list()
        if len(self.A_TA) == 2:
            temp.append(self.A_TA[1][1])
            temp.append(-1 * self.A_TA[1][0] )
            temp.append(-1 * self.A_TA[0][1] )
            temp.append(self.A_TA[0][0] )
            return np.array(np.array(temp).reshape(2, 2), dtype = float)
        elif len(self.A_TA) == 3:
            temp.append(self.det(self.A_TA[1:3, 1:3]))
            temp.append(-1 *self.det(self.A_TA[::2, ::2]))
            temp.append(self.det(self.A_TA[1:3, :2]))
            temp.append(-1*self.det(self.A_TA[:3:2, 1:3]))
            temp.append(self.det(self.A_TA[:3:2, :3:2]))
            temp.append(-1 * self.det(self.A_TA[:3:2, :2]))
            temp.append(self.det(self.A_TA[:2, 1:3]))
            temp.append(-1 * self.det(self.A_TA[:2, :3:2]))
            temp.append(self.det(self.A_TA[:2, :2]))
            return np.array(np.array(temp).reshape(3, 3), dtype = float)


    def eigenvectors_find(self):
        self.eigenvectors = list()
        diag = list(np.diag(self.A_TA))
        for i in range(len(self.eigenvalues)):
            if len(self.A_TA) == 2:
                temp_diag = np.array(list(np.diag(self.A_TA)), dtype = float) -  np.array([self.eigenvalues[i], self.eigenvalues[i]], dtype = float)
            elif len(self.A_TA) == 3:
                temp_diag = np.array(list(np.diag(self.A_TA)), dtype = float) -  np.array([self.eigenvalues[i], self.eigenvalues[i], self.eigenvalues[i]], dtype = float)

            for j in range(len(self.A_TA)):
                self.A_TA[j][j] = temp_diag[j] 

            if self.det(self.A_TA) == 0:
                for j in range(len(self.A_TA)):
                    self.A_TA[j][j] = diag[j]
                w, v = np.linalg.eig(self.A_TA)
                self.eigenvectors.append(v[i]) 
                
            else:
                inverse = (1 / self.det(self.A_TA) ) * self.adjoint()
                vector = np.dot(inverse, np.zeros(len(self.A_TA), dtype = float))
                self.eigenvectors.append(vector)

            for j in range(len(self.A_TA)):
                self.A_TA[j][j] = diag[j]
        self.to_print += f"Eigenvectors: {self.eigenvectors}\n\n"
        self.eigenvectors = np.array(self.eigenvectors, dtype = float)

    def ortogonalize(self):
        k = list()
        for i in range(1, len(self.eigenvectors)):
            temp = np.dot(self.eigenvectors[i], self.eigenvectors[i-1])/np.dot(self.eigenvectors[i-1], self.eigenvectors[i-1])
            k.append(temp)

            for j in range(len(k)):
                self.eigenvectors[i] -= k[j] * self.eigenvectors[j]

    def normalize(self, v):
        length_v = 0
        for i in range(len(v)):
            length_v += v[i]**2

        length_v = length_v ** 0.5
        for i in range(len(v)):
            v[i] = v[i]/length_v

    def length(self, v):
        length = 0
        for i in range(len(v)):
            length += v[i]**2
        return round(length**0.5)

    def C_find(self):
        self.eigenvectors_find()
        
        if np.dot(self.eigenvectors[0], self.eigenvectors[1]) != 0:
            if len(self.A_TA) == 2:
                pass
            elif len(self.A_TA) == 3:
                if np.dot(self.eigenvectors[1], self.eigenvectors[2]) != 0 or np.dot(self.eigenvectors[0], self.eigenvectors[2]) != 0:
                    self.ortogonalize()

        for i in range(len(self.eigenvectors)):
            if self.length(self.eigenvectors[i]) != 0:
                self.normalize(self.eigenvectors[i])

        self.C = self.eigenvectors.T
        self.to_print += f"C_T: {self.C}\n\n"

    def B_find(self):
        temp = list()
        for i in range(len(self.sigmas)):
            a = 1/self.sigmas[i]
            matrix = a * self.A
            vector = np.matmul(matrix, self.eigenvectors[i])
            temp.append(vector)

        self.B = np.array(temp, dtype = float)
        self.to_print += f"B: {self.B}\n\n"

    def SVD(self):
        self.D_find()
        self.C_find()
        self.B_find()
        self.to_print += f"SVD:\n {self.B} {self.D} {self.C}\n"

        print(self.to_print)

        self.scroll_bar = Scrollbar(self.frame, orient = "vertical") # Create a scroll bar
        self.text_widget = Text(self.frame, yscrollcommand=self.scroll_bar.set) # Create a text_widget 
        self.scroll_bar.grid(row = 7, column = 4, rowspan = 4) # Pack the scroll bar
        self.scroll_bar.config(command=self.text_widget.yview) # Attach the scrollbar with the text widget
        self.text_widget.grid(row = 7, column = 0, rowspan = 4, columnspan = 4) # Pack the text widget
        self.text_widget.insert(END, self.to_print)# Insert text into the text widget

if __name__ == "__main__":
    start = online_calculator()
    start.main_frame()