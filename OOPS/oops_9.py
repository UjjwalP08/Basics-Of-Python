"""
-------Public,Private and Protected access modifier------
For understand this concept using one example:--

suppose you have some information and you want to share with everyone so you copy that
information in page and stick with door so anyone see that information
"As this concept public access modifier is working in python"

suppose you have some information and you want to share with only your family members so
you stick that page inside the house so only your family member see that information
"As this concept protected access modifier is working in python"

suppose you have some information and you want to share with nobody so you stick that page
inside the your room so only you are able to  see that information
"As this concept Private access modifier is working in python"


Public Access Modifier:- Start with any name and access by all class in oops
    class employee:
      def __init__(self, name, age):
            self.name=name #Public access modifier
            self.age=age#Public access modifier

Protected Access Modifier:-Only access by the class  and its subclass which it is derived
    before start variable naem '_'(single underscore) using
    Syntax:- _variable=value
    class employee:
      def __init__(self, name, age):
            self._name=name # protected attribute
            self._age=age # protected attribute

Private Access Modifier:-Only access by the class which it is derived not access by its
        sub-class
        before start variable naem '__'(double underscore) using
        class employee:
      def __init__(self, name, age):
            self.__name=name # private attribute
            self.__age=age # private attribute

        for print this access modifier:---

            print(object._Classname__private modifier)
            Eg:-print(emp._Employee__raja)
            here emp=object name
            Employee=Class name
            raja=private modifier



"""


class Employee:
    leaves = 9  # Public access modifier
    _holidays = 5  # Private access modifier
    __raja = 4  # Protected access modifier

    def __init__(self, aname, astd, role, staem):
        self.name = aname
        self.std = astd
        self.role = role
        self.steam = staem

    def detail(self):
        return f"This mr {self.name} " \
               f" my level is {self.std} " \
               f"and steam is {self.steam} and role is {self.role} "


emp = Employee("Emp", 12, "Employee", "IT")

# print(emp.detail())
print("This is public access modifier", emp.leaves)
print("This is protected access modifier",emp._holidays)
print("This is private access modifier",emp._Employee__raja)
