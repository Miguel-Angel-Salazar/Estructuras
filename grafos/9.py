class Graph:
    def __init__(self):
        self.adj_list: dict[str, list[tuple[str, int]]] = {}
        self.size = 0
        self.nonweight_value = 0  # Valor por defecto si no se pasa peso
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

        if not any(neighbor == vertex_2 for neighbor, _ in self.adj_list[vertex_1]):
            self.adj_list[vertex_1].append((vertex_2, weight if weight is not None else self.nonweight_value))

        if not directed and not any(neighbor == vertex_1 for neighbor, _ in self.adj_list[vertex_2]):
            self.adj_list[vertex_2].append((vertex_1, weight if weight is not None else self.nonweight_value))

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


    def rutas(self, inicio, visitados=None):
        if inicio not in self.adj_list:
            return []

        if visitados is None:
            visitados = []

        visitados.append(inicio)

        if not self.adj_list[inicio]:
            return [visitados.copy()]

        rutas_encontradas = []
        for vecino, _ in self.adj_list[inicio]:
            if vecino not in visitados:
                nuevas_rutas = self.rutas(vecino, visitados)
                for ruta in nuevas_rutas:
                    rutas_encontradas.append(ruta)

        visitados.pop()

        return rutas_encontradas

    
    def pesos(self, inicio, visitados=None, peso_actual=0):

        visitados = visitados + [inicio] if visitados else [inicio]

        if not self.adj_list[inicio]:
            return [peso_actual]
        
        pesos_encontrados = []
        for vecino, peso in self.adj_list[inicio]:
            if vecino not in visitados:
                nuevos_pesos = self.pesos(vecino, visitados, peso_actual + peso)
                pesos_encontrados.append(nuevos_pesos)
        return pesos_encontrados

        


    def __repr__(self):
        return str(self.adj_list)
    
g = Graph()
g.add_edge("A", "B", weight= 2)
g.add_edge("A", "E", weight= 5)
g.add_edge("A", "C", weight= 30)
g.add_edge("B", "C", weight= 1)
g.add_edge("B", "D", weight= 7)
g.add_edge("C", "D", weight= 8)
g.add_edge("C", "X", weight= 4)
g.add_edge("D", "C", weight= 1)
g.add_edge("E", "D", weight= 6)

print(g.rutas("A"))
print(g.pesos("A"))
