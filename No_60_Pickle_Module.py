"""
----------------------------- Pickle Module ---------------------------
pickle module use to store data or preserve the data in file form and using when use it
"""

import pickle

# #   For create file
# cars = ["BMW","Audi","Ferrari","Bugatti","Volkswagen","Skkoda"]
#
# file = "mycars.pkl"
#
# fileobj = open(file,'wb')   #   Open file in binary mode
#
# pickle.dump(cars,fileobj)
#
# fileobj.close()


#   For fetch file

file = "mycars.pkl"

fileobj = open(file,'rb')

my_cars = pickle.load(fileobj)

print(my_cars)
print(type(my_cars))

fileobj.close()


