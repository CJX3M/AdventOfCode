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
    boxes.append((key, box[key]))
    graph.append({
        "node": key,
        "closestNode": box[key][0][0] if box[key] else None,
        "distance": round(box[key][0][1]) if box[key] else float('inf')
    })

graph = sorted(graph, key=lambda x: x["distance"])

#lets clean the graph. if n1 closest node is n2, and n2 closest node is n1, and they have the same distance, just add n1 
cleanedGraph = []
while graph:
    node = graph.pop(0)
    if any(n for n in cleanedGraph if n["node"] == node["node"]):
        continue
    closestNode = next((n for n in graph if n["node"] == node["closestNode"]), None)
    if closestNode and closestNode["closestNode"] == node["node"] and closestNode["distance"] == node["distance"]:
        cleanedGraph.append(node)
        graph.remove(closestNode)
    else:
        cleanedGraph.append(node)

graph = cleanedGraph

def addToCircuit(node, circuit):
    if node in circuit:
        return circuit
    
    circuit.append(node)
    if (not any(n for n in graph if n["node"] == node["closestNode"])):
        return circuit
    closestNode = next(n for n in graph if n["node"] == node["closestNode"])
    graph.remove(closestNode)
    return addToCircuit(closestNode, circuit)

while graph:
    node = graph.pop()
    circuit = addToCircuit(node, [])
    circuits.append(circuit)
print("Circuits:", circuits)

Part1 = ''
print("Part 1:", Part1)
Part2 = ''
print("Part 2:", Part2)

