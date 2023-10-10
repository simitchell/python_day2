# def start_end():
#     start = int(input("What number shall we begin with?\n"))
#     end = int(input("Awesome.  We'll start with {}.  What shall we end with? \n".format(start)))
#     for x in range(start, end, 1):
#         print(x)

# start_end()

import re

def multi_condition():
    myString = input("Give me two words, they must total 16 characters or more. \n")
    counter = 0
    if (len(myString) < 16):
        print("Not enough characters, my dude.\n")
        multi_condition()
    elif (bool(re.search(r"\s", myString))):
        print("There is a space in the string")
    else:
        while counter < len(myString):
            for x in myString:
                counter += 1
            print(counter)
    

multi_condition()