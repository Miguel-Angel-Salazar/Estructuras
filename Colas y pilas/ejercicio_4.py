class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, elemento):
        self.q.append(elemento)

    def dequeue(self):
        if not self.vacia():
            return self.q.pop(0)
        return None

    def vacia(self):
        return len(self.q) == 0

    def buscar(self, elemento):
        return elemento in self.q
    
    def __repr__(self):
        return str (self.q)

q = Queue()
q.enqueue(4)
q.enqueue(8)
q.enqueue(2)
print(q)
print(q.buscar(4))
print(q.buscar(5))
