from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as mysql
import re
from datetime import datetime
import uuid
from tkinter.messagebox import showinfo

db = mysql.connect(

    host = "localhost",

    user = "root",

    passwd = "Milana_0110",

    database = "railway")

cursor = db.cursor()

cursor.execute("SHOW TABLES;")

print(cursor.fetchall())

window = Tk()
window.geometry('1536x864')

enter_frame = Frame(window)
sign_in_frame = Frame(window)
main_page_frame = Frame(window)
my_tickets_frame = Frame(window)
vacant_seats_frame = Frame(window)
enter_frame.pack()

# enter frame
e_login_label = Label(enter_frame, text = "Login", font=("Arial Bold", 20), width = 10, height = 4).grid(row = 1, column = 0)
e_login = Entry(enter_frame)
e_login.grid(row = 1, column = 1)

e_password_label = Label(enter_frame, text = "Password", font=("Arial Bold", 20), width = 10, height = 4).grid(row = 2, column = 0)
e_password= Entry(enter_frame, show = "*")
e_password.grid(row = 2, column = 1)

# sign in frame
s_login_label = Label(sign_in_frame, text = "Login", font=("Arial Bold", 10), width = 10, height = 4).grid(row = 0, column = 0)
s_login = Entry(sign_in_frame)
s_login.grid(row = 0, column = 1)
s_password_label = Label(sign_in_frame, text = "Password", font=("Arial Bold", 10), width = 20, height = 4).grid(row = 2, column = 0)
s_password= Entry(sign_in_frame, show = "*")
s_password.grid(row = 2, column = 1)
s_password2_label = Label(sign_in_frame, text = "Repeat the password, \nplease", font=("Arial Bold", 10), width = 21, height = 4).grid(row = 3, column = 0)
s_password2 = Entry(sign_in_frame, show = "*")
s_password2.grid(row = 3, column = 1)
s_name_label = Label(sign_in_frame, text = "Your name", font=("Arial Bold", 10), width = 21, height = 4).grid(row = 5, column = 0)
s_surname_label = Label(sign_in_frame, text = "Your surname", font=("Arial Bold", 10), width = 21, height = 4).grid(row = 6, column = 0)
s_name = Entry(sign_in_frame)
s_name.grid(row = 5, column = 1)
s_surname = Entry(sign_in_frame)
s_surname.grid(row = 6, column = 1)


