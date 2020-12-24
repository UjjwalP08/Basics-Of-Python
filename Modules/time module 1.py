import time

"""
time.time()function
time.sleep() function
time.asctime() function
time.localtime() function
"""
initaltime=time.time()

# time.time() fumction show time

print(initaltime)

k=0

while(k<45):
    k+=1
    print("This is code")
    time.sleep(2)#Using to sleep time
    #mean loop start thase code run thase pachi biji vaar 2sec pachi pachi execute thasee
print("while loop running time is ",time.time()-initaltime,"Seconds")

t=time.time()

for i in range(45):
    print("This is code")

print("While loopp running time is ",time.time()-t,"Seconds")

currenttime=time.asctime(time.localtime(time.time()))

print(currenttime)