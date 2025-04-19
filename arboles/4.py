class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def _repr(self, level=0):
        result = "  " * level + f"{self.value}\n"
        for child in self.children:
            result += child._repr(level + 1)
        return result

    def __repr__(self):
        return self._repr()
    
    
class GeneralTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, parent, child, current_node=None):
        if current_node is None:
            current_node = self.root

        if self.root is None:
            self.root = Node(parent)
            self.root.children.append(Node(child))
            return True

        if current_node.value == parent:
            current_node.children.append(Node(child))
            return True

        for ch in current_node.children:
            if self.insert(parent, child, ch):
                return True
        return False


    def eliminar(self, value, node=None, parent=None):
        if node is None:
            node = self.root
        if node is None:  # Árbol vacío
            return False

        eliminado = False
        
        # Verificar si es nodo hoja y coincide con el valor
        if node.value == value and len(node.children) == 0:
            if parent is None: 
                self.root = None
                eliminado = True
            else:  
                parent.children.remove(node)
                eliminado = True
            return eliminado  

   
        for child in node.children.copy():  
            if self.eliminar(value, child, node):
                eliminado = True
        return eliminado

    def __repr__(self):
        return self.root._repr() if self.root else "<árbol vacío>"


# Ejemplo de uso
gt = GeneralTree()
gt.insert(5, 6)
gt.insert(5, 7)
gt.insert(5, 8)
gt.insert(6, 9)
gt.insert(9, 10)

print("Árbol original:")
print(gt)


print(gt.eliminar(10))
print(gt)


print(gt.eliminar(8))
print(gt)


