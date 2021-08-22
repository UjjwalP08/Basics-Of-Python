"""
iterable:- a python object  which have __iter__()
 or __getitem__() method
iterator:- a python object which have __next__() method

iteration:- the process of   iterate is known as....

if the object is able to iterate it means it is iterable and not so
not iterable

iterable using above 2 functions to get iterator

Generators:- is the one of the iterator which is travers only one
time
"""


def gen(n): # Generator function
    for item in range(n):
        yield item


g = gen(4)  # here gen is generator which is use to generate no
print(g)

"""
Why we required generators ??
becoz of the free up or get space in our RAM.Suppose we have not 
a generator in python so all the data store in our ram because of that
our system is slow down that's why we required generators here g is
iterable not the iterator 
 
 making g iterator we want to use __next()__ method
"""

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__()) # Here we get the error becoz the g value is
# up to 4 after it but it end in 3 so it will generate error

# for loop design is like that after completer the work it is
# automatically exit in the iterator

# String is iterable but integer is not iterable


# --------------------Factorial------------------
def fact(n):
    f=1
    if n==1 or n==0:
        yield 1
    else:

        for i in range(1,n+1):
            f=f*i

    yield f
f=fact(5)
print(f)
print(f.__next__())
# print(f.__next__())


# ----------------------Fibonacci Series-----------------
def fibo1(n):

    """Using iterative approach"""
    a=0
    b=1
    c=0
    print("Using iteration")

    for i in range(0,n):
        c=a+b
        a=b
        b=c

    yield a
# here fibonacci series or start with index 0 so note that point
fi=fibo1(4)

print(fi.__next__())