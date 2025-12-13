import openData
import numpy as np

useTest = True

input = [np.array(list(map(int, row.split(',')))) for row in openData.getData(8, useTest)]

box = dict()

graph = []

circuits = []

for i in input:
    key = tuple(int(x) for x in i)
    box[key] = []
    for j in input:
        if np.array_equal(i, j):
            continue
        nodeKey = tuple(int(x) for x in j)
        d = np.linalg.norm(i - j)
        box[key].append((nodeKey, d))
    box[key] = sorted(box[key], key=lambda x: x[1])
    graph.append({
        "node": key,
        "closestNode": box[key][0][0] if box[key] else None,
        "distance": round(box[key][0][1]) if box[key] else float('inf')
    })

for node in sorted(graph, key=lambda x: x["distance"]):
    if node["closestNode"] is None:
        circuits.append([node])
    else:
        if circuits == []:
            closestNode = next(n for n in graph if n["node"] == node["closestNode"])
            circuits = [[node, closestNode]]
            continue
        # check if current node its part of a circuit
        found = False
        circuit = []
        for c in circuits:
            if node in c:
                circuit = c
                closestNode = graph[node["closestNode"]]
                if closestNode not in circuit:
                    circuit.append(closestNode)
                break
            circuit.append(node)
            closestNode = graph[node["closestNode"]]
            circuit.append(closestNode)
            # check if closestNode is part of a circuit
             
print("Graph:", graph)

Part1 = ''
print("Part 1:", Part1)
Part2 = ''
print("Part 2:", Part2)

