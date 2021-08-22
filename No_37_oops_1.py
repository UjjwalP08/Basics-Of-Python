"""
Instance Variable:- Variable of object is known as ....

class Variable:- Variable of class is known as ..........
"""


class Student:
    pass #pass means nothing it means our class or function is empty
        #and if we write pass so it is valid

harry=Student()#Object of Class

ujjwal=Student()#Object of class

print(harry,ujjwal) #print its location in memory

harry.name="Harry"
harry.std=12    #Instance Variables of Object which name is Harry
harry.steam="Science"

ujjwal.name="Ujjwal"
ujjwal.std="clg" #Instance Variables of Object which name is ujjwal
ujjwal.steam="IT"

print(harry.name,harry.steam ,"\n",ujjwal.name,ujjwal.steam)