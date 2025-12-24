import openData
import math
import numpy as np
from collections import defaultdict

useTest = 1 == 0

input = [tuple(map(int, row.split(','))) for row in openData.getData(8, useTest)]
points = np.array(input)
N = len(input)

# Compute all pairwise distances efficiently
indexI, indexJ = np.triu_indices(N, k=1)
diffs = points[indexI] - points[indexJ]
dists = np.sqrt(np.sum(diffs**2, axis=1))
edges = sorted(zip(dists, indexI, indexJ))

connections = 10 if useTest else 1000

parent = list(range(N))

def findSet(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]  # Path compression
        i = parent[i]
    return i

def mergeSet(i, j):
    parent[findSet(i)] = findSet(j)

numConns = 0
lastMerge = None

for conn, (d, i, j) in enumerate(edges):
    if conn == connections:
        circuits = defaultdict(int)
        for node in range(N):
            circuits[findSet(node)] += 1
        conns = sorted(circuits.values(), reverse=True)
        Part1 = math.prod(conns[:3])
        print("Part 1:", Part1)
    root_i = findSet(i)
    root_j = findSet(j)
    if root_i != root_j:
        numConns += 1
        mergeSet(i, j)
        if numConns == N - 1:
            lastMerge = (i, j)

if lastMerge:
    i, lastMergej = lastMerge
    Part2 = input[i][0] * input[j][0]
    print("Part 2:", Part2)

