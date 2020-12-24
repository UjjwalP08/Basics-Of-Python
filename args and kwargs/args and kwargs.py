"""
Args and Kwargs
"""


def fun(a, b, c, d):
    print(a, b, c, d)


a = "ujjwal"
b = "harry"
c = "Ritik"
d = "Conan"

# fun(a,b,c,d)

"""
In this function we have total 4 arguments and we call the function
but suppose if we are add 5th variable or argument and we call function so it is give 
an error 
Suppose we add 5th arguments in function its okay but now if we have also add 10 argument
in function so it is very lengthy and confusing
so  remove this problem python developer invent "args" and "kwargs"

using args:-Before variable name use " * "(use one star) 
using kwargs:-Before variable name use " ** "(use two star)

Types of Argument:-
    1)Normal Argument
    2)Args Argument (Using for list and tuples)
    3)Kwargs Argument (Using for dictionary)
    
*args:
    args is a short form used for arguments. It is used to unpack an argument.
In the case of *args, the argument could be a list or tuple. Suppose that we have to
enter the name of students who attended a particular lecture. Each day the number of
students is different, so positional arguments would not be helpful because we can not
leave an argument empty in that case. So the best way to deal with such programs is 
to define the function using the class name as formal positional argument and student
names with parameter *args. In this way, we can pass student's names using a tuple.

Note that the name args does not make any difference, we can use any other name, 
such as *myargs. The only thing that makes a difference is the Asterisk(*).

**kwargs:
        The full form of **kwargs is keyword arguments. It passes the data to the argument
in the form of a dictionary. Let's take the same example we used in the case of *args.
The only difference now is that the student's registration, along with the student's name,
has to be entered. So what **kwargs does is, it sends argument in the form of key and
value pair. So the student's name and their registration both can be sent as a parameter
using a single ** kwargs statement.Same as we discussed for args*, the name kwargs does not
matter. We can write any other name in its place, such as **attendance. The only mandatory
thing is the double asterisks we placed before the name.   

One of the instances where there will be a need for these keyword arguments will be when 
we are modifying our code, and we have to make a change in the number of parameters or
 a specific function.
 
 
Note:-Always we can write normal argument than write *args and than we write **kwargs
"""


def func1(noramal, *n, **args):
    print(noramal)
    print()
    for item in n:
        print(f"This is the Zeroes name is {item} ")
    print()
    for stuff, things in args.items():
        print(f"The {stuff} is a {things}")


def func2(noramal, *e):
    print("\n", noramal)

    for item in e:
        print(f"\nThis is the Zeroes score is {item} is ")


n = "This is normal Argument"

args = ["Ujjwal", "Harry", "Rohan", "Ritik", "Conan"]  # List *args

args1 = ("1", "2", "3", "4", "5")  # Tuples *args

kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "Ujjwal": "Programmer", "Shivam": "Cook"}  # Dictionary **kwargs

func1(n, *args, **kw)
# func2(n,*args1)
