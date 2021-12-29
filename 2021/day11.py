from openData import getData
import numpy as np

def increaseEnergy(x, y, matrix):
    bottomBound = len(grid)
    rightBound = len(grid[0])
    if matrix[x][y] >= 10:
        matrix[x][y] = 0
        if x-1 >= 0: # UP
            if matrix[x-1][y] < 10 and matrix[x-1][y] != 0:
                matrix[x-1][y] += 1
        if y+1 < rightBound and x-1 >= 0: # UP-Right
            if matrix[x-1][y+1] < 10  and matrix[x-1][y+1] != 0:
                matrix[x-1][y+1] += 1
        if y+1 < rightBound: # RIGHT
            if matrix[x][y+1] < 10  and matrix[x][y+1] != 0:
                matrix[x][y+1] += 1
        if y+1 < rightBound and x+1 < bottomBound: # DOWN-Right
            if matrix[x+1][y+1] < 10 and matrix[x+1][y+1] != 0:
                matrix[x+1][y+1] += 1
        if x+1 < bottomBound: # DOWN
            if matrix[x+1][y] < 10 and matrix[x+1][y] != 0:
                matrix[x+1][y] += 1
        if y-1 >= 0 and x+1 < bottomBound: # DOWN-LEFT
            if matrix[x+1][y-1] < 10 and matrix[x+1][y-1] != 0:
                matrix[x+1][y-1] += 1
        if y-1 >= 0: # LEFT
            if matrix[x][y-1] < 10 and matrix[x][y-1] != 0:
                matrix[x][y-1] += 1
        if x-1 >= 0 and y-1 >= 0: # UP-LEFT
            if matrix[x-1][y-1] < 10 and matrix[x-1][y-1] != 0:
                matrix[x-1][y-1] += 1
    return matrix

data = getData("day11.txt")
grid = np.array([list(map(int, r)) for r in data])
totalOctopuses = len(grid) * len(grid[0])
flashes = 0
stepFlashes = 0
step = 0
while True:
    grid += 1
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            grid = increaseEnergy(row, column, grid)
    tens = [(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 10]
    while tens:
        for ten in tens:
            grid = increaseEnergy(ten[0], ten[1], grid)
        tens = [(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 10]
    
    stepFlashes = len([(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 0])
    step += 1
    if step < 100:
        flashes += stepFlashes
    if stepFlashes == totalOctopuses:
        break


print('Flashes:', flashes)
print('All flashes at:', step)