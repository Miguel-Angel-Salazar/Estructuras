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

    def buscar(self, value, node=None):
        if node is None:
            node = self.root  
        if node is None: 
            return False
        if node.value == value: 
            return True
        if value < node.value:
            return self.buscar(value, node.leftchild)
        else:
            return self.buscar(value, node.rightchild)

arbol = BinaryTree()
for val in [100, 50,20,55,53]:  
    arbol.insert(val)

print(arbol.root)

print(arbol.buscar(50))