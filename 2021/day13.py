from openData import getData

data = getData("day13.txt")

dots = [list(map(int, d.split(','))) for d in data if ',' in d]
foldInstructions = [(d.split("=")[0][-1], int(d.split("=")[1])) for d in data if '=' in d]

maxX = max([int(x[0]) for x in dots])+1
maxY = max([int(y[1]) for y in dots])+1

grid = [['.']*maxX for i in range(maxY)]

for dot in dots:
    grid[dot[1]][dot[0]] = "#"

for fold in foldInstructions:
    print(f"Fold {fold[0]}={fold[1]}")
    coord = fold[1]
    if fold[0] == "x":
        dotsToMove = [d for d in dots if d[0] > coord]
        for dot in dotsToMove:
            coordDif = dot[0] - coord
            grid[dot[1]][coord-coordDif] = "#"
            if not [coord-coordDif, dot[1]] in dots:
                dots.append([coord-coordDif, dot[1]])
            dots.remove(dot)
        for y in range(len(grid)):
            cols = coord
            while cols < len(grid[y]):
                grid[y].pop()            
    elif fold[0] == "y":
        dotsToMove = [d for d in dots if d[1] > coord]
        for dot in dotsToMove:
            coordDif = dot[1] - coord
            grid[coord-coordDif][dot[0]] = "#"
            if not [dot[0], coord-coordDif] in dots:
                dots.append([dot[0], coord-coordDif])
            dots.remove(dot)
        rows = coord
        maxY = len(grid)
        while rows < maxY:
            grid.pop()
            rows += 1

    print("Dots", len(dots))

[print("".join(r)) for r in grid]