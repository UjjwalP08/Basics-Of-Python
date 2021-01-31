"""
        Python Comprehensions
Comprehension means write the code in some short form

Type of Comprehension in Python
1)list comprehension
2)Dictionary comprehension
3)Set comprehension
4)Generator comprehension
"""
# ---------------List Comprehension------------------

ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)
# This is the one method write or make list
print(ls)

# Now using list comprehension
ls = [i for i in range(100) if i % 3 == 0]
print(ls)


dresses = [dress for dress in ["dress1", "dress2", "dress1",
                               "dress2", "dress1", "dress2"]]

print(dresses)  # Return whole list
print(type(dresses))
print()

# ----------------Dictionary Comprehension---------------

dict1 = {i: f"{i} item" for i in range(100) if i % 10 == 0}

dict2 = {key: value for value, key in dict1.items()}
# Reverse the key and value position in dictionary
print(dict1)
print(dict2)

print(type(dict1),type(dict2))
print()
# ----------------Set Comprehension--------------

dresses = {dress for dress in ["dress1", "dress2", "dress1",
                               "dress2", "dress1", "dress2"]}

print(dresses)  # Return set that why common value print only 1 time

print(type(dresses))
print()
# ----------------Generator Comprehension--------------
# ues round parentheses() for making generator

evens = (i for i in range(100) if i % 3 == 0)

print(evens)  # Print Location
for e in evens:  # 1st method to print iterator
    print(e, end=" ")
print()
print(type(evens))  # Print it's Type

# 2nd method is us __next__() method
