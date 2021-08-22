"""
Inheritance:-it means use the property of other class

Multiple Inheritance:-One class use to property of more than one class
"""

class employee:#Class 1
    leaves=6
    a=7

    def __init__(self,n,s,r):
        self.name=n
        self.salary=s
        self.role=r

    def details(self):
        return f"He is mr {self.name} and him salary is {self.salary} and its" \
               f" role is {self.role}"


class player:# class 2
    a=8
    games=5

    def __init__(self,na,ga):
        self.name=na
        self.game=ga

    def det(self):
        return f"The player name is {self.name} and game is {self.game}"

"""
Here the order priority is main thing because here in coolguy class employee class is first
and player class is second so if coolguy has not his own constructor so he use 
employee class constructor and follow all of his conditon

but if player class is first so it is follow fistly all the property of player
class than follow employee but if he has not property in his side

priority :- first follow all his property 
    than follow " class class_name(first follow this class,then follow this class)"
"""

class coolguy(employee,player):
    lanuage=["Cpp","Python","Ruby"]
    # a=9
    def lan(self):
        print(f"The language he knew is {self.lanuage}")


harry=employee("Harry",4000,"Programmer")
ujjwal=employee("Ujjwal",5644,"Coder")
raj=coolguy("Raj",56404,"Intern")
# karan=coolguy("karan",["cricket","footbll","Rugby","Basket Ball"])
# raj=coolguy()

# print(harry.details())
# print(ujjwal.details())
# print(karan.det())

# karan.lan()
# raj.lan()

print(raj.a)

# print(karan.a)
"""

In this statement coolguy class has a variable But if he has not a variable in its
own class so he follow the priority order of Inheritance here order is
(employee,player) so now check in employee class if a variable is not inside
employee class so now check in player class and after find it print it

But if priority order is like(player,employee) so first check in player class
then check in employee class

Best Example of Multiple Inheritance is

Sunny Deol who is actor as well as politician
"""