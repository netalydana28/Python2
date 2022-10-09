from tkinter import *
from math import *
from sympy import *
import re

calc = Tk()
calc.geometry('280x240')
calc.title('Calculator')
calc['bg'] = 'white' #coloring background white
to_print = "" # I've created two variables equation that will be printed
to_solve = "" #equation that will be taken by eval function 

def show(to_print): #funtion for printing solution on the screen 
    output = Label(calc, text = to_print, width = 39, height = 2)
    output['bg']= "white"
    output.grid(row = 0, column = 0, columnspan = 7)

#functions for th buttons
def equal():
    global to_print, to_solve 
    print(to_solve) # i observe what expression eval function gets is
    try: eval(to_solve)
    except: print(show("Error"))
    else:
        tmp = int(eval(to_solve)) if eval(to_solve) - int(eval(to_solve)) == 0.0 else eval(to_solve) # to avoid 4.0 
        show(tmp)
        to_print= str(tmp)
        to_solve = to_print
def plus():
    global to_print, to_solve
    if not len(to_print) == 0 and (to_print[len(to_print)-1].isdigit() or to_print[len(to_print)-1] == ")" or to_print[len(to_print)-1] == "e"):
        to_print += " + " 
        to_solve += " + "
        show(to_print)
    else:
        pass
def minus():
    global to_print, to_solve
    to_print += " - " 
    to_solve += " - "
    show(to_print)
def product():
    global to_print, to_solve
    if not len(to_print) == 0 and (to_print[len(to_print)-1].isdigit() or to_print[len(to_print)-1] == ")" or to_print[len(to_print)-1] == "e"): #to avoid incorrect placement
        to_print += " x " 
        to_solve += " * "
        show(to_print)
    else:
        pass
def division():
    global to_print, to_solve
    if not len(to_print) == 0 and (to_print[len(to_print)-1].isdigit() or to_print[len(to_print)-1] == ")" or to_print[len(to_print)-1] == "e"):
        to_print += " : " 
        to_solve += " / "
        show(to_print)
    elif to_print[len(to_print)-1] == "π":
        to_print += "/" 
        to_solve += " / "
        show(to_print)       
    else:
        pass
def delete(): #deletes evverything
    global to_print, to_solve
    to_print = ""
    to_solve = "" 
    show(to_print)
def zero():
    global to_print, to_solve
    to_print += "0"
    to_solve += "0" 
    show(to_print)
def two():
    global to_print, to_solve
    to_print += "2"
    to_solve += "2" 
    show(to_print)
def one():
    global to_print, to_solve
    to_print += "1"
    to_solve += "1" 
    show(to_print)
def three():
    global to_print, to_solve 
    to_print += "3"
    to_solve += "3" 
    show(to_print)    
def four(): 
    global to_print, to_solve
    to_print += "4"
    to_solve += "4" 
    show(to_print)
def five(): 
    global to_print, to_solve    
    to_print += "5"
    to_solve += "5" 
    show(to_print)
def six(): 
    global to_print, to_solve    
    to_print += "6"
    to_solve += "6" 
    show(to_print)
def seven(): 
    global to_print, to_solve    
    to_print += "7"
    to_solve += "7" 
    show(to_print)
def eight():
    global to_print, to_solve
    to_print += "8"
    to_solve += "8" 
    show(to_print)
def nine():
    global to_print, to_solve
    to_print += "9"
    to_solve += "9" 
    show(to_print)
def dot():
    global to_print, to_solve
    to_print += "." 
    to_solve += "."
    show(to_print)
def r_bracket():
    global to_print, to_solve
    to_print += " ) " 
    to_solve += ")"
    show(to_print)
def l_bracket():
    global to_print, to_solve
    to_print += " ( "
    to_solve += "(" 
    show(to_print) 
def e():
    global to_print, to_solve
    to_print += "e" 
    to_solve += "e"
    show(to_print) 
def square_root():
    global to_print, to_solve
    to_print += "√( "
    to_solve += "sqrt(" 
    show(to_print)
def l_sin():
    global to_print, to_solve
    to_print += "sin( "
    to_solve += "sin(" 
    show(to_print)
def l_cos():
    global to_print, to_solve
    to_print += "cos( " 
    to_solve += "cos("
    show(to_print)
def l_tan():
    global to_print, to_solve
    to_print += "tan( " 
    to_solve += "tan("
    show(to_print)  
def l_cot():
    global to_print, to_solve
    to_print += "cot( " 
    to_solve += "cot("
    show(to_print) 
def l_log():
    global to_print, to_solve
    to_print += "log( " 
    to_solve += "log(10, "
    show(to_print) 
def l_abs():
    global to_print, to_solve
    to_print += "abs( "
    to_solve += "abs(" 
    show(to_print)
def l_exp():
    global to_print, to_solve
    to_print += "exp( " 
    to_solve += "exp("
    show(to_print) 
def ln():
    global to_print, to_solve
    to_print += "ln( " 
    to_solve += "log("
    show(to_print)           
def l_pi():
    global to_print, to_solve
    to_print += "π"
    to_solve += "pi"
    show(to_print)
