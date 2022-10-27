import uuid
import mysql.connector as mysql
from tkinter import *

db = mysql.connect(

    host = "localhost",

    user = "root",

    passwd = "Milana_0110",

    database = "railway")

cursor = db.cursor()

tickets_dictionary = {}
tickets_text = ""
window = Tk()

def show_tickets(login_of_user):
#   global tickets_label
#    main_page_frame.forget()
#    my_tickets_frame.pack()
    print("except")   
    global tickets_dictionary, tickets_text
    cursor.execute(f'SELECT tickets FROM users WHERE user_login = "{login_of_user}"')
    temp = cursor.fetchall()
    tickets_list = temp[0][0].split()
    total = 0
    cursor.execute(f'SELECT user_name, user_surname FROM users WHERE user_login = "{login_of_user}"')
    temp = cursor.fetchall()
    tickets_dictionary["Name"] = temp[0][0]
    tickets_dictionary["Surname"] = temp[0][1]
    var = StringVar()
    var.set("None")
    for i in range(len(tickets_list)):
        tickets_text +=f"-----------\nTICKET#-{i+1}-\n-----------\n"
        cursor.execute(f'SELECT train_id, user_date, coach, seat FROM tickets_bought WHERE ticket_id = "{tickets_list[i]}"')
        ans = cursor.fetchall()
        tickets_dictionary["Ticket ID"] = tickets_list[i]
        tickets_dictionary["Train ID"] = ans[0][0]
        cursor.execute(f'SELECT from_station, to_station, time_in, time_out FROM trains WHERE train_id = "{tickets_dictionary["Train ID"]}"')
        temp = cursor.fetchall()
        tickets_dictionary["From station"] = temp[0][0]
        tickets_dictionary["To station"] = temp[0][1]
        tickets_dictionary["Date in"] = temp[0][2]
        tickets_dictionary["Date out"] = temp[0][3]
        tickets_dictionary["Date"] = ans[0][1]
        tickets_dictionary["Coach"] = ans[0][2]
        tickets_dictionary["Seat"] = ans[0][3]
        cursor.execute(f'SELECT price_top, price_bottom FROM tickets_price WHERE train = "{tickets_dictionary["Train ID"]}"')
        temp = cursor.fetchall() 
        if tickets_dictionary["Seat"] in range(1, 4):
            tickets_dictionary["Price"] = temp[0][1]
        else:
            tickets_dictionary["Price"] = temp[0][0]
        
        total += tickets_dictionary["Price"]
        for x in tickets_dictionary:
            tickets_text += f"{x}: {tickets_dictionary[x]}\n"

        tickets_label = Label(window, text = tickets_text, font=("Playfair Display", 10), fg = "#80807e").grid(row = i, column = 0)
        
        radiobutton = Radiobutton(window, text=f"TICKET#-{i+1}-", variable=var, value=f"TICKET#-{i+1}-").grid(row = i, column = 1)
        tickets_text = ""
    def show():
        print(var.get())
    button = Button(window, text="Choose", command=show).grid(row = len(tickets_list)+1, column = 0)

    tickets_text += f"\nTOTAL: {total}"
    tickets_label = Label(window, text = tickets_text, font=("Playfair Display", 10), fg = "#80807e").grid(row = len(tickets_list), column = 0)
    print(tickets_text)

show_tickets("_reno.boi")
window.mainloop()

"""
def show_tickets(login_of_user):
    cursor.execute(f'SELECT tickets FROM users WHERE user_login = "{login_of_user}"')
    temp = cursor.fetchall()
    print(temp)
    tickets_list = temp[0][0].split()
    print(tickets_list)
    total = 0
    for i in range(len(tickets_list)):
        print(tickets_list[i])
        cursor.execute(f'SELECT train_id, user_date, coach, seat FROM tickets_bought WHERE ticket_id = "{tickets_list[i]}"')
        ans = cursor.fetchall()
        global tickets_dictionary
        tickets_dictionary["Ticket ID"] = tickets_list[i]
        tickets_dictionary["Train ID"] = ans[0][0]
        cursor.execute(f'SELECT from_station, to_station, time_in, time_out FROM trains WHERE train_id = "{tickets_dictionary["Train ID"]}"')
        temp = cursor.fetchall()
        tickets_dictionary["From station"] = temp[0][0]
        tickets_dictionary["To station"] = temp[0][1]
        tickets_dictionary["Date in"] = temp[0][2]
        tickets_dictionary["Date out"] = temp[0][3]
        tickets_dictionary["Date"] = ans[0][1]
        tickets_dictionary["Coach"] = ans[0][2]
        tickets_dictionary["Seat"] = ans[0][3]
        cursor.execute(f'SELECT price_top, price_bottom FROM tickets_price WHERE train = "{tickets_dictionary["Train ID"]}"')
        temp = cursor.fetchall() 
        print(temp)
        if tickets_dictionary["Seat"] in range(1, 4):
            tickets_dictionary["Price"] = temp[0][1]
        else:
            tickets_dictionary["Price"] = temp[0][0]
        
        total += tickets_dictionary["Price"]
        print(tickets_dictionary)
        print(total)
        

x = '_reno.boi'
show_tickets(x)


cursor.execute('SELECT tickets FROM users WHERE user_login = "_reno.boi"')

x = cursor.fetchall()
my_list = x[0][0].split()
print(my_list)
print(type(cursor.fetchall()))
print("\n")
cursor.execute('SELECT * FROM users WHERE user_login = "netaly28"')
print(cursor.fetchall())
print("\n")

ans = [1,2,3]
print(type(ans))
print(uuid.uuid4().hex)
"""