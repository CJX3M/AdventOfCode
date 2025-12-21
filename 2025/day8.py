import openData
import numpy as np
import math
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

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

# Build the graph from your connections
G = nx.Graph()
for node, closestNode in [(n["node"], n["closestNode"]) for n in graph[:connections]]:
    G.add_edge(node, closestNode)

# Optionally, color nodes by their root
colors = []
roots = {node: findSet(node) for node in G.nodes}
unique_roots = list(set(roots.values()))
color_map = {root: i for i, root in enumerate(unique_roots)}
for node in G.nodes:
    colors.append(color_map[roots[node]])

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # or use nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=False, node_color=colors, cmap=plt.cm.Set3, node_size=50, edge_color='gray')
plt.title("Union-Find Tree Visualization")
plt.show()

