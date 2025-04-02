class Node:
    def __init__(self, elemento: int):
        self.elemento = elemento
        self.next = None


    
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)

Node1.next = Node4
Node2.next = Node3
Node3.next = Node1
Node4.next = Node2

print(Node1.next.next.next.elemento)

