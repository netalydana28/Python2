"""
You are given a ﬁle called students.txt. A typical line in the ﬁle looks like:
ira menina mnina@email.msmary.edu 555-3141
There is a name, an email address, and a phone number, each separated by tabs. 
Write a program that reads through the ﬁle line-by-line, and for each line, 
capitalizes the ﬁrst letter of the ﬁrst and last name and adds the area code 301 to the phone number. 
Your program should write this to a new ﬁle called students2.txt. Here is what the ﬁrst line of the new ﬁle should look like:
Ira Menina mnina@email.msmary.edu 301-555-31
"""

with open("students.txt", "r") as students:
    students_line = students.read().split("\n")
    final_doc = list()
    for each in students_line:
        students_list = each.split()
        name = students_list[0].capitalize()
        surname = students_list[1].capitalize()
        phone = "301-" + students_list[3]
        final_line = (name, surname, students_list[2], phone)
        final_doc.append(" ".join(final_line))
        
    
with open("students2.txt", "w") as st2:
    st2.write("\n".join(final_doc))
