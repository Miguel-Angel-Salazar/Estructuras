class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.f = 0  
        self.r = 0 
        self.x = [None] * capacity  
        self.s = 0  

    def full(self):
        return self.s == self.capacity

    def empty(self):
       
        return self.s == 0

    def enqueue(self, elemento: int) -> None:
        if self.full():
            print("Circular queue full")
            return
        self.x[self.r] = elemento
        self.r = (self.r + 1) % self.capacity
        self.s += 1  

    def dequeue(self) -> int:
        if self.empty():
            print("Circular queue empty")
            return None
        elemento = self.x[self.f]
        self.x[self.f] = None
        self.f = (self.f + 1) % self.capacity
        self.s -= 1  
        return elemento

    def __repr__(self):
        return str(self.x)


# Prueba del código
x = CircularQueue(3)
x.enqueue(1)
print(x)
x.enqueue(2)
print(x)
x.enqueue(3)
print(x)
x.enqueue(4)
print(x)
x.dequeue()
print(x.dequeue)
