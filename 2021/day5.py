from openData import getData

def printField(field):
    for row in field:
        print(row)

def markField(x1, y1, x2, y2, field):    
    while x1 != x2 or y1 != y2:
        field[y1][x1] += 1
        x1 += 0 if x1 == x2 else -1 if x1 > x2 else 1
        y1 += 0 if y1 == y2 else -1 if y1 > y2 else 1
    field[y2][x2] += 1

def part1(x1, y1, x2, y2, field):
    if x1 == x2 or y1 == y2:
        markField(x1, y1, x2, y2, field)

def part2(x1, y1, x2, y2, field):
    markField(x1, y1, x2, y2, field)

data = getData('day5.txt')

maxSize = max([int(i) for i in sum([i.replace("->", ",").split(",") for i in data], [])]) + 1

data = [i.split('->') for i in data]

field = [[0 for i in range(maxSize)] for r in range(maxSize)]

overlapAmmount = 0

for coord in data:
    x1, y1 = [int(i) for i in coord[0].split(',')]
    x2, y2 = [int(i) for i in coord[1].split(',')]
    #part1(x1, y1, x2, y2, field)
    part2(x1, y1, x2, y2, field)

#printField(field)

for i in range(maxSize):
    for j in range(maxSize):
        if field[i][j] >= 2:
            overlapAmmount += 1 
            
print(overlapAmmount)
