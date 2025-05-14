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
    
    def ciclos(self, inicio, visitado=None,):
            if inicio not in self.adj_list:
                return False

            if visitado is None:
                visitado = []

            visitado.append(inicio)

            for vecino in self.adj_list[inicio]:
                if vecino not in visitado:
                    if self.ciclos(vecino, visitado):
                        return True
                elif vecino == visitado[0]:
                    return True       
            return False

    def contar_ciclos(self):
        pass


    def __repr__(self):
        return str(self.adj_list)
    

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')
g.add_edge("C", "E")
g.add_edge("F", "C")

print(g)
print(g.ciclos("C"))
print(g.contar_ciclos)