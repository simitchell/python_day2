# def reverse_list():
#     numbers = [1, 2, 3, 4, 5, 99, 2600, 300]
#     print(numbers)
#     reversed_list = reversed(numbers)
#     print(list(reversed_list))

# reverse_list()

# def string_to_list():
#     myString = "teriyaki"
#     # print(myString)
#     myList = []
#     for char in myString:
#         myList.append(char)
#     print(myList)
#     reversed_list = reversed(myList)
#     print(list(reversed_list))

# string_to_list()

def g_n_r():
    band = ["Axl", "Slash", "Izzy", "Duff", "Steven"]
    audition = input('Who do you think should be in the band? \n')
    if audition in band:
        band.remove(audition)
        print('{} screwed up.  They are fired!\n'.format(audition))
    else:
        band.append("{}".format(audition))
        print("{} just got hired by the band.\n".format(audition))
    print(band)

g_n_r()
