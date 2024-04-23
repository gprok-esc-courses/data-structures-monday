
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

    def relax(self, va, vb, w):
        if va.distance + w < vb.distance:
            vb.distance = va.distance + w
            vb.parent = va

    def dijkstra(self, start):
        Q = []
        self.init_bfs()
        self.vertices[start].distance = 0
        for key in self.vertices:
            Q.append(self.vertices[key])
        while len(Q) > 0:
            # sort Q in order to bring min distance fisrt
            Q.sort(key=lambda x : x.distance)
            u = Q.pop(0)
            for edge in u.edges:
                v = edge.destination
                w = edge.weight
                self.relax(u, v, w)

    def bellman_ford(self, start):
        self.init_bfs()
        self.vertices[start].distance = 0
        for i in range(len(self.vertices)):
            for key in self.vertices:
                u = self.vertices[key]
                for edge in u.edges:
                    v = edge.destination
                    w = edge.weight
                    self.relax(u, v, w)
        for key in self.vertices:
            u = self.vertices[key]
            for edge in u.edges:
                v = edge.destination
                w = edge.weight
                if v.distance > u.distance + w:
                    return False
        return True





    def display(self):
        for key in self.vertices:
            print(self.vertices[key])
            


if __name__ == "__main__":
    # TEST BFS
    # graph = Graph()
    # keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    # edges = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'D'], ['B', 'E'], 
    #          ['C', 'F'], ['D', 'G'], ['E', 'G'], ['E', 'H'], ['F', 'G'],
    #          ['F', 'I'], ['G', 'H'], ['H', 'I']]
    # for key in keys:
    #     graph.add_vertex(key)
    # for edge in edges:
    #     graph.add_edge(edge[0], edge[1])

    # graph.display()
    # graph.bfs('A')
    # graph.shortest_path('H')
    # graph.shortest_path_recursive('H')
    # print() 

    # TEST DIJKSTRA
    # graph = Graph()
    # keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    # edges = [['A', 'B', 3], ['A', 'C', 3], ['A', 'D', 4], ['B', 'D', 3], ['B', 'E', 6], 
    #          ['C', 'F', 1], ['D', 'G', 2], ['E', 'G', 1], ['E', 'H', 4], ['F', 'G', 2],
    #          ['F', 'I', 2], ['G', 'H', 3], ['H', 'I', 1]]
    # for key in keys:
    #     graph.add_vertex(key)
    # for edge in edges:
    #     graph.add_edge(edge[0], edge[1], edge[2])
    # graph.display()

    # graph.dijkstra('A')

    # for key in graph.vertices:
    #     vertex = graph.vertices[key]
    #     print(vertex.key, 'D:', vertex.distance)
    # graph.shortest_path('H')

    graph = Graph()
    graph.directed = True
    # keys = ['s', 't', 'y', 'x', 'z']
    # edges = [ ['s', 't', 10], ['s', 'y', 5], ['t', 'x', 1], ['t', 'y', 2], ['y', 't', 3], ['y', 'x', 9], 
    #           ['y', 'z', 2], ['z', 's', 7], ['x', 'z', 4], ['z', 'x', 6]
    #         ]
    keys = ['s', 't', 'x', 'y', 'z']
    edges = [
        ['s', 't', 6], ['s', 'y', 7], ['t', 'x', 5], ['x', 't', -2], ['t', 'y', 8], ['y', 'z', 9],
        ['z', 's', 2], ['t', 'z', -4], ['z', 'x', 7], ['y', 'x', -3]
    ]
    
    for key in keys:
        graph.add_vertex(key)
    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2])
    graph.display()

    result = graph.bellman_ford('s')

    for key in graph.vertices:
        vertex = graph.vertices[key]
        print(vertex.key, 'dist: ', vertex.distance, 'parent:', vertex.parent.key if vertex.parent is not None else 'None')
    if result:
        graph.shortest_path('x')
    else:
        print("No shortest path")