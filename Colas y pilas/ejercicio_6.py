class Pila_vacia(Exception):
    pass


class Stack:
    def __init__(self):
        self.pila = []
    
    def empty (self):
        return len(self.pila) == 0

    def push (self, elementos: int) -> None:
        self.pila.append(elementos)
            

    def pop (self) -> int:
        if  self.empty():
            raise Pila_vacia("No se puede eliminar elementos, ya que esta vacia")
        return self.pila.pop()
    
    def peek(self) -> int:
        if self.empty():
            raise Pila_vacia("No hay elementos. Esta vacia")
        return self.pila[-1]
    
    def __repr__(self):
        return str(self.pila)
    
    def __len__(self):
        return len(self.pila)
    
p = Stack()
p.push(6)
print(p)
p.push(3)
print(p)
print(p.pop())
print(p.peek())
