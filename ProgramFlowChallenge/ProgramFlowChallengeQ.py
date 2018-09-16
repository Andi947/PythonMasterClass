# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
# 127.0.0.1
# .192.168.0.1
# 10.0.123456.255
# 172.16
# 255
#
# So your program should work even with invalid IP addresses. We're just interested in the number of segments
# and how long each one is
#
# Once you have a working program, here are some more suggestions for invalid input to test
# .123.45.678.91
# 123.4567.8.9.
# 123.156.289.10123456
# 10.10t.10.10
# 12.9.34.6.12.90
# '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/e;se statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.

ipAddress = input("Please enter your 4 number IP Address separated by '.': \n")
noOfSegments = 0
lengthOfSegment = 0
ipAddressSegLengths = []
i = ""
seg = ''

for i in ipAddress:
    if i == ".":
        noOfSegments += 1
        ipAddressSegLengths += str(lengthOfSegment)
        lengthOfSegment = 0
        seg = ''
    else:
        lengthOfSegment += 1
if i != '.':
    lengthOfSegment = 0
    lengthOfSegment += len(seg)
    ipAddressSegLengths += str(lengthOfSegment)

print("The IP Address {0} has {1} segments.".format(ipAddress, noOfSegments))
print("They are of the following lengths: {}".format(ipAddressSegLengths))

