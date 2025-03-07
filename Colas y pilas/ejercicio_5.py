class QuickChat:
    def __init__(self):
        self.q = []

    def enqueue(self, mensaje: str) -> None:
        self.q.append(mensaje)

    def dequeue(self):
        if not self.is_empty():
            return self.q.pop(0)
        return None

    def first(self):
        if not self.is_empty():
            return self.q[0]
        return None

    def is_empty(self) -> bool:
        return len(self.q) == 0

    def __repr__(self):
        return str(self.q)
    
    def eliminacion(self):
        pass

# Ejemplo de uso
q = QuickChat()
q.enqueue("Hola como estas")
q.enqueue("¿Cómo estas?")
q.enqueue("Adios")
q.enqueue("Adios")
q.enqueue("Ayuda")
print(q)
q.dequeue()
print(q)



