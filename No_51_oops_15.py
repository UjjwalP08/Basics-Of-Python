"""
        Setters, Deleter and Property Decorators

        Generally setters use as encapsulation in oops

Setters:-
    Setters are a great way of performing encapsulation ,So by using setter,
    our interaction gets limited to the decorator, making the use of
    encapsulation concept, which is the basis of Oop. We can set new values
    for a newer object, or we can update values for an older one.

            Syntax:-@function.name.setter
                    def function

Deleter:-
    Deleter is used to delete the values passed as a parameter before.
    We can use a setter if we want to update or change the value, but we can not
    use it to delete the value. This is where deleter comes in; it removes the
    previous value and sets the variable equal to none. As in Oop we do not
    completely erase the existence of some variable but sets it equal to none.


        Syntax:-@function_name.deleter
                def function
"""


#
class employee:
    def __init__(self, f, l):
        self.fname = f
        self.lname = l
        self.email = f"The Email is {f}.{l}@gmail.com"

    def detatil(self):
        return f"Employee name is {self.fname} {self.lname}"


emp1 = employee("Harry", "Patel")
emp2 = employee("Ujjwal", "Patel")

print(emp1.email)

emp1.fname = "code"


class employee:
    def __init__(self, f, l):
        self.fname = f
        self.lname = l
        self.email = f"The Email is {f}.{l}@gmail.com"

    def detatil(self):
        return f"Employee name is {self.fname} {self.lname}"


emp1 = employee("Harry", "Patel")
# emp2 = employee("Ujjwal", "Patel")

print(emp1.email)

emp1.fname = "code"

print(emp1.email)


# here we change the fname of employee 1 but email is still same so change it
# we are use property decorator


class employee:
    def __init__(self, f, l):
        self.fname = f
        self.lname = l
        # self.email = f"The Email is {f}.{l}@gmail.com"

    def detail(self):
        return f"Employee name is {self.fname} {self.lname}"

    @property
    def email(self):
        return f"This is the new email {self.fname}.{self.lname}@scet.ac.in"


emp1 = employee("Harry", "Patel")
# emp2 = employee("Ujjwal", "Patel")

print(emp1.email)

emp1.fname = "Codewith"
emp1.lname = "Harry"
print(emp1.email)

"""
now we want to set the  email attribute so use the setters
using the setters use @function_name.setters
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
        if self.lname == None or self.lname == None:
            return f"Try again"


        return f"This is the new email {self.fname}.{self.lname}@scet.ac.in"

    @email.setter  # Set the attribute using setter
    def email(self, string):
        """Set the attribute function"""
        # print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    # we can't direct delete the setter or its attribute use this we can delete it
    @email.deleter
    def email(self):
        """Delete the set attibute"""
        self.fname = self.lname = None


emp1 = employee("Harry", "Patel")
# emp2 = employee("Ujjwal", "Patel")

print(emp1.email)

emp1.fname = "Codewith"
emp1.lname = "Harry"

print(emp1.email)

# emp1.email="that.this@gmail.com"

del emp1.email
print(emp1.email)

emp1.email = "that.this@gmail.com"
