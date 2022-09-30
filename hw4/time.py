"""
Write a class called Time whose only ﬁeld is a time in seconds. 
It should have a method called convert_to_minutes that returns a string of minutes and 
seconds formatted as in the following example: if seconds is 230, the method should return '3:50'. 
It should also have a method called convert_to_hours that returns a string of hours, minutes, and seconds formatted 
analogously to the previous method.
"""

class Time:

    def __init__(self, sec):
        self.__sec__ = sec

    def convert_to_minutes(self):
        return f"{self.__sec__ // 60}:{self.__sec__ % 60}"

    def convert_to_hours(self):
        return f"{self.__sec__ // 3600}:{(self.__sec__ % 3600) // 60}:{(self.__sec__ % 3600) % 60}"

time1 = Time(230)
print(time1.convert_to_minutes())
time2 = Time(3661)
print(time2.convert_to_hours())