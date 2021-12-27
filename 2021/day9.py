from openData import getData

def findLowestHeights(matrix):
    rightBound = len(matrix[0])
    bottomBound = len(matrix)
    lowest = []
    for i in range(bottomBound):
        for j in range(rightBound):
            minor = []
            current = int(matrix[i][j])
            # check up
            if i-0 > 0:
                up = int(matrix[i-1][j])
                minor.append(current < up)
            # check down
            if i+1 < bottomBound:
                down = int(matrix[i+1][j])
                minor.append(current < down)
            # check left
            if j-0 > 0:
                left = int(matrix[i][j-1])
                minor.append(current < left)
            #check right
            if j+1 < rightBound:
                right = int(matrix[i][j+1])
                minor.append(current < right)
            if sum(minor) == len(minor):
                lowest.append((i, j))
    return lowest

# def findBasin(matrix):
#     basins = []
#     rightBound = len(matrix[0])
#     bottomBound = len(matrix)
#     sizes = []
#     for i in range(bottomBound):
#         for j in range(rightBound):
#             current = int(matrix[i][j])
#             if current == 9:
#                 continue
#             basins.append({ "x": i, "y": j })
#     #print(basins)
#     for basin in basins:
#         exist = True
#         size = [s for s in sizes if basin in s]
#         if not size:
#             exist = False
#             size = [basin]
#         else:
#             size = size[0]
#         for difBasin in [b for b in basins if b["x"] > basin["x"] or b["y"] > basin["y"]]:
#             basinInSize = [s for s in sizes if difBasin in s]
#             if not basinInSize:
#                 if basin["y"] == difBasin["y"] and abs(basin["x"]-difBasin["x"]) == 1:
#                     size.append(difBasin)
#                 elif basin["x"] == difBasin["x"] and abs(basin["y"]-difBasin["y"]) == 1:
#                     size.append(difBasin)
#             else:
#                 if not exist:
#                     if basin["y"] == difBasin["y"] and abs(basin["x"]-difBasin["x"]) == 1:
#                         exist = True
#                         size = basinInSize[0]
#                         size.append(basin)
#                     elif basin["x"] == difBasin["x"] and abs(basin["y"]-difBasin["y"]) == 1:
#                         exist = True
#                         size = basinInSize[0]
#                         size.append(basin)
#         if not exist:
#             sizes.append(size)

#     basinSizes = sorted([len(s) for s in sizes])
#     basinSizes.reverse()

#     print(basinSizes[0]*basinSizes[1]*basinSizes[2])

#     return 0            

def findBasin(lowest, matrix):
    sizes = []
    for low in lowest:
        sizes.append(checkPoint(low[0], low[1], matrix))
    return sizes
    
def checkPoint(x, y, matrix):
    size = 0
    rightBound = len(matrix[0])
    bottomBound = len(matrix)    
    if matrix[x][y] == '.' or matrix[x][y] == '9':
        return size
    matrix[x][y] = '.'
    size += 1
    if y+1 < rightBound:
        size += checkPoint(x, y+1, matrix)
    if y-1 >= 0:
        size += checkPoint(x, y-1, matrix)
    if x+1 < bottomBound:
        size += checkPoint(x+1, y, matrix)
    if x-1 >= 0:
        size += checkPoint(x-1, y, matrix)
    return size

data = getData("day9.txt")
matrix = [list(r) for r in data]


lowest = findLowestHeights(matrix)
riskLevel = sum([int(matrix[r[0]][r[1]])+1 for r in lowest])
print(riskLevel)
sizes = sorted(findBasin(lowest, matrix))[::-1]
print(sizes[0]*sizes[1]*sizes[2])

