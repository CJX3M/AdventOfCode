import openData
import numpy as np
import math
from collections import defaultdict

useTest = False

input = [np.array(list(map(int, row.split(',')))) for row in openData.getData(8, useTest)]

box = dict()

graph = []

for i, ni in enumerate(input):
    key = tuple(int(x) for x in ni)
    box[key] = []
    for j in range(i + 1, len(input)):
        nj = input[j]
        if np.array_equal(ni, nj):
            continue
        nodeKey = tuple(int(x) for x in nj)
        if nodeKey in box and any(b[0] == key for b in box[nodeKey]):
            continue
        d = np.linalg.norm(ni - nj)
        box[key].append((nodeKey, d))
    if any(box[key]):        
        lowestDist = round(min(d for _, d in box[key]))
        lowestNodes = [n for n in box[key] if round(n[1]) == lowestDist]
        for closestNode in lowestNodes:
            graph.append({
                "node": ",".join(str(x).strip() for x in key),
                "closestNode": ",".join(str(x).strip() for x in closestNode[0]),
                "distance": lowestDist
            })

graph = sorted(graph, key=lambda x: x["distance"])

connections = 10 if useTest else 1000

all_nodes = set()
for n in graph[:connections]:
    all_nodes.add(n["node"])
    all_nodes.add(n["closestNode"])

parent = {key: key for key in all_nodes}

def findSet(i):
    return i if parent[i] == i else findSet(parent[i])

def mergeSet(i, j):
    parent[findSet(i)] = findSet(j)

for node, closestNode in [(n["node"], n["closestNode"]) for n in graph[:connections]]:
    mergeSet(node, closestNode)

circuits = defaultdict(int)
for node in parent:
    root = findSet(node)
    circuits[root] += 1

conns = sorted(circuits.values(), reverse=True)
Part1 = math.prod(conns[:3])
print("Part 1:", Part1)
Part2 = ''
print("Part 2:", Part2)

