"""
Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
ExpectedOutput:Input the month (e.g. [1-12]): 07
Input the day: 31
Output: July, 31. Season is autumn
"""
season = {
    "01": ["January", "winter"],
    "02": ["February", "winter"],
    "03": ["March", "spring"],
    "04": ["April", "spring"],
    "05": ["May", "spring"],
    "06": ["June", "summer"],
    "07": ["July", "summer"],
    "08": ["August", "summer"],
    "09": ["September", "autumn"],
    "10": ["October", "autumn"],
    "11": ["November", "autumn"],
    "12": ["December", "winter"]
}

month = input("Input the month (e.g. [1-12]): ")
day= input("Input the day: ") 
print(f"{season[month][0]}, {day}. Season is {season[month][1]}")

#i haven't taken into accout if the input day doesn't exist