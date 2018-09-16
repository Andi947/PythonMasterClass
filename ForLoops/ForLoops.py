# for i in range(1, 20):  # [1, 20) -> doesn't include 20
#     print("i is now {0}".format(i))
# print()

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ""
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber += number[i]
# newNumber = int(cleanedNumber)  # being performed once is better than putting it in loop
# print("The number is {}".format(newNumber))

number = "9,223,372,036,854,775,807"
cleanedNumber = ""

for char in number:    # because a string is a sequence
    if char in '0123456789':
        cleanedNumber += char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)
    # print("This parrot is {}".format(state))

for i in range(0, 100, 5):
    print("i is {}".format(i))

for i in range(1, 13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j), end='\t')
    # print("================")
    print('')
