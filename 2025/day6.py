import openData

input = openData.getData(6, True)

offset = 0

for line in input:
    for c in line:
        if c != " ":
            offset += 1
        else:
            break
    
        


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

