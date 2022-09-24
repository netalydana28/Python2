"""
You are given a ﬁle namelist.txt that contains a bunch of names.
Some of the names are a ﬁrst name and a last name separated by spaces, like George Washington, while others have a middle name, like John Quincy Adams. 
There are no names consisting of just one word or more than three words. 
Write a program that asks the user to enter initials, like GW or JQA, and prints all the names that match those initials. 
Note that initials like JA should match both John Adams and John Quincy Adams
"""
import re 

initials = input("Write down your initials: ")

with open("namelist.txt", "r") as namelist:
    names = namelist.read().split("\n")
    for each in names:
        name = each.split()
        if len(initials) == 2:
            if len(name) == 3:
                if re.findall(f"^{initials[0]}", name[0]) and (re.findall(f"^{initials[1]}", name[2])):
                    print(" ".join(name))
            else:
                if re.findall(f"^{initials[0]}", name[0]) and (re.findall(f"^{initials[1]}", name[1])):
                    print(" ".join(name))                
        else:
            if re.findall(f"^{initials[0]}", name[0]) and re.findall(f"^{initials[1]}", name[1]) and re.findall(f"^{initials[2]}", name[2]):
                print(" ".join(name))