import openData
import numpy as np
import math
from collections import defaultdict

useTest = False

input = [np.array(list(map(int, row.split(',')))) for row in openData.getData(8, useTest)]

box = dict()

graph = []

circuits = defaultdict(list)

for i, ni in enumerate(input):
    key = tuple(int(x) for x in ni)
    box[key] = []
    for j, nj in enumerate(input):
        if np.array_equal(ni, nj):
            continue
        nodeKey = tuple(int(x) for x in nj)
        if nodeKey in box and any(b[0] == key for b in box[nodeKey]):
            continue
        d = np.linalg.norm(ni - nj)
        box[key].append((nodeKey, d))
    if any(box[key]):
        box[key] = sorted(box[key], key=lambda x: x[1])
        lowestDist = round(box[key][0][1])
        lowestNodes = [n for n in box[key] if round(n[1]) == lowestDist]
        for closestNode in lowestNodes:
            graph.append({
                "node": key,
                "closestNode": closestNode[0],
                "distance": lowestDist
            })

graph = sorted(graph, key=lambda x: x["distance"])

prop = "node"

parent = {key: key for key in box.keys()}

def findSet(i):
    if parent[i] != i:
        parent[i] = findSet(parent[i])
    return parent[i]

def mergeSet(i, j):
    parent[findSet(j)] = findSet(i)

connections = 10 if useTest else 1000

for node, closestNode, distance in [(n["node"], n["closestNode"], n["distance"]) for n in graph[:connections]]:
    mergeSet(node, closestNode)

for node in parent:
    root = findSet(node)
    circuits[root].append(node)

# def addToCircuit(node, circuit, connections):
#     if node[prop] in circuit or connections == 0:
#         return circuit, connections
#     connections -= 1
#     circuit.append(node[prop])
#     if (not any(n for n in graph if n[prop] == node["closestNode"])):
#         return circuit, connections
#     closestNode = next(n for n in graph if n[prop] == node["closestNode"])
#     graph.remove(closestNode)
#     return addToCircuit(closestNode, circuit, connections)

# while graph:
#     node = graph.pop()
#     circuit = next((c for c in circuits if node[prop] in c or node["closestNode"] in c), [])
#     found = True if circuit else False
#     circuit, connections = addToCircuit(node, circuit, connections)
#     if not found:
#         circuits.append(circuit)
#     if connections == 0:
#         break
# print("Circuits:", circuits)

# while graph:
#     connection = False

#     node = graph.pop()
#     closestNode = next((n for n in graph if n[prop] == node["closestNode"]), None)

#     circuit = next((c for c in circuits if node[prop] in c or node["closestNode"] in c), None)
#     if circuit is None:
#         circuit = []
#         circuit.append(node[prop])
#         if closestNode:
#             circuit.append(closestNode[prop])
#         connection = True
#     else:
#         circuits.remove(circuit)
#         if node[prop] not in circuit:
#             circuit.append(node[prop])
#             connection = True
#         if closestNode and closestNode[prop] not in circuit:
#             circuit.append(closestNode[prop])
#             connection = True

#     if connection:
#         connections -= 1

#     circuits.append(circuit)

#     if connections == 0:
#         break

conns = [len(c) for c in circuits.values()]
conns = sorted(conns)[::-1]
Part1 = math.prod(conns[:3])
print("Part 1:", Part1)
Part2 = ''
print("Part 2:", Part2)

