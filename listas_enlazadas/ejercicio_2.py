
class Node:
    def __init__(self, elemento: int):
        self.elemento = elemento
        self.next = None

def invertir(nodo: Node):
    def _invertirrecursivo(actual: Node, prev: Node) -> Node:
        if actual is None:
            return prev
        siguiente_node = actual.next
        actual.next = prev
        return _invertirrecursivo(siguiente_node, actual)
    return _invertirrecursivo(nodo, None)

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

new_list = invertir(Node1)

print(new_list.elemento)
print(new_list.next.elemento)
print(new_list.next.next.elemento)
print(new_list.next.next.next.elemento)
print(new_list.next.next.next.next.elemento)