import numpy as np
import openData

useTest = 1 == 1

input = [tuple(map(int, row.split(','))) for row in openData.getData(9, useTest)]
points = np.array(input)
N = len(input)

areas = []
for i, (x1, y1) in enumerate(points):
     for j, (x2, y2) in enumerate(points):
          if i == j:
               continue
          area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
          areas.append((area, (i, j)))

areas.sort()

Part1 = areas[-1][0]
print("Part 1:", Part1)

# sort points by x, then y
points = points[np.lexsort((points[:, 1], points[:, 0]))]

pointsOnEdge = [points[0]]
    
while True:
    x, y = pointsOnEdge[-1]
    # searchClockwise for the next corner
    # search for a point above the current
    p = [p for p in points if (x == p[0] and y < p[1])]

    if p:
        if not any(np.array_equal(pe, p[0]) for pe in pointsOnEdge):
            pointsOnEdge.append(p[0])
            continue

    # search for a point to the right
    p = [p for p in points if (x < p[0] and y == p[1])]

    if p:
        if not any(np.array_equal(pe, p[0]) for pe in pointsOnEdge):
            pointsOnEdge.append(p[0])
            continue

    # search for a point below the current
    p = [p for p in points if (x == p[0] and y > p[1])]

    if p:
        if not any(np.array_equal(pe, p[0]) for pe in pointsOnEdge):
            pointsOnEdge.append(p[0])
            continue

    # search for a point to the left the current
    p = [p for p in points if (x > p[0] and y == p[1])]

    if p:
        if not any(np.array_equal(pe, p[0]) for pe in pointsOnEdge):
            pointsOnEdge.append(p[0])
            continue

    break


print(pointsOnEdge)

for point in pointsOnEdge:
    x, y = point

    


        
Part2 = ''
print("Part 2:", Part2)
