import random

def guessing_game():
    
    try:
        guess = int(input('Select a number between 1 and 10\n'))
        magic_number = random.randrange(1, 10, 1)
        print("Your number is {}.".format(guess))
        while guess != magic_number:
            if (guess > 12 ):
                print("You're out of range, try again homie.")
                guess = int(input('Select a number between 1 and 10\n'))
            else:
                print("Try Again womp\n")
                guess = int(input('Select a number between 1 and 10\n'))
        print("Are you a MIND READER??")
        print("The magic number was {}.\n".format(magic_number))

    except:
        print("WHOA.  That's not an integer.  Check yourself and try again.")
        guessing_game()

guessing_game()