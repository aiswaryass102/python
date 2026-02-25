from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    
    def years_on_platform(self):
        current_year = 2025
        return current_year - self.joining_year

    
    @abstractmethod
    def display(self):
        pass


class Customer(User):
    def display(self):
        role = "Customer"
        print(f"Name: {self.name}, Role: {role}, Years on Platform: {self.years_on_platform()}")


class Vendor(User):
    def display(self):
        role = "Vendor"
        print(f"Name: {self.name}, Role: {role}, Years on Platform: {self.years_on_platform()}")


c1 = Customer("Aiswarya", 2021)
v1 = Vendor("varsha", 2019)

c1.display()
v1.display()