# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 10  # we create this variable to make the program flexible
answer = random.randint(1, highest)   # a class called random that has a method called randint(range)


print("Please guess a number between 1 and {}: ".format(highest))
guess = -1
guess = int(input())    # NB -> need to initialise to any number outside valid range
while (guess != answer) and (guess != 0):
    if guess < answer:
        print("Please guess higher, or to quit press 0")
    else:  # guess must be greater than that number
        print("Please guess lower, or to quit press 0")
    guess = int(input())

else:
    if guess == 0:
        print("Thanks for playing! Quitting game....")
    else:  # guess was correct
        print("Well Done! You guessed it!\n"
              "Thanks for playing! Quitting game....")
