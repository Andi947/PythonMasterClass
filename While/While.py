for i in range(10):
    print("i is now {}".format(i))

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

availableExits = ["east", "north east", "south"]

chosenExit = ""
while chosenExit not in availableExits:
    chosenExit = input("Please choose a direction: ")
    if chosenExit == "quit":
        print("Game Over")
        break
else:
    print("Aren't you glad you got out of there!")
