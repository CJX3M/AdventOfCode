import openData

useTest = False

matrix = []

input = [l.split(" ") for l in openData.getData(6, useTest)]

for i in range(len(input)):
    input[i] = [x for x in input[i] if x != '']

rotateMatrix = []

for i in range(len(input[0])):
    newRow = []
    for j in range(len(input)):
        newRow.append(input[j][i])
    rotateMatrix.append(newRow)

results = []
for row in rotateMatrix:
    operation = row[-1]
    value = 0
    for val in row[:-1]:    
        if operation == "+":
            value += int(val)
        elif operation == "*":
            if value == 0:
                value = 1
            value *= int(val)
    results.append(value)

print("Part 1:", sum(results))

input = openData.getData(6, useTest)
offset = 0
row = []
currentCol = 0
colOffsets = []

for cIndex, c in enumerate(input[-1]):
    offset += 1
    if cIndex == len(input[-1]) - 1:
        colOffsets.append(offset)
        break
    if c == " " and input[-1][cIndex + 1] != " ":
        colOffsets.append(offset)
        offset = 0

for offset in colOffsets:  
    for line in input:
        row.append(line[currentCol:currentCol + offset][::-1])
    matrix.append(row)
    row = []
    currentCol += offset

results = []

for line in matrix:
    values = []
    for currCol in range(len(line[0])):
        value = ''
        for col in line:
            c = col[currCol]
            if c == " ":
                continue
            elif c in ["+", "*"]:
                if value != '':
                    values.append(int(value))
                    value = ''
                if c == "+":
                    results.append(sum(values))
                else:
                    results.append(eval('*'.join(map(str, values))))
            else:
                value += c
        if value != '':
            values.append(int(value))
    

print("Part 2:", sum(results))

