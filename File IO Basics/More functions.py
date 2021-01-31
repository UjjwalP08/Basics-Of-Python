f  = open("u.txt")

""""
tell() function use to knew that where is our file pointer or 
what is current location of our file pointer
or which of character in our file pointer


seek() function use to set the file pointer as our wish location

in simple language ke aade je character thi start karvu hoy te tala no lakhi deva after that we
can show the magic 
"""

print(f.readline())

print(f.tell())

print(f.readline())

f.seek(21)

print(f.tell())

print(f.readline())

print(f.tell())

f.close()
