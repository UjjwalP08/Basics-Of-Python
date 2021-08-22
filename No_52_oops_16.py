"""
            Object Introspection

    Object introspection means to know about object or know about object
    information like what is the class of that object,wh
"""


class employee:

    def __init__(self, f, l):
        self.fname = f
        self.lname = l
        # self.email = f"The Email is {f}.{l}@gmail.com"

    def detail(self):
        return f"Employee name is {self.fname} {self.lname}"

    @property
    def email(self):
        """Property function"""

        if self.lname == None or self.lname is None:
            return "Try again  use the setter method set attribute"

        return f"This is the new email {self.fname}.{self.lname}@scet.ac.in"

    @email.setter
    def email(self, string):
        """Set the attribute function"""
        # print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        """Delete the set attibute"""
        self.fname = self.lname = None


skill = employee("skill", "hard")

# print(skill.detail())
# print(skill.email)


print(type(skill))  # Print the the type of skill
print(id(skill))  # Print the id of skill
print(dir(skill))  # Print the all the attribute of the skill object

"""
We are using now introspection using inspect module 

"""

import inspect

print(inspect.getmembers(skill))  # Print the all detail about skill object

print(inspect.isclass(skill))
print(inspect.isfunction(skill))
print(inspect.ismethod(skill))
print(inspect.getcomments(skill))

# Some function of inspect module
