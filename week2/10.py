"""
Write a Python program to display astrological sign for given date of birth.
ExpectedOutput: Input birthday: 15 
Input month of birth (e.g. march, july etc): may
Your Astrological sign is: Taurus
"""

astrology = {
    "January": [19, "Capricorn", "Aquarius"],
    "February": [18, "Aquarius", "Pisces"],
    "March": [20, "Pisces", "Aries"],  
    "April": [19, "Aries", "Taurus"], 
    "May": [20, "Taurus", "Gemini"], 
    "June": [20, "Gemini", "Cancer"],  
    "July": [22, "Cancer", "Leo"],
    "August": [22, "Leo", "Virgo"],
    "September": [22, "Virgo", "Libra"], 
    "October": [22, "Libra", "Scorpio"], 
    "November": [19, "Capricorn", "Sagittarius"],   
    "December": [21, "Sagittarius", "Capricorn"],   

}

birthday = int(input("Input birthday: "))
birthmonth = input("Input month of birth (e.g. March, July etc): ")
if birthday <= astrology[birthmonth][0]:
    print(f"Your Astrological sign is: {astrology[birthmonth][1]}")
else:
    print(f"Your Astrological sign is: {astrology[birthmonth][2]}")
  