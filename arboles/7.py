class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None

    def __repr__(self):
        return self._repr()

    def _repr(self, level=0, prefix="Root: "):
        result = " " * (level * 4) + prefix + str(self.value) + "\n"
        if self.leftchild:
            result += self.leftchild._repr(level + 1, "L--- ")
        if self.rightchild:
            result += self.rightchild._repr(level + 1, "R--- ")
        return result


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value, current_node=None):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            if current_node is None:
                current_node = self.root 
            if value == current_node.value:
                return None
            if value < current_node.value:
                if current_node.leftchild is None:
                    current_node.leftchild = BinaryNode(value)
                else:
                    self.insert(value, current_node.leftchild)
            else:
                if current_node.rightchild is None:
                    current_node.rightchild = BinaryNode(value)
                else:
                    self.insert(value, current_node.rightchild)

    def contar_hojas(self, node=None):
        if self.root is None:
            raise Exception("El árbol está vacío")
        if node is None:
            node = self.root
        if node.leftchild is None and node.rightchild is None:
            return 1
        hojas_izq = 0
        hojas_der = 0
        if node.leftchild:
            hojas_izq = self.contar_hojas(node.leftchild)
        if node.rightchild:
            hojas_der = self.contar_hojas(node.rightchild)
        return hojas_izq + hojas_der

arbol = BinaryTree()
for val in [50, 30, 70, 20, 40, 60]:  
    arbol.insert(val)

print(arbol.root)
cantidad_hojas = arbol.contar_hojas()
print(f"El árbol tiene {cantidad_hojas} hojas.")
