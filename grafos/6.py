class Graph:
    def __init__(self):
        self.adj_list: dict[(int, list[int])] = {}
        self.size = 0
        self.nonweight_value = 0
        self.relation_value = 1

    def add_vertex(self, vertex_value):
        if vertex_value in self.adj_list:
            return
        self.adj_list[vertex_value] = []
        self.size += 1

    def add_edge(self, vertex_1, vertex_2, directed=True, weight: int = None):
        if vertex_1 not in self.adj_list:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.adj_list:
            self.add_vertex(vertex_2)

        if vertex_2 not in self.adj_list[vertex_1]:
            self.adj_list[vertex_1].append(vertex_2)

        if not directed and vertex_1 not in self.adj_list[vertex_2]:
            self.adj_list[vertex_2].append(vertex_1)

    def dfs_recursivo(self, inicio, visitado=None):
        if inicio not in self.adj_list:
            return []

        if visitado is None:
            visitado = []

        if inicio not in visitado:
            visitado.append(inicio)
            for vecino in self.adj_list[inicio]:
                if vecino not in visitado:
                    self.dfs_recursivo(vecino, visitado)

        return visitado

    def __repr__(self):
        return str(self.adj_list)
g = Graph()
g.add_edge('0', '1')
g.add_edge('0', '2')
g.add_edge('1', '3')
g.add_edge('1', '4')

print(g.dfs_recursivo('0'))