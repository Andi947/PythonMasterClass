# age = int(input("How old are you? "))
# if (age >= 16) and (age <= 65):   # both had to be true
#if 16 <= age <= 65:
# if 15 < age < 66:
#     print("Have a good day at work")
#
# if (age < 16) or (age > 65):        # if either are true
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

# x = "false"
# if x:
#     print("x is true")
#
#
# x = input("Please enter some text: ")
# if x:
#     print("You have entered '{}'".format(x))
# else:
#     print("You did not enter anything")
#
# print(not False)
# print(not True)
#
# print()
#
# age = int(input("How old are you? "))
#
# if not(age<18):
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18-age))

parrot = "Norwegian Blue".upper()
letter = input("Enter a character: ").upper()

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me a {}, Bob".format(letter))

