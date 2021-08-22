"""
    Abstract Base Class & @abstractmethod

    use the abstract class to must follow or obey of the some functions

    abstract class method is inside the abc module
"""
# from abc import ABCMeta,abstractmethod # 1st way to import abc module
from abc import ABC, abstractmethod  # 2nd way to import abc module


class Shape(ABC):
    @abstractmethod  # abstract method
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.printarea())

"""
In this case we are define abstract method in class Shape and give command
which inherit Shape class to always define or declare printarea function 
in side it, if it not declare or define so we get error

The use of Abstract class is obey the command of parent or which class
inherit parent class and it must follow this command 
"""
