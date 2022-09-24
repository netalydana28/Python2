"""
Print the space-separated name and email address pairs containing valid email addresses only. 
Each pair must be printed on a new line in the following format:

name <user@email.com>

You must print each valid email address in the same order as it was received as input.
"""

"""
My validity criteria:
A) ends with @gmail.com or @mail.ru or @example.com
B) no whitespaces, no -, no capital letters, no +
C) letters [a-z] before @
D) starts with [a-z]

P.S. there could be much more criteria but i have chosen this ones
I found example of list in internet
"""
import re

with open("emails.txt", "r") as  emails:
    email_list = emails.read().split("\n")
    for each in email_list:
        name, email = each.split()
        email = re.sub("^<", "", email)
        email = re.sub(">$", "", email)
        if (re.findall("[a-z]+\.*[a-z]*@mail.ru$", email) or re.findall("[a-z]+\.*[a-z]*@gmail.com$", email) or re.findall("[a-z]+\.*[a-z]*@example.com$", email)) and (re.findall("^[a-z]", email)) and (not re.findall("[A-Z]", email) and not re.findall("\-", email) and not re.findall("\+", email)):
            print(name + " " + email)
