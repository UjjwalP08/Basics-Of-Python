"""
Static Method

Some time we need to the different method which is not access by object
 and class directly that method is "Static Method"

Static method use by @staticmethod decorator
"""


class emempolyee:
    leaves = 9

    def __init__(self, aname, astd, role, staem):
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

    @classmethod
    def das(cls, str):
        return cls(*str.split("-"))

    @classmethod
    def slash(cls, string):
        return cls(*string.split("/"))

    @staticmethod  # Static method
    def tpri(string):
        print("That is good thing " + string)
"""
This method is not take an object or any function as arguments just only
print some statements

Why we add inside the class?
because it only run by the employee object that why we added into object
"""


harry = emempolyee("harry", "12", "Student", "Science")  # Total 3 argument
ujjwal = emempolyee("ujjwal", "Clg", "Coder", "IT")  # Total 3 argument
mehul = emempolyee.das("mehul-10-student-school")

print(mehul.detail())

mehul.tpri("You know")