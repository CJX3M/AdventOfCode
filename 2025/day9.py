from functools import cache
import openData

useTest = 1 == 0

points = [tuple(map(int, row.split(','))) for row in openData.getData(9, useTest)]
N = len(points)
Part1 = 0
Part2 = 0

@cache
def pointInPolygon(x, y):
    inside = False

    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        if (x == x1 == x2 
            and min(y1, y2) <= y <= max(y1, y2)
            or ( y == y1 == y2
            and min(x1, x2) <= x <= max(x1, x2))):
            return True  # on edge
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside

def edgeIntersectsSquare(x1, y1, x2, y2, sx1, sy1, sx2, sy2):

    if y1 == y2:  # horizontal edge
        if sy1 < y1 < sy2:
            if max(x1, x2) > sx1 and min(x1, x2) < sx2:
                return True
    elif x1 == x2:  # vertical edge
        if sx1 < x1 < sx2:
            if max(y1, y2) > sy1 and min(y1, y2) < sy2:
                return True

def validSquare(x1, x2, y1, y2):

    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    for x, y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
        # check if the corner is part of the points 
        if not pointInPolygon(x, y):
            return False
    for (ex1, ey1), (ex2, ey2) in zip(points, points[1:] + points[:1]):
        # check if any edge intersects with the square
        if edgeIntersectsSquare(ex1, ey1, ex2, ey2, x1, y1, x2, y2):
            return False
        
    return True

for i, (x1, y1) in enumerate(points):
     for j, (x2, y2) in enumerate(points):
          if i < j:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            Part1 = max(Part1, area)
            if area > Part2 and validSquare(x1, x2, y1, y2):
                Part2 = area

print("Part 1:", Part1)

           
# # sort points by x, then y
# points = points[np.lexsort((points[:, 1], points[:, 0]))]

# pointsOnEdge = [points[0]]
    
# while True:
#     x, y = pointsOnEdge[-1]
#     # searchClockwise for the next corner
#     # search for a point above the current
#     p = [p for p in points if (x == p[0] and y < p[1])]

#     if p:
#         if not any(np.array_equal(pe, p[0]) for pe in pointsOnEdge):
#             pointsOnEdge.append(p[0])

#     # search for a point to the right
#     p = [p for p in points if (x < p[0] and y == p[1])]

#     if p:
#         if not any(np.array_equal(pe, p[0]) for pe in pointsOnEdge):
#             pointsOnEdge.append(p[0])

#     # search for a point below the current
#     p = [p for p in points if (x == p[0] and y > p[1])]

#     if p:
#         if not any(np.array_equal(pe, p[0]) for pe in pointsOnEdge):
#             pointsOnEdge.append(p[0])

#     # search for a point to the left the current
#     p = [p for p in points if (x > p[0] and y == p[1])]

#     if p:
#         if not any(np.array_equal(pe, p[0]) for pe in pointsOnEdge):
#             pointsOnEdge.append(p[0])

#     if np.array_equal(pointsOnEdge[0], pointsOnEdge[-1]):
#         break

# areas = []

# def checkForSquare(p1, p2):
#     opositeCorner = (p2[0][0], p1[0][1])
    
#     path = Path(pointsOnEdge)    

#     if path.contains_point(opositeCorner):
#         area = calculateArea(p2[0], p1[0])
#         areas.append(area)

# for point in pointsOnEdge:
#     x, y = point
        
#     # search for a point above the current
#     upper = [p for p in points if (x == p[0] and y > p[1])]

#     # search for a point to the right
#     left = [p for p in points if (x > p[0] and y == p[1])]

#     # search for a point below the current
#     right = [p for p in points if (x < p[0] and y == p[1])]

#     # search for a point to the left the current
#     down = [p for p in points if (x == p[0] and y < p[1])]

#     if upper and left:
#         checkForSquare(upper, left)

#     if down and left:
#         checkForSquare(down, left)

#     if down and right:
#         checkForSquare(down, right)

#     if upper and right:
#         checkForSquare(upper, right)

print("Part 2:", Part2)

# 158357832 is not the answer
# 420179376
# 4623743592 is too high