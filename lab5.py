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
            if self.DLS(i, target, maxDepth - 1):
                return True
        return False

# Static input for the graph
graph_edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (4, 7)]

N = 8  # Number of vertices
g = Graph(N)

for edge in graph_edges:
    g.addEdge(edge[0], edge[1])

target = 7
maxDepth = 3
src = 0

if g.DLS(src, target, maxDepth):
    print("Target is reachable from source within max depth")
else:
    print("Target is NOT reachable from source within max depth")
"""
Sample output
Target is reachable from source within max depth
"""
