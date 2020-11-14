
# In python Index start with o
mystr ="You can do it"
my ="yahoothis"
print(mystr  )  # print whole string
print(len(mystr)  )# print length of string
print(type(mystr)  )# print type of varible
print(mystr[5]  )# print index 5 element of string which is a
print(mystr[0:5])
"""only print You c becoz here 0 is including but 5 is excluding"""
print(mystr[0:12])
"""only print You can do i becoz here 0 is including but 12
 is excluding"""
print(mystr[0:13])# String Slicing
print(mystr[:5]  )# Automatic count index o so print You c
print(mystr[1:]  )# Automatic count all end index
# print ou can do it becoz we start wit index 1
print(mystr[0:12:1])
"""we know mystr[0:12] print You can do but last :1 use to skip 
character 1"""
print(mystr[0:13:2])
"""we know mystr[0:12] print You can do but last :2 use to skip 2
character so it is print Yucnd t """
# means last part(:2) use to skip elements
print(mystr[::]  )  # this is automatic detect index 0 to 12
"""mean total 13 elements in the string so it is automatic detect index 0
to index 12 and skip the 1 element"""
print(mystr[-1])
"""print the index 12 element if we reverse and start with
 -1 so t will printed and if we write mystr[12] also t is printed"""
print(mystr[::-1])
"""this is first reverse string then skip 1 character"""
print(mystr[::-2])
"""this is first reverse string then skip 2 characters 
so print t dncuY"""
# isalnum() function
print(mystr.isalnum()  )  # return true if string is alphanumeric
# alphanumeric:-The string without white space
print(my.isalnum())
# retun true
# isalpha() function
print(mystr.isalpha()  )  # return trur if all chracter is alphabet without
# white space
print(my.isalpha())

# endwith() function
print(mystr.endswith("it"))
# return true if enter string is actually end with this string
print(mystr.endswith("you"))

#   count() function
print(mystr.count("o"))
# return intger value of character how many time use in the string

#   capitalize() function
print(mystr.capitalize())
# Make first letter to captial case

# upper() and lower() function
print(mystr.upper()  )# convert full string in capital case
print(mystr.lower()  )  # convert full string in lower case

#   find() function
print(mystr.find("u"))
# return integer value of letter how many time comes in string

# replace() function
print(mystr.replace("You" ,"I"))
# replace word in strin replace("old word","new word


