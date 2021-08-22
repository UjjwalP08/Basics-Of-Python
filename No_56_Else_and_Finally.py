"""
        Finally and Else with try exception
"""
f1 = open("try.txt")
try :
    with open("t1.txt") as u:
        pass
except IOError as e:
    print(e)

except EnvironmentError as e:
    print(e)

except EOFError as e:
    print(e)

else:
    print("Execute only when except statement not executed")

finally:
    print("we have to must print this statement")

    f1.close()
# When we print any statement or code to execute forcefully we are
# use the finally keyword
# We can run exception statement n no of times

"""
Else statement run only when the except statement is not execute
"""
print("Important Statements")