class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

print("Graph (Adjacency List):")
g.print_graph()