import os
import sys

data = ""

strPath = os.path.join(sys.path[0], "day1Input.txt")
with open(strPath) as fileObject:
    data = fileObject.read().split('\n')

# Part 1
def part1(data):
    current = 0
    previous = 0
    increased = 0
    for number in data:
        current = int(number)
        if previous != 0:
            if current > previous:
                increased += 1
        previous = current

    print(increased)

# Part 2
def part2(data):
    startIndex = 0
    endIndex = 3
    chunks = []
    while endIndex <= len(data) and startIndex <= endIndex:
        chunks.append(data[startIndex:endIndex])
        startIndex += 1
        if endIndex < len(data):
            endIndex += 1

    current = 0
    previous = 0
    increased = 0
    for chunk in chunks:
        current = sum(int(item) for item in chunk)
        if previous != 0:
            if current > previous:
                increased += 1
        previous = current
    print(increased)

part1(data)
part2(data)