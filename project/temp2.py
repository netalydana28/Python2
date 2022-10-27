from datetime import datetime

tickets_dictionary = {}
tickets_dictionary["Date"] = "19/10/2022"
tickets_dictionary["Time in"] = "16:15"

def time_left_check():
    current_datetime = datetime.now()
    day, month, year = map(int, tickets_dictionary["Date"].split("/"))
    hour, minute = map(int, tickets_dictionary["Time in"].split(":"))
    current_year = current_datetime.year
    current_month = current_datetime.month
    current_day = current_datetime.day
    current_hour = current_datetime.hour
    current_minute = current_datetime.minute
    print(hour, current_hour)
    print(current_year < year)
    if current_year < year:
        print(year)
        return True
    elif current_month < month:
        print(month)
        return True
    elif day - current_day >=2:
        print(day)
        return True
    else:
        if day - current_day ==1:
            minute_left = (24 - current_hour)*60 + current_minute
            minute_left += hour * 60 + minute
        else:
            minute_left = (hour - current_hour) * 60 + minute
        print(hour - current_hour)
        print(minute_left)
        if minute_left <= 360:
            return False
        else:
            return True

print(time_left_check())