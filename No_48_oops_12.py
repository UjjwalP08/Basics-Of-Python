"""

Diamonds Problem(Multi-level Inheritance) in OOPs

the image of diamonds problem is generally solve in python and Cpp

but not solve in java

the diamonds problem figure is shown in diamond.jpg pic

as per picture

A is grand parent
B and C is child of A
D is Child of B and C

this is the example of Multi-level Inheritance

"""

class A:
    pass

    def det(self):
        print("This is Class A")

class B(A):
    pass

    def det(self):
        print("This is Class B")


class C(A):
    pass

    def det(self):
        print("This is Class C")


class D(B,C):
    pass

    def det(self):
        pass
        # print("This is Class D")

a=A()
b=B()
c=C()
d=D()

d.det()