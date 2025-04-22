class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None

    def _repr(self, level=0):
        result = "  " * level + f"{self.value}\n"
        if self.leftchild:
            result += self.leftchild._repr(level + 1)
        if self.rightchild:
            result += self.rightchild._repr(level + 1)
        return result

    def __repr__(self):
        return self._repr()

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinaryNode(value)   
        