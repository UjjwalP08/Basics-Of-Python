a = {"key": "value", "greet": "good morning", "jay": "studyman", "mehul": "FEKU"}
# Here a is dictionary in python dictionary start with curly brackets{}
"""Dictionary is collection of key and value pairs"""
print(a)

print(a["key"])
print(a["greet"])
# here this the key and we print the value of key

a["ritik"] = "Gk"
a["Anurag"] = "free fire"
# using this we can add element in dictionary
print(a)

#   using update({key:value}) function we can add elements in dictionary
a.update({"Deva": "free fire pro"})
a.update({"Ayushman": "Too mature"})
print(a)

# using del we can delete or remove elements in dictionary
del a["greet"]
del a["jay"]
print(a)

d1 = a.copy()
del d1["key"]
print(a)
print(d1)

a["bhaji"] = {"free fire": "noob", "cricket": "noob", "pavn": "roll"}

# some times we can make a dictionary inside the dictionary above example
print(a)

d = a
# d is new dictionary and a is our old dictionray
del a["key"]

"""If we copy our dictionary in other dictionary and if we change in other 
dictionary so change also show in our dictionary becloz here other dictionray
is pointer and point to our old dictionay and if we do change new dictionary so 
change also happen in old dictionary so remove this proble we can use copy()
function"""
print(a)
print(d)
# print both dictionary

#   Use the copy function
d2 = a.copy()
# d2 is new and a is old dictionary
del d2["bhaji"]
print(d2)
print(a)
# this time only change happen in new dictionary d2

print(a.keys())
# print all the a dictionary key

print(a.items())
# print all the a dictionary key values or items
