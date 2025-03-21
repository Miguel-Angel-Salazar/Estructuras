class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, elemento):
        self.q.append(elemento)

    def dequeue(self):
        if not self.vacia():
            return self.q.pop(0)
        return None
    
    def first(self) -> int:
        if(len(self.q) == 0):
            return self.q[0]

    def vacia(self):
        return len(self.q) == 0

    def buscar(self, elemento):
        return elemento in self.q
    
    def __repr__(self):
        return str (self.q)
    
    def __len__(self):
     return len(self.q)


def buscar_elemento_en_cola(cola: Queue, elemento: int) -> bool:
    encontrado = True
    cola_aux: Queue = Queue()
    for _ in range(len(cola)):
        if cola.first() == elemento:
            encontrado = False
        cola_aux.enqueue(cola.dequeue())
    for _ in range(len(cola_aux)):
        cola.enqueue(cola_aux.dequeue())
    return encontrado

q = Queue()
q.enqueue(3)
q.enqueue(7)    
print(q)
print(buscar_elemento_en_cola(q, 3)) 



