class Graph:
    def _init_(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)

    def DFS(self, start_vertex):
        visited = [False for _ in range(self.num_vertices)]
        
        self.DFS_util(start_vertex, visited)

    def DFS_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex)
        
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self.DFS_util(neighbor, visited)

# create a sample graph
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# run DFS starting from vertex 2
g.DFS(2)
