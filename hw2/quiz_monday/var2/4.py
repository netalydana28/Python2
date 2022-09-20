"""
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""
import re
passwords = list(input().split(","))

def check(password):
    cond1 = re.findall("[a-m]", password)
    cond2 = re.findall("[0-9]", password)
    cond3 = re.findall("[A-Z]", password)
    cond4 = re.findall("[$#@]", password)
    if len(password) >= 6 and len(password)<=12 and cond1 and cond2 and cond3 and cond4:
        return True
    else:
        return False

for i in range(len(passwords)):
    if check(passwords[i]):
        print(passwords[i])