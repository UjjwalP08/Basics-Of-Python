"""
            --------------------> Function Caching <---------------------------

some times we are call the same function in program again and again so our time
of program is taken more than expected so reduce this we are use the function
caching

this method is inside the functool module and method is lur_cache

"""
# import time
#
# def work(n):
#     # This is my function of work
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("This is first time")
#     work(3)
#     print("This is Second time")
#     work(3)
#     print("Completed")
#
"""
In this program we are call the work function 2 time but it contain 6 sce but 
suppose if we have call function 10 times so taken time 30 sec that has not mean
to speed for us 

so we want to first store that time value and when we want to that is printed

using this  to or call this is known as function caching 
"""

from functools import lru_cache
import time


@lru_cache(maxsize=10)  # store the capacity of this function call  is 10 now
# for different value of it stores after again call the time is reduce

def work(n):
    # This is my function of work
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("This is first time")
    work(5)
    print("This is Second time")
    work(3)
    print("Completed")
    work(5)
    print("Again")
    work(3)
    print("Again")
    work(4)
    print("call Again")
    work(3)
    print("again call")
    work(4)
    print("Over")

# In this program the file or work function call 6 or 7 time like work(5) and work(3) etc
# after when we call the work(5) 2nd time that is not take 5sec to run it
"""
In simple or gujarati language ma kahu to work(5) 2nd time call thase tyare te 5 sce jetlo time nahi le 
execution mate tevi j rite jo work(3) pacho call thaay to 3 sec nahi le aabadha function only ek j vaar
tema aapeli integer value hisabe run tahvaa mate time lese biji vaar jo te pachu call thay tyare speed ma
execute thasee vadhare samay nahi lee
"""