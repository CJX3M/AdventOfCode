from openData import getData
from copy import deepcopy

def traverseTrail(currentTrail, grid, directions, score, limits, part2 = False):

    for direction in directions:
        moveTo = [a + b for a,b in zip(currentTrail, direction)]
        if inbound(moveTo, limits):
            currentValue = {i for i in grid if currentTrail in grid[i]}
            nextValue = {pos for pos in grid if moveTo in grid[pos]}
            if nextValue:
                currentValue = currentValue.pop()
                nextValue = nextValue.pop()
                if nextValue == currentValue + 1:
                    if currentValue + 1 == 9:
                        score += 1
                        if not part2:
                            grid[nextValue].remove(moveTo)
                    else:
                        score = traverseTrail(moveTo, grid, directions, score, limits, part2)
    return score

def inbound(position, limits):
    return 0 <= position[0] <= limits[0] and 0 <= position[1] <= limits[1]

if __name__ == "__main__":

    #input = [list(row) for row in getData("day10TestInput.txt")]

    input = [list(row) for row in getData("day10Input.txt")]

    grid = dict()

    for rowI, row in enumerate(input):
        for colI, c in enumerate(row):
            if not c.isdigit():
                continue
            c = int(c)
            if c not in grid:
                grid[c] = [[rowI, colI]]
            else:
                grid[c].append([rowI, colI])
                
    maxCol = len(input[0])
    maxRow = len(input)

    directions = [[ 1,  0], #down,
                  [ 0, -1], #left
                  [-1, 0], #up
                  [ 0, 1] #right
                  ]
    
    scores = []

    part2 = True

    for i in [r for r in grid.keys() if r == 0]:
        for coord in grid[i]:
            scores.append(traverseTrail(coord, deepcopy(grid), directions, 0, [maxCol, maxRow], part2))
    print(f"\r\n{scores}")
    print(f"\rResult: {sum(scores)}")