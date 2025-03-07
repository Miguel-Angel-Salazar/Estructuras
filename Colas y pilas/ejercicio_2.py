class Queue:
    def __init__(self):
        self.q = {}
        self.key = 0
        self.ubicacion = 0
    
    
    def enqueue(self, elemento : int) -> None:
        self.q[self.ubicacion] = elemento
        self.ubicacion += 1
    
    def dequeue(self) -> int:
        elemento = self.q[self.key]
        del self.q[self.key]
        self.key += 1
        return elemento
    
    def first(self):
        return self.q[self.key]
    
    def __repr__(self):
        return str(self.q)
    
    
    
q = Queue()

q.enqueue(1)
print(q.enqueue)
q.enqueue(2)
print(q.enqueue)
q.enqueue(3)
print(q.enqueue)
q.dequeue()
print(q.dequeue)
q.dequeue()
print(q.dequeue)
q.first()
print(q.first)
