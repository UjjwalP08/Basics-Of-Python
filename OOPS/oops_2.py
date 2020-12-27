# class employee:
#
#     leaves=8 #Class Variable
#
#
#     def detail(self): #Here self means object name which is passes
#
#         return  f"This mr {self.name} " \
#                 f"my level is {self.std} and steam is {self.steam} "
#
#
#
# harry = employee()
# ujjwal = employee()
#
#
# harry.name="Harry"
# harry.std=12    #Instance Variables of Object which name is Harry
# harry.steam="Science"
#
# ujjwal.name="Ujjwal"
# ujjwal.std="clg" #Instance Variables of Object which name is ujjwal
# ujjwal.steam="IT"
#
# # print(harry.detail())
#
# print("The leaves of harry is ", harry.leaves)
#
# print("The leaves of ujjwal is ", ujjwal.leaves)
#
# #If we wish to change the leaves of class we are not able to change
#
# #Suppos we wrtie
#
# harry.leaves=9 # this is not change in classs variable but create new instance
# #variable of object which name is harry
#
# print(harry.leaves)
#
# print(harry.__dict__)#In this printed statement u show the leaves as variable
#
#
# print(employee.leaves)#Employee class variable is not changed
#
# print(employee.__dict__)
# #In this print statement u show the leaves orignal value
#
# # class variable is only changed by only its class
# employee.leaves=45
#
# print(employee.leaves)
# print(employee.__dict__)
# print(ujjwal.leaves)

"""
Suppose we want to make an object an passing the argument so not always
make to instance variable so doing this using "init " function
"""

class emempolyee:

    def __init__(self,aname,astd,role,staem):
        self.name=aname

        self.std=astd

        self.role=role

        self.steam=staem

    def detail(self):
        return  f"This mr {self.name} " \
                f" my level is {self.std} " \
                f"and steam is {self.steam} and role is {self.role} "




harry=emempolyee("harry","12","Student","Science")
ujjwal=emempolyee("ujjwal","Clg","Coder","IT")


# harry.name="Harry"
# harry.std=12    #Instance Variables of Object which name is Harry
# harry.steam="Science"

#  Without using it print object values

# ujjwal.name="Ujjwal"
# ujjwal.std="clg" #Instance Variables of Object which name is ujjwal
# ujjwal.steam="IT"

print(ujjwal.detail())
print(harry.detail())