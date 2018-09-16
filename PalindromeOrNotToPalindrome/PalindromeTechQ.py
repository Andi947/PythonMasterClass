
print("Please enter a word for the palindrome tester: ")
firstWord = input().lower()
# firstWord = input().lower().replace(' ', '').replace(',', '').replace('!', '').replace('-', '').replace('.', '')\
#     .replace('/', '').replace("'", '')

firstWordEdit = ''
for i in firstWord:
    if i in "abcdefghijklmnopqrstuvwxyz":
        firstWordEdit += i
    else:
        continue

newWord = ''
print(firstWordEdit)

while newWord == "":
    if firstWordEdit != "":
        for i in reversed(firstWordEdit):
            # print(i)
            newWord += i
        print(newWord)
    else:
        while firstWordEdit == "":
            print("Please enter a word: ")
            firstWord = input().lower()
            for i in firstWord:
                if i in "abcdefghijklmnopqrstuvwxyz":
                    firstWordEdit += i
                else:
                    continue

if newWord == firstWordEdit:
    print("Is a palindrome")
else:
    print("Is not a palindrome")

# if newWord == firstWord:
#     print("{} is a palindrome".format(firstWord))
# else:
#     print("{} is not a palindrome".format(firstWord))



