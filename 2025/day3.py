import openData

input = openData.getData(3, False)
input = [list(map(int, list(line))) for line in input]

values = []
switches = []
for volt in input:
    maxValue = max(volt[:-1])
    maxValueIndex = volt.index(maxValue)
    restOfValue = volt[maxValueIndex+1:]
    secondMax = max(restOfValue)

    values.append((maxValue * 10) + secondMax)

    switch = []
    value = 0
    for i in range(-12+1, 1, 1):
        offset = i  if i != 0 else None
        digit  = max(volt[:offset])
        value = (value * 10) + digit
        volt = volt[volt.index(digit) + 1:]
    switches.append(value)

print("Part 1 result: ", sum(values))
print("Part 2 result: ", sum(switches))
