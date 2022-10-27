from tkinter import *

enter_window = Tk()

screenwidth = enter_window.winfo_screenwidth()
screenheight = enter_window.winfo_screenheight()
x0 = screenwidth/2
y0 = screenheight/2

l_w = 250
l_h = 70
b_w = 240
b_h = 70
interval = 40


users = {"eldana": "Milana_0110","alisher": "12345", "kamilla": "qwerty"}

login_label = Label(enter_window, text = "Login", font=("Arial Bold", 40)).place(x = x0 - l_w - (interval /2), y = y0 - l_h - (interval/2), width = l_w, height = l_h)
login = Entry(enter_window)
login.place(x = x0 + (interval/2), y = y0 - l_h - (interval/2), width = l_w, height = l_h)

password_label = Label(enter_window, text = "Password", font=("Arial Bold", 40)).place(x = x0 - l_w - (interval /2), y = y0 + (interval/2), width = l_w, height = l_h)
password= Entry(enter_window)
password.place(x = x0 + (interval/2), y = y0 +(interval/2), width = l_w, height = l_h)

def callback():

    login_of_user = login.get()
    password_of_user = password.get()

    if login_of_user in users.keys():
        if users[login_of_user] == password_of_user:
            print("Enter is successful") 
        else:
            pass
            #print("Wrong password or login")
            #sign_in_label = Label(enter_window, text = "Wrong password or login").place(x = x0y = y0 - interval * 1.5 )
    
log_in_button = Button(enter_window, text = "Log in", font=("Times New Roman", 20), bg="green", fg="white", command = callback).place(x = x0 - (b_w/2) , y = y0 + 2 * interval + l_h, width = b_w, height = b_h)
sign_in_button = Button(enter_window, text = "Sign in", font=("Times New Roman", 20), bg="blue", fg="white").place(x = x0 - (b_w/2), y = y0 + 3 * interval + l_h + b_h, width = b_w, height = b_h)

#print(screenheight, screenwidth)
enter_window.mainloop()