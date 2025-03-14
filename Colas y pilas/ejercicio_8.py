class Stack:
    def __init__(self):
        self.pila = []

    def empty(self):
        return len(self.pila) == 0

    def push(self, elementos: int) -> None:
        self.pila.append(elementos)

    def pop(self) -> int:
        if self.empty():
            raise Pila_vacia("No se puede eliminar elementos, ya que está vacía")
        return self.pila.pop()

    def peek(self) -> int:
        if self.empty():
            raise Pila_vacia("No hay elementos. Esta vacía")
        return self.pila[-1]

    def __repr__(self):
        return str(self.pila)

    def __len__(self):
        return len(self.pila)

    
    def imprimir_y_restaurar(self):
        temp = []  
        while not self.empty():
            elemento = self.pop()  
            print(elemento) 
            temp.append(elemento)  
        

# Ejemplo de uso
p = Stack()
p.push(6)
p.push(3)
p.push(8)
p.push(1)

# Usamos el nuevo método
p.imprimir_y_restaurar()

# Imprimimos la pila para verificar que se ha restaurado
print(p)