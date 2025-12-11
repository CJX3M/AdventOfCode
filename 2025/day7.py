from functools import lru_cache
import openData

def searchTimeLines(currentGrid, currentPosition):
    rIndex, cIndex = currentPosition
    @lru_cache(maxsize=None)
    def performDFS(rIndex, cIndex, searchLeft):
        if rIndex == len(currentGrid):
            return 1
        if currentGrid[rIndex][cIndex] == '^':
            if searchLeft:
                return (performDFS(rIndex, cIndex-1, True) +
                        performDFS(rIndex, cIndex+1, False))
            else:
                return performDFS(rIndex, cIndex+1, False)
        if currentGrid[rIndex][cIndex] == '.':
            return performDFS(rIndex+1, cIndex, True)
        else:
            return 0
    return performDFS(rIndex, cIndex, True)

useTest = True
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
    

input = [list(l) for l in openData.getData(7, useTest)]
timeLines = searchTimeLines(input, (1, startPos))

print("Part 1:", splits)
print("Part 2:", timeLines)
