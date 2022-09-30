"""
Write a class called Password_manager. 
The class should have a list called old_passwords that holds all of the user’s past passwords. 
The last item of the list is the user’s current password. 
There should be a method called get_password that returns the current password and 
a method called set_password that sets the user’s password. 
The set_password method should only change the password if the attempted password is different from all the user’s past passwords. 
Finally, create a method called is_correct that receives a string and returns a boolean True or False depending on whether the string
is equal to the current password or not.
"""

class Password_manager:

    def __init__(self, user, passwords):
        self.__user__ = user
        self.__passwords__ = passwords

    def get_password(self):
        return self.__passwords__[len(self.__passwords__) - 1]

    def set_password(self, new_password):
        for i in range(len(self.__passwords__)):
            if self.__passwords__[i] == new_password:
                return "New password equals to the user's past password"

        return self.__passwords__.append(new_password)

        
        

    def is_correct(self,input_password):
        if self.__passwords__[len(self.__passwords__) - 1] == input_password:
            return True
        else:
            return False

user1 = Password_manager( "user1", ["1234", "qwerty", "idontknow"])

print(user1.get_password())
print(user1.set_password("password_is_changed"))
print(user1.get_password())
print(user1.set_password("password_is_changed"))
print(user1.is_correct("password_is_changed"))
print(user1.is_correct("qwerty"))