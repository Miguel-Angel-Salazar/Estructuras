class Graph:
  def __init__(self):
    self.adj_matrix: list[list[int]] = []
    self.nodes: list[int] = []
    self.size = 0
    self.nonweight_value = 0 #valor no representativo
    self.relation_value = 1

  def add_vertex(self, vertex_value):
    if(vertex_value in self.nodes):
      return

    #agrego a la lista de nodos
    self.nodes.append(vertex_value)
    self.size += 1

    #matriz de ady.
    for row in self.adj_matrix:
      row.append(self.nonweight_value)

    self.adj_matrix.append([self.nonweight_value] * self.size)

  def add_edge(self, vertex_1, vertex_2, directed = True, weight: int = None):
    #si no existen los vértices, los creo...
    if(vertex_1 not in self.nodes):
      self.add_vertex(vertex_1)

    if(vertex_2 not in self.nodes):
      self.add_vertex(vertex_2)

    pos_v1 = self.nodes.index(vertex_1)
    pos_v2 = self.nodes.index(vertex_2)

    relation_weight = self.relation_value if weight is None else weight

    if(not directed):
      self.adj_matrix[pos_v2][pos_v1] = relation_weight
    self.adj_matrix[pos_v1][pos_v2] = relation_weight


  def DFS(self, current, visited = []):
    if(current not in self.nodes):
      return

    current_pos = self.nodes.index(current)
    neighbors = self.adj_matrix[current_pos]
    for idx, adj in enumerate(neighbors):
      neighbor = self.nodes[idx]
      if(adj == 1 and neighbor not in visited):
        visited.append(neighbor)
        self.DFS(neighbor, visited)
    return visited

  def encontrar_palabra(self, palabra):
    for i, node in enumerate(self.nodes):
      if node == palabra[0]:
        stack = [(i, 1, {i})]
        while stack:
          current_idx, word_idx, visited = stack.pop()
          if word_idx == len(palabra):
            return True
          for idx, connected in enumerate(self.adj_matrix[current_idx]):
            if connected == self.relation_value and idx not in visited and self.nodes[idx] == palabra[word_idx]:
              stack.append((idx, word_idx + 1, visited | {idx}))
    return False
  
    

  def __repr__(self):
    repr_matrix = ""
    for row in self.adj_matrix:
      repr_matrix += str(row) + "\n"

    repr_matrix += f"\n{self.nodes}"

    return repr_matrix

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

g.DFS("O")