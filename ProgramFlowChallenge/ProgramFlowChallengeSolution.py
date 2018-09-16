ipAddress = input("Please enter your 4 number IP Address separated by '.': ")

if ipAddress[-1] != '.':
    ipAddress += '.'
segment = 1
segmentLength = 0
character = ''

for character in ipAddress:
    if character == '.':
        print("Segment {} contains {} characters". format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1

# unless the final character in the string was a . then we haven't printed the last segment
if character != '.':
    print("Segment {} contains {} characters". format(segment, segmentLength))
