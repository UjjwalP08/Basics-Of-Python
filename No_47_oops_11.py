"""
Super Class and Overriding or Overwriting
"""

#
# class A:
#     var1 = "I am the class variable of class A"
#
#
# class B(A):
#     pass
#
#     var1 = "I am the class variable of Class B"

#
# a = A()  # a is object of class A
# b = B()  # b is object of class B

# print(a.var1)
# print(b.var1)
"""
here class A we declare var1 and we also class B declare var 1
and class B is inherit class A so it is access all property of it
but above statement when we want to print both var1 so in class B
print statement is different because class B var1 is "override"
class A var 1 that why he first print or find class B var1 in 
object a 

If in class B var1 is does not exist in this case scenario it was
print class A var1  
"This is the "Overriding" or "Overwriting" "
"""
#
#
# class A:
#     var1 = "I am the class variable of class A"
#
#     def __init__(self):
#         self.var1 = "This is instance variable of class A"
#
#
# class B(A):
#     pass
#
#     var1 = "I am the class variable of Class B"
#
#
# a = A()  # a is object of class A
# b = B()  # b is object of class B
#
# print(a.var1)
# print(b.var1)

"""
In this case object b is first print the instance variable then
he print class variable but if he not found instance variable in 
parent or child class 
"""

# class A:
#     var1 = "I am the class variable of class A"
#
#     def __init__(self):
#         pass
#
#         self.var1 = "This is instance variable of class A"
#
#
# class B(A):
#     var1 = "I am the class variable of Class B"
#
#     def __init__(self):
#         pass
#         self.var1 = "I am instance variable of class B"
#
#
# # Here we are overwrite the constructor of class A
# # Overwrite statements can't print
# a = A()  # a is object of class A
# b = B()  # b is object of class B
#
# print(a.var1)
# print(b.var1)

"""
Suppose we are overwrite the constructor now we are not able to 
use it but we want to use it for some-reasons so use that 
constructor we are use "Super Class" in oops 
"""


class A:
    cvar1 = "I am the class variable of class A"

    def __init__(self):
        self.var1 = "This is instance variable of class A"
        self.special = "Something new"


class B(A):

    def __init__(self):
        super().__init__()

# First call super class constructor than call class B
# constructor so variable is not change

        self.var1 = "I am instance variable of class B"
        self.cvar1 = "I am the class variable of Class B"

        # super().__init__()


# First call Class B constructor than call super Class constructor
# so that variable is change if call here


a = A()  # a is object of class A
b = B()  # b is object of class B

# print(a.var1)
print(b.special, b.var1, b.cvar1)

print("\t\t------After------")


class A:
    cvar1 = "I am the class variable of class A"

    def __init__(self):
        self.var1 = "This is instance variable of class A"
        self.special = "Something new"


class B(A):

    def __init__(self):

        # super().__init__()

        self.var1 = "I am instance variable of class B"
        self.cvar1 = "I am the class variable of Class B"


        super().__init__()


#


a = A()  # a is object of class A
b = B()  # b is object of class B

# print(a.var1)
print(b.special, b.var1, b.cvar1)
