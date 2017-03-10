greeting = "Bruce"
_myName = "Tim"
# 1Tim = "Not good" -> can't write like this
Tim45 = "Good"  # but we can do this
Tim_Was_57 = "Hello"  # is also okay
Greeting = "There"  # upper case is treated as a different variable name to greeting
# print(Tim_Was_57 + " " + greeting)
#
# age = 24
# print(age)

# print(greeting + age) -> doesn't work because one is an int and another is a str

a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # answer returned as a float always
print(a // b)  # returns answer as an int
print(a % b)

print()

for i in range(1, 4):
    print(i)

# for i in range(1, a/b):  # float obj cannot be interpreted as an int
#     print(i)

for i in range(1, a//b):  # a range requires an integer
    print(i)


print(a + b / 3 - 4 * 12)  # BODMAS - b/3 ; 4*12 -> 12 + 1 - 48 = -35
print(((a+b)/(3-4))*12)  # / automatically converts to float
print((((a + b) / 3) - 4) * 12)
print(8 / 2 * 3)
print(8 // 2 * 3)

print()

c = a + b
d = c / 3
e = d - 4
f = e * 12
print(f)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])  # prints the 4th character; list with indices for characters
print(len(parrot))  # prints the length of the string
print(parrot[-1])  # counts from the end of the string
print(parrot[0:6])  # [0 to 6)
print(parrot[:6])   # [beginning to 6)
print(parrot[6:])   # [6 to end)
print(parrot[-4:-2])  # [-4 = B to -2) = before u; therefore Bl
print(parrot[0:6:2])    # go from [0 to 6) and print every 2nd incl 0 (0, 2, 4) = (Nre)

number = "9,223,372,036,854,775,807"
print(number[1::4])  # returns all the ,

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])  # extracted numbers and avoided commas and spaces

string1 = "he's "
string2 = "probably"
print(string1 + string2)
print("he's " "probably " "pining")  # adds string together

print("Hello " * 5)
# print("Hello " * 5 + 4)  # can't convert int to string
print("Hello " * (5 + 4))

today = "Friday"
print("day" in today)  # true or false if string is in word saved in variable
print("Fri" in today)
print("thursday" in today)
print("parrot" in "fjord")
print("real" in "really")  # can also be done on a word







