import openData
import numpy as np

useTest = True

input = [np.array(list(map(int, row.split(',')))) for row in openData.getData(8, useTest)]

box = dict()

graph = []

circuits = []

boxes = []

for i in input:
    key = tuple(int(x) for x in i)
    box[key] = []
    for j in input:
        if np.array_equal(i, j):
            continue
        nodeKey = tuple(int(x) for x in j)
        # if j in box:
        #     continue
        d = np.linalg.norm(i - j)
        box[key].append((nodeKey, d))
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

graph.reverse()
connections = 10 if useTest else 1000
prop = "node"

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

while graph:
    connection = False

    node = graph.pop()
    closestNode = next((n for n in graph if n[prop] == node["closestNode"]), None)

    circuit = next((c for c in circuits if node[prop] in c or node["closestNode"] in c), None)
    if circuit is None:
        circuit = []
        circuit.append(node[prop])
        if closestNode:
            circuit.append(closestNode[prop])
        connection = True
    else:
        circuits.remove(circuit)
        if node[prop] not in circuit:
            circuit.append(node[prop])
            connection = True
        if closestNode and closestNode[prop] not in circuit:
            circuit.append(closestNode[prop])
            connection = True

    if connection:
        connections -= 1

    circuits.append(circuit)

    if connections == 0:
        break
print("Circuits:", circuits)

Part1 = ''
print("Part 1:", Part1)
Part2 = ''
print("Part 2:", Part2)

