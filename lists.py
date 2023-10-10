# def reverseList():
#     numbers = [1, 2, 3, 4, 5, 99, 2600, 300]
#     print(numbers)
#     reversed_list = reversed(numbers)
#     print(list(reversed_list))

# reverseList()

def stringToList():
    myString = "teriyaki"
    # print(myString)
    myList = []
    for char in myString:
        myList.append(char)
    print(myList)
    reversed_list = reversed(myList)
    print(list(reversed_list))

stringToList()
