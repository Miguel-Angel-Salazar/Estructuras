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

    def insert(self, parent, child, current_node = None):
      if(current_node is None):
        current_node = self.root

      if(self.root is None):
        self.root = Node(parent)
        self.root.children.append(Node(child))
        return True

      if(current_node.value == parent):
        current_node.children.append(Node(child))
        return True

      for ch in current_node.children:
        if (self.insert(parent, child, ch) == True):
           return True
      return False

    def Eliminar(self, value, node=None):
        if node is None:
            node = self.root  
        if node is None: 
            return False
        
        for i in range(len(node.children)):
               if node.children[i].value == value:
                  node.children.pop(i)
                  return True                
        
        for child in node.children: 
            if self.Eliminar(value, child):
                return True
        return False 

    def __repr__(self):
        return self.root._repr() if self.root else "<árbol vacío>"
    
  

gt = GeneralTree()
gt.insert(5,6)
gt.insert(5,7)
gt.insert(5,8)
gt.insert(5,9)
gt.insert(6,9)
gt.insert(9,10)

print(gt)

gt.Eliminar(6)

print(gt)
