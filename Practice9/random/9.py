#Exercise 9: Random String without Repeating Characters

import random as r 
import string

mystring = string.ascii_letters + string.digits + string.punctuation
mylist = list() # i transfer string to choose from to list to use further remove special method of lists

for i in range(len(mystring)):
    mylist.append(mystring[i])

n = int(input("Set length of string "))

def get_string():
    ans = ""
    for i in range(n):
        char = r.choice(mylist)
        ans += char
        mylist.remove(char)
    return ans

print(get_string())