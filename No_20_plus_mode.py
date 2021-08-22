"""
In plus mode we can perform read and write both operations
"""

u=open("u.txt","r+")

me=u.read()
# read() function use to read the data in the file
print(me)
# u.write(" Enter data in file")
#first this function add statement in file after we can execute it

u.close()