"""
Class Method As Alternative Constructor

In this program we can create object using function and passes only one
argument

"""
class emempolyee:

    leaves=9

    def __init__(self,aname,astd,role,staem):

        self.name=aname
        self.std=astd
        self.role=role
        self.steam=staem

    def detail(self):
        return  f"This mr {self.name} " \
                f" my level is {self.std} " \
                f"and steam is {self.steam} and role is {self.role} "

    @classmethod # Decorator

    def change_leaves(cls,updated):
        """A function which is change leaves"""

        cls.leaves=updated

    @classmethod
    def das(cls,str):

        # v=str.split("-")
        # print(v)
        # return cls(v[0],v[1],v[2],v[3])
        return cls(*str.split("-"))#this line work same as above 3 line
    """
    split() function use split the string with as the argument and convert it
    in list
    """


    @classmethod
    def slash(cls,string):

        return cls(*string.split("/"))


harry=emempolyee("harry","12","Student","Science")#Total 3 argument
ujjwal=emempolyee("ujjwal","Clg","Coder","IT")#Total 3 argument

rahul=emempolyee.das("Rahul-12-worker-nothing")

mehul=emempolyee.das("Mehul-10-student-school")
# print(rahul.name)

print(rahul.detail())
print(mehul.detail())

deva=emempolyee.slash("Dev/10/student/owner")

golu=emempolyee.slash("Golu/diploma/student/engineer")

print(deva.detail())
print(golu.detail())