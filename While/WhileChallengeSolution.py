import random

highest = 1000  # we create this variable to make the program flexible
answer = random.randint(1, highest)   # a class called random that has a method called randint(range)

# THERE is a way to guess within 10 guesses no matter what the range

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Thanks for playing! Quitting game....")
        break
    if guess < answer:
        print("Please guess higher, or to quit press 0")
    elif guess > answer:  # guess must be greater than that number
        print("Please guess lower, or to quit press 0")
    else:  # guess was correct
        print("Well Done! You guessed it!")
