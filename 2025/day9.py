from functools import cache
import openData

useTest = 1 == 0

points = [tuple(map(int, row.split(','))) for row in openData.getData(9, useTest)]
N = len(points)
Part1 = 0
Part2 = 0

@cache
def pointInPolygon(x, y):
    vertices = len(points)

    inside = False

    p1 = points[0]

    for i in range(1, vertices + 1):
        p2 = points[i % vertices]

        if y > min(p1[1], p2[1]):
            if y <= max(p1[1], p2[1]):
                if x <= max(p1[0], p2[0]):
                    xinters = int((y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0])
                    if p1[0] == p2[0] or x <= xinters:
                        inside = not inside
        p1 = p2

    return inside

def calculateArea(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return int((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

def validSquare(x1, x2, y1, y2):

    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    for x, y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
        # check if the corner is part of the points 
        if (x, y) not in points and not pointInPolygon(x, y):
            return False
        
    return True

for i, (x1, y1) in enumerate(points):
     for j, (x2, y2) in enumerate(points):
          if i == j:
               continue
          area = calculateArea((x1, y1), (x2, y2))
          Part1 = max(Part1, area)
          if area > Part2 and validSquare(int(x1), int(x2), int(y1), int(y2)):
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
# 4623743592 is too high