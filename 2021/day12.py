from collections import defaultdict, Counter
from openData import getData

class Graph:

    def __init__(self, vertices) -> None:
        self.vertices = vertices

        self.graph = defaultdict(list)
        self.visited = {}
        self.paths = 0
        self.canVisitTwice = False

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if u != "start" and u != "end":
            self.graph[v].append(u)
        if u not in self.visited.keys():
            self.visited[u] = 0
        if v not in self.visited.keys():
            self.visited[v] = 0

    def printAllPathsUtil(self, u, d, visited, path):

        if u.islower():
            visited[u] += 1            
        path.append(u)

        if u == d:
            self.paths += 1
            #print(f'{self.paths}', end="\r")
            print(path)            
        else:
            smallCaves = len([item for item, count in Counter([i for i in path if i.islower()]).items() if count > 1])
            for i in self.graph[u]:
                if (visited[i] == 0) or (visited[i] < 2 
                    and self.canVisitTwice 
                    and (smallCaves == 0 or i.isupper())):
                    self.printAllPathsUtil(i, d, visited, path)

        path.pop()

        visited[u] = 0 if not self.canVisitTwice else visited[u] - 1

    def printAllPaths(self, s, d, _canVisitTwice = False):

        path=[]

        self.canVisitTwice = _canVisitTwice

        self.printAllPathsUtil(s, d, self.visited, path)

        print(self.paths)


data = getData("day12.txt")

graph = Graph(len(data))
[graph.addEdge(v.split("-")[0], v.split("-")[1]) for v in data]
graph.printAllPaths("start", "end")
print("")
graph = Graph(len(data))
[graph.addEdge(v.split("-")[0], v.split("-")[1]) for v in data]
graph.printAllPaths("start", "end", True)


        