def moda(self):
    if self.songs.size == 0: 
        print("\n⚠️  La playlist está vacía")
        return

    frecuencias = {}
    current = self.songs.head
    while current:
        dur = current.value.duration
        if dur in frecuencias:
            frecuencias[dur] += 1
        else:
            frecuencias[dur] = 1
        current = current.next

    moda = max(frecuencias, key=frecuencias.__getitem__)

    current = self.songs.head
    while current:
        if current.value.duration == moda and current.value.duration > 10:
            current.value.duration -= 1
        current = current.next

    print(f"Se redujo -1s a las canciones de {moda}s")
