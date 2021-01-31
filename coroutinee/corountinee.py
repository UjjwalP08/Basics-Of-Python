"""
------------------------ Coroutine ---------------------------
Coroutines are mostly used in cases of time-consuming programs,
such as tasks related to machine learning or deep learning algorithms
or in cases where the program has to read a file containing a large
number of data


"""
import time


def searcher():  # Coroutine
    book = "This is my book or coroutine program which you want write"

    time.sleep(4)
    # that is time to take read book only 1st time

    while True:
        text = (yield)  # This keyword use to generate value on the fly

        if text in book:
            print("Your Text in the book")
        else:
            print("This Text not inside the book")


# Now we want to run the Coroutine

search = searcher()

# Running coroutine we are use the next() function

next(search)

# Search in the book or coroutine we are use the send() function

search.send("write")
# after search we must close the coroutine for it use close() function
print("Next word")
search.send("this")
input("Press any key:-")
search.send("program")
input("Press any key:-")
search.send("that")
search.close()

"""
coroutine only 1st time to take time search the text, after it only
while loop do it job and find the word without any delay

"""



