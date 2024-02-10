from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
def DFS(graph, vertex):
    visited = set()
    stack = [vertex]
    while stack:
        vertex = stack.pop(0)
        
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
 
            for neighbour in graph[vertex]:
                stack.append(neighbour)
    

if __name__ == "__main__":
    g = graph()
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(2, 1)
    g.addEdge(3, 3)
 
    print("Following is Depth First Traversal (starting from vertex 0)")
     
    DFS(g.graph, 0)