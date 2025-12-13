import openData
import numpy as np

useTest = False

input = [np.array(list(map(int, row.split(',')))) for row in openData.getData(8, useTest)]

graph = dict()

for i in input:
    key = tuple(i)
    graph[key] = []
    for j in input:
        if np.array_equal(i, j):
            continue
        nodeKey = tuple(j)
        if nodeKey in graph[key]:
            continue
        d = np.linalg.norm(i - j)
        graph[key].append((nodeKey, d))




Part1 = ''
print("Part 1:", Part1)
Part2 = ''
print("Part 2:", Part2)

