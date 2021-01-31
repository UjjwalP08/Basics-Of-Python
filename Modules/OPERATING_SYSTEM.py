"""
------------------- Os Module ------------------------
"""
# First import os module. Os module is in-build module

import os

# print(dir(os))  # Give all method,object,attribute list which is inside the os module

# print(os.getcwd())  # Give current working directory location

# os.chdir("c:")  # Use to change the location of directory
# Only editior is change to path origanl path is still same

# print(os.getcwd())

print(os.listdir("d:/"))  # Give a list containing the names of the entries in the directory given by path.

# os.mkdir("New")  # Make new directory automatic in side you folder

# os.makedirs("new/Brand_new/something")
#   make new directory automatic and also a make new directory in side the new directory in side it

# f=open("new.txt")
# pass
#
# f.close()

# os.rename("Navi.txt","New.txt") #Change the name of files


print(os.environ.get("path"))  # Give the path of environmental variable

# os.path.join("") # this function to join the path


print(os.path.exists("C://Program Files"))
# Return true if the path of that directory is exist otherwise return false

print(os.path.isfile("C://Program Files"))
#   Return true if give path has exist files otherwise return false
