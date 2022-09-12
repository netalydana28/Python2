"""
Write a Python program to get next day of a given date.
ExpectedOutput:
Input a year: 2016
Input a month [1-12]: 08
Input a day [1-31]: 23
The next date is [yyyy-mm-dd] 2016-8-24
"""
year = int(input("Input a year: "))
leapyear = False
if year % 4 == 0:
    leapyear = True

month = int(input("Input a month [1-12]: "))
day = int(input("Input a day [1-31]: "))

if month == 2 and day == 28:
    if leapyear:
        day = 29
elif day == 31:
    if month == 12:
        year += 1
        month = 1
    day = 1
elif day == 30 and ( month == 4 or month == 6 or month == 11 or month == 11):
    day = 1
    month+=1
else:
    day +=1

print(f"The next date is [yyyy-mm-dd] {year}-{month}-{day}")