#main page
bg = Image.open("main_bg.jpg")
search_sign = Image.open("search.png")
search_sign = ImageTk.PhotoImage(search_sign)
bg = bg.resize((1536, 864))
bg = ImageTk.PhotoImage(bg)
main_bg = Label(main_page_frame, image = bg)
main_bg.grid(row = 0, column = 0)
from_station_label = Label(main_page_frame, text = "from-station", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e", width = 9)
from_station_label.place(x = 20, y = 40)
from_station_entry = Entry(main_page_frame, bg = "#f5f8f9", fg = "#80807e", width = 40)
from_station_entry.place(x = 100, y =40)
to_station_label = Label(main_page_frame, text = "to-station", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e", width = 9)
to_station_label.place(x = 347, y = 40)
to_station_entry = Entry(main_page_frame, bg = "#f5f8f9", fg = "#80807e", width = 40)
to_station_entry.place(x = 428 , y = 40)
date_label = Label(main_page_frame, text = "date", font=("Playfair Display", 10), fg = "#80807e", width = 9).place(x = 675, y = 40)
date_entry = Entry(main_page_frame, bg = "#f5f8f9", fg = "#80807e", width = 40)
date_entry.place(x = 755, y = 40)

#my tickets frame
tickets_text = ""
tickets_dictionary = {}
t_bg = Image.open("tickets_bg.jpg")
t_bg = t_bg.resize((1536, 864))
t_bg = ImageTk.PhotoImage(t_bg)
tickets_bg = Label(window, image = t_bg)

def log_in():
    global login_of_user
    login_of_user = e_login.get()
    password_of_user = e_password.get()
    cursor.execute(f"SELECT * FROM users WHERE user_login = '{login_of_user}' and user_password = '{password_of_user}'")
    to_check = cursor.fetchall()

    if to_check:
        print("User is in the base") 
        e_login.delete(0, END)
        e_password.delete(0, END)
        enter_frame.forget()
        main_page_frame.pack()
    else:
        label_wrong = Label(enter_frame, text = "Wrong password or login", font=("Arial Bold", 11), fg="red", width = 20, height = 2).grid(row = 0, column = 0, columnspan = 2)

def register():
    global login_of_user
    login_of_user = s_login.get()
    password_of_user = s_password.get()
    password2_of_user = s_password2.get()
    name_of_user = s_name.get()
    surname_of_user = s_surname.get()
    cursor.execute(f"SELECT * FROM users WHERE user_login = '{login_of_user}'")
    to_check = cursor.fetchall()
    mistakes_cnt = 0
    label_wrong1 = Label(sign_in_frame, text = f"Passwords are different", font=("Arial Bold", 8), fg="red", width = 20, height = 2)
    label_wrong2 = Label(sign_in_frame, text = f"The login already exists \n in the base", font=("Arial Bold", 8), fg="red", width = 20, height = 2)
    label_wrong3 = Label(sign_in_frame, text = f"Please, fill all gaps", font=("Arial Bold", 8), fg="red", width = 20, height = 2)

    if password_of_user != password2_of_user:
        label_wrong1.grid(row = 4, column = 1, columnspan = 2)
        mistakes_cnt += 1 

    if len(to_check) != 0:
        label_wrong2.grid(row = 1, column = 1, columnspan = 2) 
        mistakes_cnt +=1

    if len(name_of_user)==0 or len(surname_of_user)==0 or len(login_of_user) == 0 or len(password_of_user) == 0 or len(password2_of_user) == 0:
        label_wrong3.grid(row = 7, column = 1, columnspan = 2) 
        mistakes_cnt +=1   

    if mistakes_cnt == 0:
        cursor.execute(f"INSERT INTO users (user_login, user_password, user_name, user_surname, tickets) VALUES ('{login_of_user}', '{password_of_user}', '{name_of_user}', '{surname_of_user}', '')")
        db.commit()
        sign_in_frame.forget()
        main_page_frame.pack()

def prev_page(): 
    sign_in_frame.forget()
    enter_frame.pack()

def prev_page1(): 
    main_page_frame.forget()
    enter_frame.pack()

def prev_page2():
    my_tickets_frame.forget()
    main_page_frame.pack()

def prev_page3():
    vacant_seats_frame.forget()
    main_page_frame.pack()

def sign_in():
    enter_frame.forget()
    return_button = Button(sign_in_frame, text = "Return to \nprevious page", font=("Times New Roman", 10), bg="blue", fg="white", width = 15, height = 2, command = prev_page).grid(row = 8, column = 0)
    sign_in_button = Button(sign_in_frame, text = "Sign in", font=("Times New Roman", 10), bg="blue", fg="white", width = 15, height = 2, command = register).grid(row = 8, column = 1)
    sign_in_frame.pack()

def update_main_page():
    for widget in my_tickets_frame.winfo_children():
            widget.destroy()
    log_in()

def search():
    #update_main_page()
    to_print = ""
    from_station = from_station_entry.get()
    to_station = to_station_entry.get()
    date = date_entry.get()
    query = f"SELECT * FROM trains WHERE from_station = '{from_station}' and to_station = '{to_station}'"
    cursor.execute(query)
    ans = cursor.fetchall()
    to_print += '{train_id:^10}|{from_s:^20}|{to_s:^20}|{in_t:^10}|{out_t:^10}|{price_top:^30}|{price_bottom:^30}\n'.format(train_id = "Train", from_s = "From-station", to_s = "To-station", in_t = "Time in", out_t = "Time out", price_top = "Top seats price (1, 2, 3)", price_bottom = "Bottom seats price (4, 5)")
    to_print = to_print + "-"*150 + "\n"
    var = StringVar()
    var.set("None")
    dy = 70
    for i in range(len(ans)):
        to_print += '{train_id:^10}|{from_s:^20}|{to_s:^20}|{in_t:^10}|{out_t:^10}|{price_top:^30}|{price_bottom:^30}\n'.format(train_id = f"{ans[i][0]}", from_s = f"{ans[i][1]}", to_s = f"{ans[i][2]}", in_t = f"{ans[i][3]}", out_t = f"{ans[i][4]}", price_top = f"{ans[i][5]}", price_bottom = f"{ans[i][6]}")
        to_print = to_print + "-"*150 + "\n"
        radiobutton = Radiobutton(main_page_frame, text=f"{ans[i][0]}", variable=var, value=f'{ans[i][0]}').place(x = 755, y = dy)
        dy +=20

    search_ans_label = Label(main_page_frame, text = f"{to_print}", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e", justify = "left").place(x = 20, y = 70)
    def show_vacant_seats():
        main_page_frame.forget()
        vacant_seats_frame.pack()
        my_train = var.get()
        query = f"SELECT * FROM tickets_bought WHERE train_id = '{my_train}' and user_date = '{date}'"
        cursor.execute(query)
        tickets = cursor.fetchall()
        to_print = ""
        coaches ={1 : [1, 2, 3, 4, 5], 2 : [1, 2, 3, 4, 5], 3 : [1, 2, 3, 4, 5], 4 : [1, 2, 3, 4, 5], 5 : [1, 2, 3, 4, 5]}

        for i in range(len(tickets)):
            coaches[tickets[i][3]].remove(tickets[i][4])

        for i in range(len(coaches)):
            to_print += f"Coach #{i+1}:\n"
            for j in range(len(coaches[i+1])):
                to_print += str(coaches[i+1][j])
                to_print += "\n"
        
        ans_label = Label(vacant_seats_frame, text = f"{to_print}", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e").grid(row = 0, column = 0, rowspan = 10)
        coach_label = Label(vacant_seats_frame, text = "Choose your coach", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e").grid(row = 0, column = 1)
        seat_label = Label(vacant_seats_frame, text = "Choose your seat", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e").grid(row = 1, column = 1)
        coach_entry = Entry(vacant_seats_frame, font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e")
        coach_entry.grid(row = 0, column = 2)
        seat_entry = Entry(vacant_seats_frame, font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e")
        seat_entry.grid(row = 1, column = 2)

        def announce_purchase():
            showinfo( 
                title = 'Congratulations!', 
                message = "Ticket was bought\nUpdate the page"
                )

        def buy():
            coach = coach_entry.get()
            seat = seat_entry.get()
            if int(seat) in coaches[int(coach)]:
                ticket_id = uuid.uuid4().hex
                query = f"INSERT INTO tickets_bought (ticket_id, train_id, user_date, coach, seat) VALUES ('{ticket_id}', '{my_train}', '{date}', '{coach}', '{seat}')"
                cursor.execute(query)
                db.commit()
                cursor.execute(f'SELECT tickets FROM users WHERE user_login = "{login_of_user}"')
                temp = cursor.fetchall()
                tickets_list = temp[0][0].split()
                tickets_list.append(ticket_id)
                temp = ""
                for i in range(len(tickets_list)):
                    temp += f"{tickets_list[i]} "
                cursor.execute(f"UPDATE users SET tickets = '{temp}' WHERE user_login = '{login_of_user}'")
                db.commit()
                announce_purchase()
            else:
                label_wrong = Label(vacant_seats_frame, text = "Seat is not vacant", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "red").grid(row = 3, column = 1)
        
        def clearFrame():
            for widget in vacant_seats_frame.winfo_children():
                widget.destroy()

        def update_page():
            clearFrame()
            show_vacant_seats()

        update_button = Button(vacant_seats_frame, text = "Update\npage", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e", command = update_page).grid(row = 11, column = 1)
        buy_button = Button(vacant_seats_frame, text = "Buy\nticket", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e", command = buy).grid(row = 2, column = 1)
        return_button = Button(vacant_seats_frame, text = "Previous page", font=("Playfair Display", 10), bg = "#f5f8f9", fg = "#80807e", command = prev_page3).grid(row = 11, column = 0)


    show_vacant_seats_button = Button(main_page_frame, text = "Show vacant\n seats", font=("Playfair Display", 10), bg = "#736f7b", fg = "white", command = show_vacant_seats).place(x = 755, y = 500)

def show_tickets():
    global tickets_label
    main_page_frame.forget()
    my_tickets_frame.pack()
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
    to_print = ""
    for i in range(len(tickets_list)):
        tickets_text +=f"-----------\nTICKET#-{i+1}-\n-----------\n"
        cursor.execute(f'SELECT train_id, user_date, coach, seat FROM tickets_bought WHERE ticket_id = "{tickets_list[i]}"')
        ans = cursor.fetchall()
        tickets_dictionary["Ticket ID"] = tickets_list[i]
        tickets_dictionary["Train ID"] = ans[0][0]
        cursor.execute(f'SELECT from_station, to_station, time_in, time_out, price_top, price_bottom FROM trains WHERE train_id = "{tickets_dictionary["Train ID"]}"')
        temp = cursor.fetchall()
        tickets_dictionary["From station"] = temp[0][0]
        tickets_dictionary["To station"] = temp[0][1]
        tickets_dictionary["Time in"] = temp[0][2]
        tickets_dictionary["Time out"] = temp[0][3]
        tickets_dictionary["Date"] = ans[0][1]
        tickets_dictionary["Coach"] = ans[0][2]
        tickets_dictionary["Seat"] = ans[0][3]

        if tickets_dictionary["Seat"] in range(1, 4):
            tickets_dictionary["Price"] = temp[0][4]
        else:
            tickets_dictionary["Price"] = temp[0][5]
        
        total += tickets_dictionary["Price"]
        for x in tickets_dictionary:
            tickets_text += f"{x}: {tickets_dictionary[x]}\n"

        tickets_label = Label(my_tickets_frame, text = tickets_text, font=("Playfair Display", 10), fg = "#80807e").grid(row = i, column = 0)
        to_print += tickets_text
        radiobutton = Radiobutton(my_tickets_frame, text=f"TICKET#-{i+1}-", variable=var, value=f'{tickets_dictionary["Ticket ID"]}').grid(row = i, column = 1)
        tickets_text = ""

    def time_left_check():
        current_datetime = datetime.now()
        day, month, year = map(int, tickets_dictionary["Date"].split("/"))
        hour, minute = map(int, tickets_dictionary["Time in"].split(":"))
        current_year = current_datetime.year
        current_month = current_datetime.month
        current_day = current_datetime.day
        current_hour = current_datetime.hour
        current_minute = current_datetime.minute
        if current_year < year:
            return True
        elif current_month < month:
            return True
        elif day - current_day >=2:
            return True
        else:
            if day - current_day ==1:
                minute_left = (24 - current_hour)*60 + current_minute
                minute_left += hour * 60 + minute
            else:
                minute_left = (hour - current_hour) * 60 + minute
            if minute_left <= 360:
                return False
            else:
                return True

    def announce_cancel():
        showinfo( 
            title = 'Congratulations!', 
            message = "Ticket was canceled\nUpdate the page"
            )
        
    def cancel():
        if time_left_check():
            temp = var.get()
            query = f"DELETE FROM tickets_bought WHERE ticket_id = '{temp}'"
            cursor.execute(query)
            db.commit()
            tickets_list.remove(temp)
            temp = ""
            for i in range(len(tickets_list)):
                temp += f"{tickets_list[i]} "
            query = f"UPDATE users SET tickets = '{temp}' WHERE user_login = '{login_of_user}'"
            cursor.execute(query)
            db.commit()
            announce_cancel()
        else: 
            mistake_label = Label(my_tickets_frame, text = "Less than 6 hours left.\nCancelation can't be done", font=("Playfair Display", 10), fg = "red").grid( row = len(tickets_list) +3, column = 0, columnspan = 2)
    
    def clearFrame():
        for widget in my_tickets_frame.winfo_children():
            widget.destroy()

    def update_page():
        clearFrame()
        show_tickets()

    def download_txt():
        with open("receipt.txt", "w") as f:
            f.write(to_print)

    cancel_button = Button(my_tickets_frame, text="Cancel", command=cancel).grid(row = len(tickets_list)+1, column = 0)
    download_button = Button(my_tickets_frame, text="Download ticket", command=download_txt).grid(row = len(tickets_list)+1, column = 1)
    return_button = Button(my_tickets_frame, text="Previous page", command=prev_page2).grid(row = len(tickets_list)+2, column = 0)
    update_button = Button(my_tickets_frame, text="Update", command=update_page).grid(row = len(tickets_list)+2, column = 1)

    tickets_text += f"\nTOTAL: {total}"
    to_print += tickets_text
    tickets_label = Label(my_tickets_frame, text = tickets_text, font=("Playfair Display", 10), fg = "#80807e").grid(row = len(tickets_list), column = 0)
    print(tickets_text)
    tickets_text = ""
    
log_in_button = Button(enter_frame, text = "Log in", font=("Times New Roman", 10), bg="green", fg="white", width = 15, height = 2, command = log_in).grid(row = 3, column = 0, columnspan = 2)
sign_in_button = Button(enter_frame, text = "Sign in", font=("Times New Roman", 10), bg="blue", fg="white", width = 15, height = 2, command = sign_in).grid(row = 4, column = 0, columnspan = 2)
search_button = Button(main_page_frame, image = search_sign, command = search).place(x = 1000, y =40)
tickets_button = Button(main_page_frame, text = "My tickets", font=("Playfair Display", 10), bg = "#c79a8d", width = 10, height = 2, command = show_tickets).place(x = 1200, y = 40)
return_button = Button(main_page_frame, text = "Log out", font=("Times New Roman", 10), bg="#c79a8d", fg="white", width = 10, height = 2, command = prev_page1).place(x = 20, y = 750)


window.mainloop()