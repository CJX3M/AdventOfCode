import openData
import time

useTest = False
input = [list(l) for l in openData.getData(7, useTest)]

startPos = input[0].index('S')
input[1][startPos] = '|'

splits = 0
for rIndex, row in enumerate(input[1:]):
    for cIndex, c in enumerate(row):
        if c == '^':
            if input[rIndex][cIndex] == '|':
                input[rIndex+1][cIndex-1] = '|'
                input[rIndex+1][cIndex+1] = '|'
                splits += 1
        if c == '.' and input[rIndex][cIndex] == '|':
            input[rIndex+1][cIndex] = '|'
    print(''.join(input[rIndex]))
    
print("Part 1:", splits)
Part2 = ''
print("Part 2:", Part2)
