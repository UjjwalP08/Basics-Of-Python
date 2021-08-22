"""
Dudner Method and Operator overloading

Dunder Method:- A method start with (__)double underscore and end with double underscore
    is known as

    Dudner method is one of the special type of method
"""


class Employee:
    holiday = 30

    def __init__(self, aname, astd, role, staem, s):  # init is dunder method

        self.name = aname
        self.std = astd
        self.role = role
        self.steam = staem
        self.salary = s

    def detail(self):
        return f"This mr {self.name} " \
               f" my level is {self.std} " \
               f"and steam is {self.steam} and role is {self.role} "

    @classmethod  # classmethod
    def change(cls, update):
        cls.holiday = update

    def __add__(self, other):  # Type of Dunder method or operator overloading
        return self.salary + other.salary

    def __truediv__(self, other):  # Type of Dunder method or operator overloading

        return self.salary / other.salary

    def __repr__(self):
        return f"Details is ('{self.name}','{self.role}','{self.std}'" \
               f",'{self.steam}',{self.salary})"

    def __str__(self):
        return f"This mr {self.name} " \
               f" my level is {self.std} " \
               f"and steam is {self.steam} and role is {self.role} "


emp1 = Employee("ujjwal", "Clg", "Student", "IT", 4500)
# emp2 = Employee("Harry", "Clg", "Coder", "IIIT", 5500)

# print(emp1.detail())
# print(emp2.detail())

# print(emp2 + emp1)
# print(emp1 / emp2)

# when we define __repr__ and not give any value of object than it will automatic
# return its value but when __str__method is not declare, but if __str__ method is
# declare in this scenario it return it's value ,if both dunder method is present
# in this case first priority is str then repr

print(emp1)
