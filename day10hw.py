from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

  
    def account_age(self):
        current_year = 2025
        return current_year - self.account_year

   
    @abstractmethod
    def get_role(self):
        pass


class Admin(User):

    def get_role(self):
        return "Admin"

   
    def __str__(self):
        return f"{self.name} is an Admin user with {self.account_age()} years old account."


class Guest(User):

    def get_role(self):
        return "Guest"

   
    def __str__(self):
        return f"{self.name} is a Guest user with {self.account_age()} years old account."


admin1 = Admin("Aiswarya", 2020)
guest1 = Guest("Rithik", 2023)


print("Role:", admin1.get_role())
print("Account Age:", admin1.account_age())
print(admin1)

print("Role:", guest1.get_role())
print("Account Age:", guest1.account_age())
print(guest1)