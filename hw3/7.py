"""
Use a regular expression to take a date in a verbose format, like February 6, 2011, and convert it an abbreviated format, mm/dd/yy (with no leading zeroes).

For instance, your program must work:

1. the user spells out the whole month name or abbreviates it ;
2. Capitalization does not matter;
3. Only the ﬁrst three letters must be correct;
4. No matter how much space they use;
5. Whether or not they use a comma after the day.

Examples:

>> Enter date: Feb 1 2019

2/1/19

Enter date: Janjhhh.3 1290

1/3/90
"""
import re

date = input()

def month_reader(date):
    date = date.lower()
    if re.findall("^jan", date):
        return "1"
    elif re.findall("^feb", date):
        return "2"
    elif re.findall("^mar", date):
        return "3"
    elif re.findall("^apr", date):
        return "4"
    elif re.findall("^may", date):
        return "5"
    elif re.findall("^jun", date):
        return "6"
    elif re.findall("^jul", date):
        return "7"
    elif re.findall("^aug", date):
        return "8"
    elif re.findall("^sep", date):
        return "9"
    elif re.findall("^oct", date):
        return "10"
    elif re.findall("^nov", date):
        return "11"
    elif re.findall("^dec", date):
        return "12"

month = month_reader(date)
temp = re.findall("\D+[0-9]{1,2}", date)
day = re.findall("[0-9]{1,2}$", temp[0])
year = re.findall("[0-9]{4}$", date)
print(month[0] + "/" + day[0] + "/" + year[0])