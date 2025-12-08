import openData

input = [list(l) for l in openData.getData(4, False)]

rollOfPaper = '@'
emptySpace = '.'

directions = [[-1, -1],[-1, 0],[-1, 1],
              [0, -1], [0, 1],
            [1, -1],[1, 0],[1, 1]]

maxLines = len(input)
maxCols = len(input[0])
iters = []

while True:
    canMove = 0
    for lineIndex, line in enumerate(input):
        rollsInLine = [colIndex for colIndex, char in enumerate(line) if char == rollOfPaper]

        for colIndex in rollsInLine:
            cr, cc = [lineIndex, colIndex]
            rolls = 0
            for dr, dc in directions:
                nr, nc = [cr + dr, cc + dc]

                if 0 <= nr < maxCols and 0 <= nc < maxLines:
                    currChar = input[nr][nc]
                    rolls += 1 if currChar == rollOfPaper or currChar == 'X'  else 0

            if rolls < 4:
                input[cr][cc] = 'X'
                canMove += 1
    
    if canMove > 0:
        iters.append(canMove)
        for lineIndex, line in enumerate(input):
            rollsToRemoveLine = [colIndex for colIndex, char in enumerate(line) if char == 'X']

            for colIndex in rollsToRemoveLine:
                input[lineIndex][colIndex] = emptySpace
    else:
        break

print("Part 1: ", iters[0])
print("Part 2: ", sum(iters))