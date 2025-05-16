class Graph:
    def __init__(self):
        self.adj_list: dict[str, list[str]] = {}
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

    def contar_componentes_conexas(self) -> int:
        visitados = []
        componentes = 0

        for nodo in self.adj_list:
            if nodo not in visitados:
                resultado = self.dfs(nodo)
                visitados.extend(resultado) # si se hace con el append lo que se logra es que se comparen listas de listas, no el nodo invidivual, por eso el extend
                componentes += 1

        return componentes

    def __repr__(self):
        return str(self.adj_list)
    
grafo = Graph()
grafo.add_edge('1', '2')
grafo.add_vertex('3')
grafo.add_edge('4', '5')

print(grafo.contar_componentes_conexas())