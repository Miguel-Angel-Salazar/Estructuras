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

    def encontrar_palabra(self, palabra: str) -> bool:
        for node in self.adj_list:
            if node == palabra[0]:
                stack = [(node, 1, {node})]
                while stack:
                    current_node, word_idx, visited = stack.pop()
                    if word_idx == len(palabra):
                        return True
                    for neighbor in self.adj_list[current_node]:
                        if neighbor not in visited and neighbor == palabra[word_idx]:
                            stack.append((neighbor, word_idx + 1, visited | {neighbor}))
        return False

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
print(g.encontrar_palabra("HOLA"))
