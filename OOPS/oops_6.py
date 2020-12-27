"""
Inheritance:-it means use the property of other class

Single Inheritance:- onc class use to property of only one class
"""


class Employee:  # class 1
    leaves = 9

    def __init__(self, aname, astd, role, staem):  # constructor of Employee class
        self.name = aname
        self.std = astd
        self.role = role
        self.steam = staem

    def detail(self):
        return f"This mr {self.name} " \
               f" my level is {self.std} " \
               f"and steam is {self.steam} and role is {self.role} "

    @classmethod  # Decorator
    def change_leaves(cls, updated):
        """A function which is change leaves"""

        cls.leaves = updated


harry = Employee("harry", "12", "Student", "Science")  # Total 3 argument
ujjwal = Employee("ujjwal", "Clg", "Coder", "IT")  # Total 3 argument


# now programmer is inherited Employee class
# Now programmer class is use the all property of Employee class
# Here Employee is Parent and Programmer is child
class Programmer(Employee):
    def __init__(self, a, s, r, em, lan):  # constructor of programmer class
        self.name = a
        self.std = s
        self.role = r
        self.steam = em
        self.lan = lan

    def det1(self):
        return (f"The coder is {self.name},it's graduation is {self.std} "
                f"role is {self.role} and steam is {self.steam}"
                f"and know language is {self.lan}")


ritik = Programmer("Ritik", 12, "Programmer", "Commerce", "python")
print(ritik.det1())
print(ritik.detail())
"""
This is example of single inheritance
with example 

the son is use the property of his father this is the example of single inheritance
"""
