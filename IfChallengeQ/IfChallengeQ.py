# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("What is your name? ")
age = int(input("How old are you, {0}? ".format(name)))

if (age > 17) and (age < 31):
    print("Welcome to the legally under 30s Holiday, {}!".format(name))
else:
    print("Unfortunately {}, you do not meet the age criteria for this holiday".format(name))
    if age < 18:
        print("Please come back when you are 18 to join the fun!")
    else:
        print("Please look at our over 30s Holiday Packages!")

