import numpy
from numpy.core.fromnumeric import sort
from openData import getData

def createOutPut(seg, output, sort, reverse):
        # Create the segment for 1
    #  ..
    # .  1
    # -  1
    #  ..
    # .  1
    # -  1
    #  ..
    one = [s for s in seg if len(s) == 2][0]
    if sort:
        one = sorted(one)
    if reverse:
        one = sorted(one)[::-1]
    output[1][3] = one[0]
    output[2][3] = one[0]
    output[4][3] = one[1]
    output[5][3] = one[1]
    # Create the segment for 7
    #  77
    # .  1
    # -  1
    #  ..
    # .  1
    # -  1
    #  ..
    seven = [s for s in seg if len(s) == 3][0]
    for char in seven:
        if (output[1][3] != char 
            and output[2][3] != char 
            and output[4][3] != char 
            and output[5][3] != char):
            output[0][1] = char
            output[0][2] = char
    # Create the segment for 4
    #  77
    # 4  1
    # 4  1
    #  44
    # .  1
    # -  1
    #  ..
    four = [s for s in seg if len(s) == 4][0]
    # lets get 2, 3 and 5
    five = [s for s in seg if len(s) == 5]
    for char in four:        
        if (output[0][1] != char and output[0][2] != char 
            and output[1][3] != char and output[2][3] != char 
            and output[4][3] != char and output[5][3] != char):
            matches = [f for f in five if char in f]
            if len(matches) == 3:
                output[3][1] = char
                output[3][2] = char
            else:
                output[2][0] = char
                output[1][0] = char  
    # Close the output with 2 and 5
    #  77
    # 4  1
    # 4  1
    #  44
    # 2  1
    # 2  1
    #  25
    for elem in five:
        for char in elem:
            if (output[0][1] != char and output[0][2] != char 
            and output[1][3] != char and output[2][3] != char 
            and output[4][3] != char and output[5][3] != char
            and output[3][1] != char and output[3][2] != char
            and output[2][0] != char and output[1][0] != char):
                matches = [f for f in five if char in f]
                if len(matches) == 3:
                    output[6][1] = char
                    output[6][2] = char
                if len(matches) == 1:
                    output[4][0] = char
                    output[5][0] = char
    
    return output

def getDigits(output, numbers):
    # create patterns for 2, 3, 5, 6, 9, and 0
    patterns = [
        {"pattern": output[0][1] + output[1][3] + output[3][1] + output[4][0] + output[6][1], "digit": "2"},
        {"pattern": output[0][1] + output[1][3] + output[3][1] + output[4][3] + output[6][1], "digit": "3"},
        {"pattern": output[0][1] + output[1][0] + output[3][1] + output[4][3] + output[6][1], "digit": "5"},
        {"pattern": output[0][1] + output[1][0] + output[3][1] + output[4][3] + output[6][1] + output[4][0], "digit": "6"},
        {"pattern": output[0][1] + output[1][0] + output[3][1] + output[1][3] + output[4][3] + output[6][1], "digit": "9"},
        {"pattern": output[0][1] + output[1][0] + output[1][3] + output[4][0] + output[4][3] + output[6][1], "digit": "0"},
    ]
    digits = []
    for number in numbers:
        if len(number) == 2:
            digits.append("1")
        elif len(number) == 3:
            digits.append("7")
        elif len(number) == 4:
            digits.append("4")
        elif len(number) == 7:
            digits.append("8")
        else:
            for pattern in [p for p in patterns if len(p["pattern"]) == len(number)]:
                sortedNumber = sorted(number)
                sortedPattern = sorted(pattern["pattern"])
                if sortedNumber == sortedPattern:
                    digits.append(pattern["digit"])
    return digits
    


data = [i.split('|') for i in getData("day8.txt")]

# Part 1
correctDigits = 0

for i in data:
    correctDigits += len([m for m in i[1].split() if len(m) == 2 or len(m) == 3 or len(m) == 4 or len(m) == 7])

print("Part 1: ", correctDigits)

# Part 2

emptyOutput = [["." for c in range(4)] for r in range(7)]

digits = []
for i in data:
    tries = 0
    segmentDigits = []
    while len(segmentDigits) != 4:
        seg = i[0].split()
        output = createOutPut(seg, emptyOutput, tries == 0, tries == 2)
        numbers = i[1].split()
        segmentDigits = getDigits(output, numbers)
        tries += 1
        if tries == 3 and len(segmentDigits) != 4:
            print(seg)
            exit()
    segmentDigits = int("".join(segmentDigits))    
    digits.append(segmentDigits)


print("Part 2: ", sum(digits))
