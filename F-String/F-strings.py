import math

a = "Hey buddy!!!"
b = 34

# c="this is %s %s"%(a,b)
# c="this is {1} {0}"
# d=c.format(a,b)
# print(d)

c = f"this is {a} {b} {math.sin(90)}"  # This is Fstring

"""
Generally we can use fstring to reduce the add more variable in long string

suppose, we have long string and 10 variable which is type 'str', now we have add 10 variable into
string to add some string part so using above method(above fstring) we can have maximum chance
to generate error or get error or not able this program to readable form so remove this error we 
are use F-string in F-string F means fast 
In using f-sting we can add maximum string variable without any error and also our program is readable
"""

print(c)
