""" 

        -----------> In build Moudle in Python:-

            --->Module Name:- Module Purpose

                calendar:- used in case we are working with calendars

                random:-used for generating random numbers within certain defined limits

                enum:- used while working with enumeration class

                html:-for handling and manipulating code in HTML

                math:- for working with math functions such as sin, cos, etc.

                runpy:- runpy is an important module as it locates and runs python modules without importing them first

 """

import random  # inbuild module in python

num=random.randint(0,100)#genratae random no between 0 to 100

num = random.random() * 100  # Genrate random no between 0 to 100

print(num)

l = [["Detective Conan", "Conan"], ["Solo leveling", "Unknown"], ["My Hero Academia", "Deku"],
     ["One punch man", "Saitama"]
    , ["City Hunter", "Saeba-san"]]

u = random.choice(l)

print(u)

n = random.randbytes(9)  # this function genratae n no of random bytes

print(n)
import calendar

print("Your Calender\n \n ")

y = int(input("Enter the Year : "))
m = int(input("Enter the month : "))

mycalender = calendar.month(y, m)
print("\n", mycalender)

