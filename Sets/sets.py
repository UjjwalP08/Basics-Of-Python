s = set()  # Empty set
print(type(s))  # Print Its type
"""
Set:- Collection of well define objects

In python we can add value in set using list

Set always Identify unique values
"""
l = [1, 2, 3, 5]  # list
s1 = set(l)  # using list add values in set
print(s1)
print(type(s1))

""" Set Function or Method """
#   add() function use to add data in set
s1.add(4)
s1.add(6)
print(s1)

#   remove() function use to remove data in set
s1.remove(6)
print(s1)

# isdisjoint function use to Returns whether two sets have a intersection or not
print(s)  # s is empty set for now
print(s1.isdisjoint(s))

s.add(9)
# update() function use to update value of set through other set
s1.update(s)
print(s)
print(s1)

# remove function use to remove elemetns in the set
s1.remove(9)
print(s1)

s.add(5)
# difference function use to find diffrent value in both set
print(s1.difference(s))

# intesection use to intersect two sets
print(s1.intersection(s))

# If u intresetd more set functin so simply write in pychar set_name. after this many
# functions are visible in your IDE

print(max(s1))
print(min(s1))
print(len(s1))
"""For more set functions visit this website
https://www.w3schools.com/python/python_ref_set.asp
"""