def rad():
    global to_print, to_solve
    to_print += "rad("
    to_solve += "radians("
    show(to_print)  
def sq():
    global to_print, to_solve
    x = re.findall("[0-9]+$", to_print) # by usage of regular expression i get number to raise in 2nd power
    to_print += "²"
    to_solve = to_solve + "*" + x[0] # multiply number by itself
    show(to_print)
def percent():
    global to_print, to_solve
    to_print += "%"
    to_solve += "/100"
    show(to_print)
def l_degrees():
    global to_print, to_solve
    x = re.findall("[0-9]+$", to_print) # by usage of regular expression i get number
    to_print += "°"
    to_solve += "/" + x[0] + "*" + f"degrees({x[0]})" # get rid of previous number by dividing to itself and multiply on target expression
    show(to_print)        


b_equal = Button(calc, text = "=", width = 4, height = 2, command = equal).grid(row = 5, column = 5)
b_plus = Button(calc, text = "+", width = 4, height = 2, command = plus).grid(row = 5, column = 6)
b_minus = Button(calc, text = "-", width = 4, height = 2, command = minus).grid(row = 4, column = 6)
b_product = Button(calc, text = "x", width = 4, height = 2, command = product).grid(row = 3, column = 6)
b_division = Button(calc, text = ":", width = 4, height = 2, command = division).grid(row = 2, column = 6)
b_delete = Button(calc, text = "C",width = 4, height = 2, command = delete).grid(row = 1, column = 6 )
b_0 = Button(calc, text = "0", width = 9, height = 2, command = zero).grid(row = 5, column = 3, columnspan = 2)
b_1 = Button(calc, text = "1", width = 4, height = 2, command = one).grid(row = 4, column = 3)
b_2 = Button(calc, text = "2", width = 4, height = 2, command = two).grid(row = 4, column = 4)
b_3 = Button(calc, text = "3", width = 4, height = 2, command = three).grid(row = 4, column = 5)
b_4 = Button(calc, text = "4", width = 4, height = 2, command = four).grid(row = 3, column = 3)
b_5 = Button(calc, text = "5", width = 4, height = 2, command = five).grid(row = 3, column = 4)
b_6 = Button(calc, text = "6", width = 4, height = 2, command = six).grid(row = 3, column = 5)
b_7 = Button(calc, text = "7", width = 4, height = 2, command = seven).grid(row = 2, column = 3)
b_8 = Button(calc, text = "8", width = 4, height = 2, command = eight).grid(row = 2, column = 4)
b_9 = Button(calc, text = "9", width = 4, height = 2, command = nine).grid(row = 2, column = 5)
b_dot = Button(calc, text = ".", width = 4, height = 2, command = dot).grid(row = 5, column = 1)
b_percent = Button(calc, text = "%", width = 4, height = 2, command = percent).grid(row = 1, column = 5)
b_r_bracket = Button(calc, text = ")", width = 4, height = 2, command = r_bracket).grid(row = 1, column = 4)
b_l_bracket = Button(calc, text = "(", width = 4, height = 2, command = l_bracket).grid(row = 1, column = 3)
b_exp = Button(calc, text = "e", width = 4, height = 2, command = e).grid(row = 3, column = 2)
b_pi = Button(calc, text = "π", width = 4, height = 2, command = l_pi).grid(row = 2, column = 2)
b_sqrt = Button(calc, text = "√", width = 4, height = 2, command = square_root).grid(row = 1, column = 0)
b_pow2 = Button(calc, text = "x²", width = 4, height = 2, command = sq).grid(row = 1, column = 2)
# in trigonometrical functions user should specify type of data radians or degrees otherwise my code will break
b_sin = Button(calc, text = "sin", width = 4, height = 2, command = l_sin).grid(row = 2, column = 1)
b_cos = Button(calc, text = "cos", width = 4, height = 2, command = l_cos).grid(row = 3, column = 1)
b_tan = Button(calc, text = "tan", width = 4, height = 2, command = l_tan).grid(row = 4, column = 1)
b_cot = Button(calc, text = "cot", width = 4, height = 2, command = l_cot).grid(row = 4, column = 0)
b_degrees = Button(calc, text ="°", width = 4, height = 2, command = l_degrees).grid(row = 5, column = 2)
b_rad = Button(calc, text ="rad", width = 4, height = 2, command = rad).grid(row = 5, column = 0)
b_abs = Button(calc, text ="|x|", width = 4, height = 2, command = l_abs).grid(row = 1, column = 1)
#sometimes eval function doesn't evaluate log, ln and exp function and returns string, sometimes it does. I didn't figured why
b_log = Button(calc, text ="log", width = 4, height = 2, command = l_log).grid(row = 2, column = 0)
b_ln = Button(calc, text ="ln", width = 4, height = 2, command = ln).grid(row = 3, column = 0)
b_e_pow_x = Button(calc, text ="eˣ", width = 4, height = 2, command = l_exp).grid(row = 4, column = 2)

output = Label(calc, text = to_print, width = 39, height = 2)
output['bg']= "white"
output.grid(row = 0, column = 0, columnspan = 7)

calc.mainloop()