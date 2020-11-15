shopping = ["biscuits", "chezze", "cokacola", 23, 34]
# This is list data structure which start with index 0

print(shopping)
# print the values of list

print(type(shopping))
#Print which type data type we are using


print(shopping[3])
# print index 3 element

print(shopping[2])
# print index 2 element

shopping[2] = "Sprite"
# list data structure is Mutable data type

# Mutable:- we can change the index values
# Immutable:- we cannot change the index values
print(shopping[::])
# automatic detect start and end

print(shopping[0:5])  # List slicing

# print(shopping[10])
#  give error this
numbers = [1, 35, 6, 7, 2, 60, 9, 12, 43, 34]
print(numbers)

print(max(numbers))
#print max element which is  in the list

print(min(numbers))
#print min element which is in the list
"""Some List Method or Function"""

numbers.sort()  # use this function to sorting elemnts
print(numbers)

numbers.reverse()
# use this function to reverse list elements
print(numbers)

numbers.append(3)
numbers.append(90)
numbers.append(450)
# use this function to add elements in end of list
print(numbers)

numbers.insert(3, 70)
# use this function to add elements at specific index
print(numbers)

numbers.pop(0)
# use this function to remove elements at specific index
numbers.pop()
"""if we leave paranthese blank it is automatic remove last
elements"""
print(numbers)

numbers.remove(1)
# use this function to remve direct elements in list
print(numbers)

numbers.clear()
# delete all elements
print(numbers)

a = (1, 2, 3)
"""this is tuple in python describe tuples we are use 
() this type brackets or parantheses"""

# tuple is Immutable data type

print(a)
# we cannot add the value is tuple using a(1)=4 this

"""For more function use this url
https://www.w3schools.com/python/python_ref_list.asp
https://docs.python.org/3/tutorial/datastructures.html"""
# Swaping
a = 4
b = 5
temp = a
a = b  # this is standard  Method of swaping
b = temp
print(a, b)

# Python Method for swaping

a = 10
b = 20

a, b = b, a
print(a, b)

a = 12
b = 20
c = 40
# In below exam precedence is Right to left
a, b, c = c, a, b
print(a, b, c)
