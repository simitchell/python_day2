def start_end():
    start = int(input("What number shall we begin with?\n"))
    end = int(input("Awesome.  We'll start with {}.  What shall we end with? \n".format(start)))
    for x in range(start, end, 1):
        print(x)

start_end()