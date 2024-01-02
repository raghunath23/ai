from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v) 
    def DLS(self, src, target, maxDepth):
        if src == target:
            return True
        if maxDepth <= 0:
            return False
        for i in self.graph[src]:
            if self.DLS(i, target, maxDepth-1):
                return True
        return False
N = int(input("Enter number of vertices: "))
g = Graph(N)
E = int(input("Enter number of edges: "))
for i in range(E):
    print("Enter parent and child node of edge", (i+1))
    g.addEdge(int(input()), int(input()))
target = int(input("Enter target node: "))
maxDepth = int(input("Enter maxDepth: "))
src = int(input("Enter source node: "))
if g.DLS(src, target, maxDepth):
    print("Target is reachable from source within max depth")
else:
    print("Target is NOT reachable from source within max depth")