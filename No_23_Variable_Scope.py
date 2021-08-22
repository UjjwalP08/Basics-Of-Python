""" 
        ---------->  Variable Scope,Global Variable and Local Variable,Global Keyword
 """

c=45 #Global Variable

def func1():
    y=54 #Local Variable
    print(y,c)


func1()
print(y) #give error because y is local variable and its scope only
# for fucn1() scope
print(c)



c=45

def func2():
    global c
    """Here using global keyword we are able to change value of
    global variable c
    if we aren't use the global keyword we are unable to change the
    value of global vatiable c value
    """
    c+=55
    print("This is value of c in side the function" ,c)

func2()
print(c)

"""
Nested function:- Function inside the function is known as....
"""

def fun1():
    x=45
    def fun2():
        global x
        x=100
    print("Before calling function",x)
    fun2()

    print("After calling function",x)
"""Here after calling function the value is not change becoz 
   global keyword is direct change the global variable values
   but here both x is local variable so initially global variable
   x value is 0
"""


fun1()
print(x)
"""After func1() the global variable value is change 0 to 100 becoz
   the global keyword
"""







