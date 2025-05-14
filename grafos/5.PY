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

    def dfs(self, inicio, visitado=None):
        if inicio not in self.adj_list:
            return []

        if visitado is None:
            visitado = []

        if inicio not in visitado:
            visitado.append(inicio)
            for neighbor in self.adj_list[inicio]:
                if neighbor not in visitado:
                    self.dfs(neighbor, visitado)

        return visitado

    def bfs(self, inicio):
        if inicio not in self.adj_list:
            return []

        visitado = []
        cola = [inicio]
        while cola:
            nodo = cola.pop(0)  # Simula cola FIFO
            if nodo not in visitado:
                visitado.append(nodo)
                for vecino in self.adj_list[nodo]:
                    if vecino not in visitado and vecino not in cola:
                        cola.append(vecino)
        return visitado

    def __repr__(self):
        return str(self.adj_list)

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')

print(g.bfs("A"))