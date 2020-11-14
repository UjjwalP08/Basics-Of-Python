var1 = "Hello "
var2 = "Hey brother"
var3 = 45
var4 = 75.5

# In pytho compiler automatic Identify the varible type
print(type(var1))
print(var1)

"""
In python when we add two string the string not excatly add but it is
joint with each other
"""
print(var1+var2)
print(var3+var4)

v1 = "32 "  # here v1 is string not int becoz we use double quotes
v2 = "45"  # here v2 is string not int
print(v1+v2)

print(int(v1)+int(v2))
"""
here we are type cast v1 and v2 becoz these variables are
strings
"""

"""
In python to take input from user we can use 
input() function

here input save as the string form so if we enter int this int also store
in string type
"""
print("Enter a number")
n1 = input()

print("Enter a second number")
n2 = input()

print(10 *("The sum is  ", n1 + n2))
# here answer is n1 n2 becoz it is string

print("The sum is ", int(n1) + int(n2))
# here we are typecast the varible to string to Int
