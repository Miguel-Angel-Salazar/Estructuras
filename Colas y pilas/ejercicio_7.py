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
    
    def invertir(self) -> None:
        lista_inversa = []
        while not self.empty():
            lista_inversa.append(self.pop())
        self.pila = lista_inversa


    def __repr__(self):
        return str(self.pila)
    
    def __len__(self):
        return len(self.pila)
    
p = Stack()
p.push(1)
print(p)
p.push(2)
print(p)
p.push(3)
print(p)
p.push(4)
print(p)
print(p.peek())
p.invertir()
print(p)
print(p.peek())
