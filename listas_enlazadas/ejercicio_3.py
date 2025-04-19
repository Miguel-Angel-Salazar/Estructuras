#Objetos tipo nodo
class Dnode():
  def __init__(self, value: int, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

    def __repr__(self):
      return str(self.value)

#print(b.prev.value)

class DoubleLinkedList():
  def __init__(self, head: Dnode = None, tail: Dnode = None, size: int = 0):
    self.head: Dnode = head
    self.tail: Dnode = tail
    self.size: int = 0

  #Agregar un nuevo nodo al final
  def append(self, value):
    new_node = Dnode(value)
    if(self.size == 0):
      self.head = new_node
      self.tail = new_node

    else:
      self.tail.next = new_node
      self.new_node.prev = self.tail
      self.tail = new_node

    self.size += 1


  def traverse(self, current_node = None, flag = True):
    if(flag == True):
      current_node = self.head

    if(current_node is None):
      return

    print(current_node.value)

    current_node = current_node.next
    self.traverse(current_node, False)

  def traverse_inverso(self, current_node=None, flag = True):
    if(flag == True):
      current_node = self.tail

    if(current_node is None):
      return

    print(current_node.value)

    current_node = current_node.prev
    self.traverse_inverso(current_node, False)

  #Eliminar el ultimo nodo
  def pop_Dblinked(self):
    if self.size == 0:
      raise Exception("La lista está vacía")

    else:
      self.tail = self.tail.prev
      self.tail.next.prev = None
      self.tail.next = None
    self.size -= 1

  #Agregar un nodo al final
  def push_Dblinked(self, value):
    new_node = Dnode(value)
    if self.size == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail.next.prev = self.tail
      self.tail = new_node
    self.size += 1

  def peek(self):
    if self.size == 0:
        raise Exception("La lista está vacía")
    else:
        return self.tail.value

  def __repr__(self) -> str:
    current_node = Dnode(self)
    if self.size == 0:
      return "[]"  # Lista vacía

    current_node = self.head
    representation = "["
    while current_node is not None:
      representation += str(current_node.value)
      if current_node.next is not None:
        representation += "-> "
      current_node = current_node.next
    representation += "]"
    return representation

class Pila():
    def __init__(self):
        self.pila = DoubleLinkedList()

    def pop(self):
        if self.pila.size > 0:
            self.pila.pop_Dblinked()
        else:
            raise Exception("La pila está vacía")

    def push(self, value):
        self.pila.push_Dblinked(value)

    def peek(self):
        return self.pila.peek() 
    
mi_pila = Pila()
mi_pila.push(10)
mi_pila.push(20)
mi_pila.push(30)

print(mi_pila.peek())

mi_pila.pop()
print(mi_pila.peek())