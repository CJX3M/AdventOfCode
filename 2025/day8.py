import openData
import numpy as np
import math
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

useTest = 1 == 0

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

adjacency = defaultdict(list)
for edge in graph:
    adjacency[edge["node"]].append(edge["closestNode"])
    adjacency[edge["closestNode"]].append(edge["node"])

def dfs(node, visited, component):
    visited.add(node)
    component.append(node)
    for neighbor in adjacency[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, component)

visited = set()
components = []

for node in list(adjacency):
    if node not in visited:
        component = []
        dfs(node, visited, component)
        components.append(component)


Part1 = math.prod(sorted([len(c) for c in components], reverse=True)[:3])
print("Part 1:", Part1)
Part2 = ''
print("Part 2:", Part2)