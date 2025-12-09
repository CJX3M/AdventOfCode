import openData

input = openData.getData(6, True)

offset = 0

matrix = []
row = []
currentCol = 0
while currentCol < len(input[:-1]):
    #usar la ultima linea de input para determinar el offset
    for line in input:
        if offset == 0:
            for cIndex, c in enumerate(line):
                if c == " ":
                    offset += 1
        row.append(line[currentCol:currentCol + offset])
        # for c in range(0, len(line), offset + 1):
        #     marker = line[c:offset + c]
        #     row.append(marker)

    matrix.append(row)
    currentCol += offset + 1
    offset = 0
print(matrix)    
        


# input = [l.split(" ") for l in openData.getData(6, False)]

# for i in range(len(input)):
#     input[i] = [x for x in input[i] if x != '']

# rotateMatrix = []

# for i in range(len(input[0])):
#     newRow = []
#     for j in range(len(input)):
#         newRow.append(input[j][i])
#     rotateMatrix.append(newRow)

# results = []
# for row in rotateMatrix:
#     operation = row[-1]
#     value = 0
#     for val in row[:-1]:    
#         if operation == "+":
#             value += int(val)
#         elif operation == "*":
#             if value == 0:
#                 value = 1
#             value *= int(val)
#     results.append(value)

# print("Part 1:", sum(results))

