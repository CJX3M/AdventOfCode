from os import error
from openData import getData

data = getData("day10.txt")

opening = ["{", "[", "(", "<"]
closing = ["}", "]", ")", ">"]

def checkChar(chars, index):
    if index >= len(chars):
        return ('', 0)
    char = chars[index]
    charIndex = index
    error = ""
    while index < len(chars):
        nextChar = ""
        if char in opening:
            nextChar, currentIndex = checkChar(chars, index+1)
            if currentIndex == 0:
                if char == "{":
                    nextChar += "}"
                elif char == "[":
                    nextChar += "]"
                elif char == "(":
                    nextChar += ")"
                elif char == "<":
                    nextChar += ">"
                return (nextChar, 0)
        elif char in closing:
            return (char, index)
        if (nextChar == '.'):
            index = currentIndex
            continue
        if char == "{" and nextChar != "}":
            error = "Expected } but found " + nextChar
        elif char == "[" and nextChar != "]":
            error = f"Expected ] but found {nextChar}"
        elif char == "(" and nextChar != ")":
            error = f"Expected ) but found {nextChar}"
        elif char == "<" and nextChar != ">":
            error = f"Expected > but found {nextChar}"
        if error:
            raise Exception(error, nextChar)
        if charIndex == 0 and index < len(chars):            
            return checkChar(chars, index+2)
        return ('.', index+1)

illegal = []
completed = []

for line in data:
    try:
        complete = checkChar(line, 0)        
        completed.append(line + "-" + complete[0])
    except Exception as error:
        if "Expected" in error.args[0]:
            illegal.append(error.args[1])        

sum = 0
for i in illegal:
    if i == ")":
        sum += 3
    elif i == "]":
        sum += 57
    elif i == "}":
        sum += 1197
    elif i == ">":
        sum += 25137
print(sum)

sums = []
for c in [c.split("-")[1] for c in completed if "-" in c]:
    sum = 0
    for i in c:
        sum = sum * 5
        if i == ")":
            sum += 1
        elif i == "]":
            sum += 2
        elif i == "}":
            sum += 3
        elif i == ">":
            sum += 4
    sums.append(sum)
sums = sorted(sums)

print(sums[int(len(sums)/2)])

