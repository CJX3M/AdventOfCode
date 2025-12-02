from openData import getData
from sys import maxsize

data = [list(map(int,i)) for i in getData("day15Test.txt")]

graph = {}
path = {}
explored = {}

for y, row in enumerate(data):
    for x, col in enumerate(row):
        graph[(y, x)] = col
        path[(x, y)] = maxsize
        explored[(x, y)] = False

graph[(0,0)] = 0
path[(0,0)] = graph[(0,0)]
boundaries = (len(data), len(data[0]))

currentNode = {"x":0,"y":0}

directions = [(-1, 0), (0, 1), (1,0), (0, -1)] #down, right, up, left

for node in range(len(graph)):
    neighboors = {}

    for diry, dirx in directions:
        if  -1 > currentNode["y"] + diry < boundaries[0] and -1 > currentNode["x"] + dirx < boundaries[1]:
            neighboors[(currentNode["y"] + diry, currentNode["x"] + dirx)] = graph[(currentNode["y"] + diry, currentNode["x"] + dirx)]

    minNeigh = {
        "neigh" : (0,0),
        "size": maxsize
    }




# while (9,9) not in path:
#     neighboors = {}
#     currentRisk = sum(path.values())
#     # lets get all the neightboors of the current node we are in
#     for diry, dirx in directions:
#         if currentNode["y"] + diry > -1 and currentNode["y"] + diry < boundaries[0] \
#         and currentNode["x"] + dirx > -1 and currentNode["x"] + dirx < boundaries[1]:
#             neighboors[(currentNode["y"] + diry, currentNode["x"] + dirx)] = currentRisk + graph[(currentNode["y"] + diry, currentNode["x"] + dirx)]
#     minNeigh = {
#         "neigh" : (0,0),
#         "size": maxsize
#     }
#     # lets find out, which its the node with the lowest risk and that we hadn't visited yet
#     for neigh in [n for n in neighboors if n not in path]:
#         if graph[neigh] < minNeigh["size"]:
#             minNeigh = {
#                 "neigh": neigh,
#                 "size": graph[neigh]
#             }
#             if minNeigh["neigh"] in explored and explored[minNeigh["neigh"]] < minNeigh["size"]:
#                 minNeigh["size"] = explored[minNeigh["neigh"]]
#     # lets add the node to the path, setting as visited
#     path[minNeigh["neigh"]] = graph[minNeigh["neigh"]]
#     neighboors.pop(minNeigh["neigh"])
#     explored.update(neighboors)
#     # lets move to the node we decided to visit
#     currentNode = {
#         "x": minNeigh["neigh"][1],
#         "y": minNeigh["neigh"][0]
#     }

reversedPath = path[:-1]

truePath = []

# class Graph:
#     def __init__(self, data) -> None:
#         self.paths = []
#         self.graph = data
#         self.exit = [len(data)-1, len(data[0])-1]
        
#     def movement(self, path, currentPos):
#         if currentPos == self.exit:
#             self.paths.append(path)
#             #return True
#         elif currentPos != [0,0]:
#             path.append(self.graph[currentPos[0]][currentPos[1]])

#         while currentPos[0] <= self.exit[0]-1:
#             if currentPos[1] < self.exit[1]:
#                 currentPos[1] += 1
#             elif currentPos[1] == self.exit[1]:                
#                 currentPos[0] += 1
#             self.movement(path, currentPos)

#         currentPos[1] -= 1
#         currentPos[0] = 0

#         #return False
        
#     def startSearch(self):
#         self.movement([], [0,0])
#         sums = [sum(p) for p in self.paths]

#         return min(sums)

# pages = 5
# width = len(data[0])
# height = len(data)

# myList = [[(value + x + y -1) % 9 + 1 for x in range(pages) for value in line]for y in range(pages) for line in data]

# [print(item) for item in myList]