"""
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines.

Valid mobile: +7 777 621 34 56 or 87012345678 or +7078904367
"""
import re
with open("phones.txt", "r") as phones:
    phone_list = phones.read().split("\n")
    yes, no = list(), list()
    for i in range(len(phone_list)):
        phone_list[i] = re.sub(" ", "", phone_list[i])
        if not re.findall("[a-z]", phone_list[i]) and not re.findall("[A-Z]", phone_list[i]) and not re.findall("[@#$%^&*()_]", phone_list[i]):
            if len(phone_list[i]) == 11:
                if re.findall(r"^8707", phone_list[i]) or re.findall(r"^8747", phone_list[i])  or re.findall(r"^8777", phone_list[i]) or re.findall(r"^8701", phone_list[i]):
                    yes.append(phone_list[i])
            elif len(phone_list[i]) == 12:
                if re.findall(r"^\+7707", phone_list[i]) or re.findall(r"^\+7777", phone_list[i]) or re.findall(r"^\+7747", phone_list[i]) or re.findall(r"^\+7701", phone_list[i]):
                    yes.append(phone_list[i])
            else:
                no.append(phone_list[i])
        else: 
            no.append(phone_list[i])
    
    print(f"YES: {yes}")
    print(f"NO: {no}")