class PQ:
    def __init__(self, p: str = "max"):
        self.q = []
        self.p = p
    
    def enqueue (self, elementos: int)-> None:

        self.q.append(elementos)
        self.q.sort(reverse=(self.p == "max"))

    def dequeue (self):

        if len(self.q) == 0:
            return None
        return self.q.pop
    
    def first (self):
        if len(self.q) == 0:
            return None 
        return self.q[0] 

    def __repr__(self) -> str:
        return f"prioridad({self.q},p = {self.p})"
    

q = PQ("min")
q.enqueue(5)
print(q.enqueue)
q.enqueue(2)
print(q.enqueue)
q.enqueue(7)
print(q.enqueue)




q = PQ("max")
q.enqueue(5)
print(q.enqueue)
q.enqueue(2)
print(q.enqueue)
q.enqueue(7)
print(q.enqueue)