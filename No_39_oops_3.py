"""
Changing the class variable using class method


class method is use the @classmethod
"""


class emempolyee:
    leaves = 9

    holiday = 30

    def __init__(self, aname, astd, role, staem):  # constructor

        self.name = aname
        self.std = astd
        self.role = role
        self.steam = staem

    def detail(self):
        return f"This mr {self.name} " \
               f" my level is {self.std} " \
               f"and steam is {self.steam} and role is {self.role} "

    # Suppose we want to change leaves without using class.variable name
    # so we use class method as you seen
    @classmethod  # Decorator
    def change_leaves(cls, updated):
        """A function which is change leaves"""
        # Here cls means class we can direct change the variable of classs

        cls.leaves = updated  # Change the class variable using class method
        # cls.holiday=updated# Change the class variable using class mehtod

    @classmethod
    def change_holidays(cls, update):
        """A function which is change holidays"""

        cls.holiday = update


harry = emempolyee("harry", "12", "Student", "Science")
ujjwal = emempolyee("ujjwal", "Clg", "Coder", "IT")

print(emempolyee.change_leaves.__doc__)
print(emempolyee.change_holidays.__doc__)
print()
print("Before")
print("Ujjwal leaves are", ujjwal.leaves, "ujjwal Holidays are", ujjwal.holiday)

print("Harry leaves are", harry.leaves, "Harry Holidays are", harry.holiday)

print()

print("Before changing leaves is", emempolyee.leaves)
emempolyee.change_leaves(45)
print("After changing  leaves is", emempolyee.leaves)

print("Before changing Holiday are", emempolyee.holiday)
emempolyee.change_holidays(10)
print("After changing Holidays are", emempolyee.holiday)
# print(ujjwal.detail())
# print(harry.detail())

print()
print("After")
print("Ujjwal leaves are", ujjwal.leaves, "ujjwal Holidays are", ujjwal.holiday)

print("Harry leaves are", harry.leaves, "Harry Holidays are", harry.holiday)
