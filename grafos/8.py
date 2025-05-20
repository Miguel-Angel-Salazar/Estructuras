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

    def entradas(self, inicio):
        if inicio not in self.adj_list:
            return 0
        contador = 0
        for i, vecinos in self.adj_list.items():
            if inicio in vecinos:
                contador += 1
        return contador

    def salidas(self, inicio):
        if inicio not in self.adj_list:
            return 0
        return len(self.adj_list[inicio])
    
    def eliminar(self, valor):
        if valor in self.adj_list:
            del self.adj_list[valor]

            for vecinos in self.adj_list.values():
                if valor in vecinos:
                    vecinos.remove(valor)
        else:
            print("no hay valor para eliminar")

    def desconectados(self):
        contador = 0
        for nodo in self.adj_list:
            if len(self.adj_list[nodo]) == 0 and self.entradas(nodo) == 0:
                contador += 1
        return contador

    def desconectados_1(self):
            d = []
            for nodo in self.adj_list:
                if len(self.adj_list[nodo]) == 0 and self.entradas(nodo) == 0:
                    d.append(nodo)
            return d

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


# Ejemplo de uso con letras para formar palabras
g = Graph()
g.add_edge("H", "A")
g.add_edge("H", "O")
g.add_edge("O", "X")
g.add_edge("O", "A")
g.add_edge("O", "L")
g.add_edge("O", "O")
g.add_edge("L", "A")
g.add_edge("L", "Z")
g.add_edge("L", "O")


print(g)
print(g.bfs("H"))
print(g.dfs("H"))
print(g.entradas("A"))
print(g.salidas("L"))
print(g.eliminar("L"))
print(g)
print(g.desconectados_1())
print(g.desconectados())
