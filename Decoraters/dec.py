# here in inner1 function we can pass function as argument and add some statements inside it

def inner1(func):
    def inner2():
        print("Before function Execution")
        func()
        print("After function Execution")

    return inner2


@inner1  # 1 way to use decorators
# This the decorter
def function_to_be_used():
    print("This is inside the function")


# function_to_be_used=inner1(function_to_be_used) # 2nd way to use decorators

function_to_be_used()

"""

Decorator as can be noticed by the name is like a designer that helps to modify a function. The decorator can be said
as a modification to the external layer of function, as it does not make any change in its structure. What a decorator 
does is, it takes a function and insert some new functionality in it without changing the function itself. A reference 
to a function is passed to a decorator and the decorator returns a modified function. The modified functions usually 
contain calls to the original function. This is also known as metaprogramming because a part of the program tries to 
modify and add functionality into another part of the program at compile time. Understanding the definition could be
difficult but we can grasp the concept easily through the example in the video section. In terms of python, the other
function is also called a wrapper.


A wrapper is a function that provides a wrap-around another function. While using decorator all the code which are
executed before our function that we passed as a parameter and also the code after it is executed belongs to the 
wrapper function. The purpose of the wrapper function is to assist us. Like if we are dealing with a number of similar 
statements, the wrapper can provide us with some code that all the functions have in common and we can use a decorator 
to call our function along with wrapper. A function can be decorated many times




Advantages:

• Decorator function can make our work compact because we can pass all the functions to a decorator that requires the
    same sort of code that the wrapper provides.
• We can get our work done, without any alteration in the original code of our function.
• We can apply multiple decorators to a single function.
• We can use decorators in authorization in Python frameworks such as Flask and Django, Logging and measuring execution 
    time.












"""




