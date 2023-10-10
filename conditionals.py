import random

def guessing_game():
    guess = input('Select a number between 1 and 10\n')
    magic_number = random.randrange(1, 10, 1)
    print("Your number is {}.".format(guess))
    if (int(guess) > 12 ):
        print("You're out of range, try again homie.")
    elif (int(guess) == magic_number):
        print("Are you a MIND READER??")
        print("The magic number was {}.\n".format(magic_number))
    else:
        print("Try Again womp")
        print("The magic number was {}.\n".format(magic_number))

guessing_game()