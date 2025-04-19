class Dnode():
    def __init__(self, value: int, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.value)

class DoubleLinkedList():
    def __init__(self):
        self.head: Dnode = None
        self.tail: Dnode = None
        self.size: int = 0

    def append(self, value):
        new_node = Dnode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


    def enqueue(self, value):
        new_node = Dnode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1


    def dequeue(self):
        if self.size == 0:
            raise Exception('La lista está vacía')
        
        value = self.tail.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value


    def retornar_primer_valor(self):
        if self.size == 0:
            raise Exception("La cola está vacía")
        return self.head.value

    # Representación de la lista
    def __repr__(self) -> str:
        if self.size == 0:
            return "[]"
        
        current_node = self.head
        representation = "["
        while current_node is not None:
            representation += str(current_node.value)
            if current_node.next is not None:
                representation += " <-> "
            current_node = current_node.next
        representation += "]"
        return representation

class Cola():
    def __init__(self):
        self.cola = DoubleLinkedList()

    def enqueue(self, value):
        self.cola.enqueue(value)

    def dequeue(self):
        if self.cola.size > 0:
            return self.cola.dequeue()
        else:
            raise Exception("La cola está vacía")

    def peek(self):
        return self.cola.retornar_primer_valor()

    def __repr__(self):
        return self.cola.__repr__()


mi_cola = Cola()
mi_cola.enqueue(10)
mi_cola.enqueue(20)
mi_cola.enqueue(30)
print("Cola inicial:", mi_cola)  

mi_cola.dequeue()
print("Después de dequeue:", mi_cola)  

mi_cola.dequeue()
print("Después de otro dequeue:", mi_cola)  #