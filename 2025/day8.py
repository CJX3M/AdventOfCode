import openData
import math
from collections import defaultdict

useTest = 1 == 0

input = [tuple(map(int, row.split(','))) for row in openData.getData(8, useTest)]

dist = []

for i, (x1, y1, z1) in enumerate(input):
    for j, (x2, y2, z2) in enumerate(input):
        if i < j:
            d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
            dist.append((d, i, j))

connections = 10 if useTest else 1000

parent = {key: key for key in range(len(input))}

def findSet(i):
    return i if parent[i] == i else findSet(parent[i])

def mergeSet(i, j):
    parent[findSet(i)] = findSet(j)

numConns = 0

for conn, (d, i, j) in enumerate(sorted(dist)):
    if conn == connections:
        circuits = defaultdict(int)
        for node in parent:
            circuits[findSet(node)] += 1
        conns = sorted(circuits.values(), reverse=True)
        Part1 = math.prod(conns[:3])
        print("Part 1:", Part1)

    root_i = findSet(i)
    root_j = findSet(j)
    if root_i != root_j:
        numConns += 1
        mergeSet(i, j)
        if numConns == len(input) - 1:
            last_merge = (i, j)

i, j = last_merge
Part2 = input[i][0] * input[j][0]
print("Part 2:", Part2)

