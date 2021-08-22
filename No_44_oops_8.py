"""
Inheritance:-it means use the property of other class

Multi-level Inheritance:-
"""

class Grandfather:# Class 1
    cricket_win_games=1

    def win1(self):
        return f"win games in cricket is {self.cricket_win_games}"

class Father(Grandfather):# Class 2
    cricket_win_games=5
    football_win_games=6

    def win1(self):
        return f"win games in cricket is {self.cricket_win_games}"
    def win2(self):
        return f"win games in football is {self.football_win_games}"

class Son(Father):# Class 3
    cricket_win_games=8
    football_win_games=10
    pubg_win_games=20

    def win1(self):
        return f"win games in cricket is {self.cricket_win_games}"

    def win2(self):
        return f"win games in football is {self.football_win_games}"

    def win3(self):
        return f"win games in pubg is {self.pubg_win_games}"

dadaji=Grandfather()

papaji=Father()

beta=Son()

print("\t\tIn Cricket")
print("Dadaji ",dadaji.win1())
print("Papaji",papaji.win1())
print("Dikro",beta.win1())
print()
print("\t\tIn Football")
# print("Dadaji",dadaji.win2())#Give Error
print("Papaji",papaji.win2())
print("Dikro",beta.win2())
print()
print("\t\tIn Pubg")
# print("Dadaji",dadaji.win3())#Give Error
# print("Papaji",papaji.win3())#Give Error
print("Dikro",beta.win3())

"""
Best Example of Multi-level Inheritance is

son use the property of his father as well as use the property of his grandfather

Note:-But Grandfather not use the property of son and grand son
      As well as father is not use the property of son
"""
