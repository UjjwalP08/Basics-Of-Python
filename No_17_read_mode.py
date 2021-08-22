f = open("u.txt", "rt")

# print(f.readline())#this statement print u.txt files 1st line
# print(f.readline())#this statement not print u.txt files 1st line but print after that line
# print(f.readline())

# stuff=f.read()
# print(f.readline())#now this statement not print becoz stuff variable is read whole
# file becoz of that we can't read file becoz file is already readed
# print("You file statments are \n",stuff)

# stuff=f.read(2)
# print("1", stuff)#only print becoz we oreder to read only 2 characters
#
# stuff=f.read(2)
# print("2", stuff)#print after 2 character above statements


# for line in f:
#     print(line, end=" ")
print(f.readlines())#Give our statements in list form

f.close()
