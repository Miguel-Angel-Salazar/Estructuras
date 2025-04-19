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

        if node.value == value:
            if parent is None:  # Es la raíz
                if not node.children:  # Raíz sin hijos
                    self.root = None
                    return True
                else:  
                    return False
            else:  # Nodo no raíz
                # Eliminar el nodo del padre y mover sus hijos
                parent.children.remove(node)
                parent.children.extend(node.children)
                return True

        for child in node.children:
            if self.eliminar(value, child, node):  # node actúa como padre aquí
                return True
        return False

    def __repr__(self):
        return self.root._repr() if self.root else "<árbol vacío>"


# Ejemplo de uso
gt = GeneralTree()
gt.insert(5, 6)
gt.insert(5, 7)
gt.insert(5, 8)
gt.insert(5, 9)
gt.insert(6, 9)
gt.insert(9, 10)
print("Árbol original:")
print(gt)

gt.eliminar(9)
print(gt)  

gt.eliminar(9)
print(gt)  
