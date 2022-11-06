"""
Exercise 7: Roll dice in such a way that every time you get the same number
Dice has 6 numbers (from 1 to 6). Roll dice in such a way that every time you must get the same output number. do this 5 times.
"""
#maybe i misunderstood this task, i solved it the way i understood it
import random as r

start = input("Push the Enter Button to roll the dice, '0' to stop")
numbers = "123456"
def roll_dice():
    global numbers
    ans = r.choice(numbers)
    print(ans)
    numbers = ans
    start = input("Push the Enter Button to roll the dice, '0' to stop")
    if start == "":
        roll_dice()
    elif start == "0":
        pass
    else:
        print("Error")

roll_dice()