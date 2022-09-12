"""
Write a Python program to convert month name to a number of days.
List of months: January, February, March, April,May, June, July, August, September, October, November, December
Input the name of Month: February
Expected Output: No. of days: 28/29 days
"""
month_days = { "January": "31", "February": "28/29", "March": "31", "April": "30","May": "31", "June": "30", "July": "31", "August": "31", "September": "30", "October": "31", "November": "30", "December" : "31"
}
month = input("Input the name of Month: ")
print(f"No. of days: {month_days[month]} days")