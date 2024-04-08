
class Vertex:
    def __init__(self, key) -> None:
        self.key = key
        self.edges = []
        # variables for bfs
        self.parent = None
        self.color = 'white'
        self.distance = 0

    def __str__(self) -> str: 
        result = self.key + " -> "
        for edge in self.edges:
            result += "[" + edge.destination.key + ", " + str(edge.weight) + "] "
        return result


class Edge:
    def __init__(self, destination, weight=1) -> None:
        self.destination = destination
        self.weight = weight 


class Graph:
    def __init__(self) -> None:
        self.directed = False
        self.vertices = {}

    def add_vertex(self, key):
        if key in self.vertices:
            print("Error: vertex already in graph")
            return False
        else:
            v = Vertex(key)
            self.vertices[key] = v
            return True
        
    def add_edge(self, source, dest, weight=1):
        if source in self.vertices and dest in self.vertices:
            self.vertices[source].edges.append(Edge(self.vertices[dest], weight))
            if not self.directed:
                self.vertices[dest].edges.append(Edge(self.vertices[source], weight))
            return True
        else:
            print("Error: one of the vertices (or both) not found")
            return False
        
    def init_bfs(self):
        for key in self.vertices:
            vertex = self.vertices[key]
            vertex.parent = None
            vertex.color = 'white'
            vertex.distance = float('inf')

    def bfs(self, start):
        if start not in self.vertices:
            print("Error: vertex not found")
            return False
        else:
            self.init_bfs()
            queue = []
            start_vertex = self.vertices[start]
            start_vertex.color = 'gray'
            start_vertex.distance = 0
            start_vertex.parent = None 
            queue.append(start_vertex)
            while(len(queue) > 0):
                vertex = queue.pop(0)
                for edge in vertex.edges:
                    if edge.destination.color == 'white':
                        edge.destination.color = 'gray'
                        edge.destination.distance = vertex.distance + 1
                        edge.destination.parent = vertex 
                        queue.append(edge.destination)
                vertex.color = 'black'
            return True
        
    def shortest_path(self, dest):
        stack = []
        vertex = self.vertices[dest]
        while vertex.parent is not None:
            stack.append(vertex)
            vertex = vertex.parent
        stack.append(vertex)
        while len(stack) > 0:
            v = stack.pop()
            print(v.key, end=' ')
        print()

    def shortest_path_recursive(self, dest):
        vertex = self.vertices[dest]
        if vertex.parent is not None:
            self.shortest_path_recursive(vertex.parent.key)
        print(vertex.key, end=' ')

    def dfs(self, start):
        pass

    def display(self):
        for key in self.vertices:
            print(self.vertices[key])
        

if __name__ == "__main__":
    graph = Graph()
    keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    edges = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'D'], ['B', 'E'], 
             ['C', 'F'], ['D', 'G'], ['E', 'G'], ['E', 'H'], ['F', 'G'],
             ['F', 'I'], ['G', 'H'], ['H', 'I']]
    for key in keys:
        graph.add_vertex(key)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    graph.display()
    graph.bfs('A')
    graph.shortest_path('H')
    graph.shortest_path_recursive('H')
    print() 