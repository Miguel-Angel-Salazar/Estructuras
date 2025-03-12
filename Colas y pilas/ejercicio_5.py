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

    def filtrar_duplicados(self):
        mensajes_vistos = set()
        cola_filtrada = QuickChat()

        def _filtrar_recursivo():
            if self.is_empty():
                return cola_filtrada
            mensaje = self.dequeue()
            if mensaje not in mensajes_vistos:
                mensajes_vistos.add(mensaje)
                cola_filtrada.enqueue(mensaje)
            return _filtrar_recursivo()

        return _filtrar_recursivo()

q = QuickChat()
q.enqueue('Hola')
q.enqueue("¿Cómo estás?")
q.enqueue("Hola")
q.enqueue("Nos vemos")
q.enqueue("Ok")
q.enqueue("¿Cómo estás?")
q.enqueue("Ok")
q.enqueue("Ok")

chat_filtrado = q.filtrar_duplicados()
print(chat_filtrado)  



