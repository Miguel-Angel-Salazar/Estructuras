import random # Importa random para el modo aleatorio (shuffle)
import time # Importa el módulo time para usar sleep y simular la reproducción
import sys # Importa el módulo sys para manipular la salida estándar

# =============================================
# Clase Nodo Doblemente Enlazado (Dnode)
# =============================================
class Dnode:
    def __init__(self, value, next=None, prev=None):
        self.value = value    # Valor almacenado (canción)
        self.next = next      # Referencia al siguiente nodo
        self.prev = prev      # Referencia al nodo anterior

    def __repr__(self):
        return str(self.value)  # Representación legible del nodo

# =============================================
# Lista Doblemente Enlazada (DoubleLinkedList)
# =============================================
class DoubleLinkedList:
    def __init__(self):
        self.head = None      # Primer nodo de la lista
        self.tail = None      # Último nodo de la lista
        self.size = 0         # Cantidad de elementos

    # Añade un nodo al final de la lista
    def append(self, value): # Método que añade un nuevo nodo con el valor dado al final de la lista
        new_node = Dnode(value) # Crea un nuevo nodo con el valor proporcionado
        if self.size == 0: # Si la lista está vacía (tamaño 0)
            self.head = self.tail = new_node # El nuevo nodo es tanto la cabeza como la cola
        else: # Si la lista no está vacía
            new_node.prev = self.tail # El nodo anterior del nuevo nodo es el nodo cola actual
            self.tail.next = new_node # El nodo siguiente de la cola actual es el nuevo nodo
            self.tail = new_node # Se actualiza la cola a este nuevo nodo
        self.size += 1 # Incrementa el tamaño de la lista en 1

    # Elimina un nodo específico de la lista
    def remove(self, node):
        if self.size == 0:
            raise Exception("Lista vacía")

        # Caso: Único nodo
        if self.size == 1:
            self.head = self.tail = None # Se eliminan ambas referencias (la lista queda vacía)
        
        # Caso: Nodo es la cabeza
        elif node == self.head:
            self.head = self.head.next  # Se actualiza la cabeza al siguiente nodo
            self.head.prev = None # El nuevo primer nodo ya no tiene anterior
        
        # Caso: Nodo es la cola
        elif node == self.tail:
            self.tail = self.tail.prev # Se actualiza la cola al nodo anterior
            self.tail.next = None # El nuevo último nodo ya no tiene siguiente
        
        # Caso: Nodo en medio
        else:
            node.prev.next = node.next # Se enlaza el nodo anterior con el nodo siguiente
            node.next.prev = node.prev # Se enlaza el nodo siguiente con el nodo anterior
        
        self.size -= 1  # Se reduce el tamaño de la lista en 1
        node.prev = node.next = None  # Se eliminan las referencias del nodo eliminado (por limpieza)

    # Representación visual de la lista
    def __repr__(self):
        if self.size == 0:
            return "[]"
        elements = []
        current = self.head
        while current:  # Mientras no se llegue al final
            elements.append(str(current.value)) # Agrega el valor del nodo a la lista
            current = current.next  # Avanza al siguiente nodo
        return "[ <-> ".join(elements) + "]" # Une los valores con "<->" como conector visual

# =============================================
# Clase Canción (Song)
# =============================================
class Song:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration  # Duración en segundos (10-15)

    def __repr__(self):
        return f"{self.title} - {self.artist} ({self.duration}s)"  # Formato canción

# =============================================
# Clase Playlist
# =============================================
class Playlist:
    def __init__(self):
        self.songs = DoubleLinkedList()   # Lista de canciones
        self.current_song = None           # Canción actualmente en reproducción
        self.shuffle_mode = False          # Estado del modo aleatorio
        self.shuffle_list = []             # Lista auxiliar para shuffle
        self.shuffled_index = 0
        self.shuffled_order = []  # Almacenará el orden aleatorio completo
        self.current_cycle = []   # Canciones pendientes del ciclo actual

    # Verifica si una canción ya existe en la playlist
    def song_exists(self, title: str) -> bool: # Verifica si una canción ya existe en la playlist por título
        current = self.songs.head # Comienza desde el inicio de la lista
        while current: # Recorre la lista nodo por nodo
            if current.value.title.lower() == title.lower(): # Compara ignorando mayúsculas/minúsculas
                return True # Retorna True si encuentra una coincidencia
            current = current.next # Avanza al siguiente nodo
        return False # Si termina el recorrido sin encontrar, retorna False

    # Añade una canción a la playlist
    def add_song(self, song: Song):
        if self.song_exists(song.title): # Verifica si ya existe para evitar duplicados
            print("\n❌ Error: Canción ya existe en la playlist")
            return
        
        self.songs.append(song) # Añade la canción al final de la lista
        if self.songs.size == 1:  # Primera canción añadida
            self.current_song = self.songs.head # La establece como la canción actual
        print(f"\n✅ '{song.title}' añadida exitosamente!") # Confirma adición

    # Avanza a la siguiente canción (comportamiento circular)
    def next_song(self):
        if not self.current_song:
            print("\n⚠️  Playlist vacía")
            return
        
        if self.shuffle_mode: # Si el modo aleatorio está activado
            self._handle_shuffle_next() # Usa la lógica de shuffle  
        else:
            self.current_song = self.current_song.next if self.current_song.next else self.songs.head # representa el nodo actual y lo compara si hay otro sigue, si no se devuelve al inicio
        print(f"\n⏭  Siguiente canción: {self.current_song.value}") #muestra la cancion

    # Retrocede a la canción anterior (comportamiento circular)
    def previous_song(self):
        if not self.current_song:
            print("\n⚠️  Playlist vacía")
            return
        
        if self.shuffle_mode:
            self._handle_shuffle_prev()
        else:
            self.current_song = self.current_song.prev if self.current_song.prev else self.songs.tail # representa el nodo actual y lo compara si hay otro retrocede, si no se devuelve al final
        print(f"\n⏮  Canción anterior: {self.current_song.value}")

    # Elimina una canción por título
    def delete_song(self, title: str):
        current = self.songs.head
        while current:
            if current.value.title.lower() == title.lower():
                if current == self.current_song: # Si es la canción actual
                    self.next_song()  # Cambiar a siguiente antes de eliminar
                self.songs.remove(current)  # Elimina el nodo
                print(f"\n✅ '{title}' eliminada exitosamente!")
                if self.songs.size == 0:
                    self.current_song = None
                return
            current = current.next
        if self.shuffle_mode:
        # Remover de ambas listas si existe
            self.shuffled_order = [n for n in self.shuffled_order 
                                if n.value.title.lower() != title.lower()]
            self.current_cycle = [n for n in self.current_cycle 
                                if n.value.title.lower() != title.lower()]
        print("\n❌ Canción no encontrada")

# Eliminar las canciones del artista que menos tiene
    def delete_least_frequent_artist(self):
        if self.songs.size == 0: #compara para ver si esta hacia la lista
            print("\n⚠️  La playlist está vacía")
            return

        artist_count = {} #almacena los valore del artista y la canciones
        current = self.songs.head # para poder recorrer todo desde la cabeza
        while current: #recorre todos los nodos
            artist = current.value.artist.lower() # pone el combre de los artistas en minus para evitar errores 
            artist_count[artist] = artist_count.get(artist, 0) + 1 #un contador para guardar a los artistas y va sumando
            current = current.next #acceder al valor del siguiente nodo

        min_count = min(artist_count.values(), default=0) #para asi guardar los valores minimos de las canciones que hay, y se ponde el default para evitar errores por si esta vacia 
        least_artists = [artist for artist, count in artist_count.items() if count == min_count] #para guardar a los artistas y sus canciones, el artist_count.items para guardar los valores en el diccionario, ademas el count == min_count filtra a los artistas los cuales sus canciones sean iguales al minimo
        
        nodes_to_remove = [] #almacenara los nodos que deseo eliminar
        current = self.songs.head # para poder recorrer todos los nodos desde la cabeza
        while current: #recorre toda la lista
            if current.value.artist.lower() in least_artists: #verificar si el artista se encuentra en la lista de least_artistis
                nodes_to_remove.append(current)# si el artista esta se añade
            current = current.next #acceder al siguiente

        for node in nodes_to_remove: #recorre los nodos que se encuetran en nodes_to_remove
            self.songs.remove(node) #se van a remover los nodos 
            if self.current_song == node:#se comparan el current con el node para ver si son la misma cancion
                self.current_song = self.songs.head if self.songs.size > 0 else None # el current_song es igual a las canciones que se encuentran en la cabeza entoncces son mas de 0 sino no hay nada

        print(f"\n 🗑️ Eliminadas {len(nodes_to_remove)} canciones de: {', '.join(least_artists)}") #imprime la cantidad de canciones eliminadas con el len(nodes_to_remove) y el nombre del artista
            

    # Muestra la canción actual
    def show_current(self):
        if self.current_song:
            print(f"\n🎵 Reproduciendo: {self.current_song.value}")
        else:
            print("\n⚠️  No hay canción en reproducción")

    # Muestra todas las canciones en orden
    def show_all(self):
        if self.songs.size == 0:
            print("\n📭 Playlist vacía")
            return
        
        print("\n📋 Playlist completa:")
        current = self.songs.head
        idx = 1 # Contador de canciones
        while current:
            prefix = "▶️ " if current == self.current_song else "  " # Marca la canción actual
            print(f"{prefix}{idx}. {current.value}") # Imprime la canción
            current = current.next
            idx += 1 # aumenta Contador de canciones

    # Activa/desactiva el modo aleatorio
    def toggle_shuffle(self):
        self.shuffle_mode = not self.shuffle_mode # Alterna entre True y False
        if self.shuffle_mode: # Si se activa
            self._generate_shuffle_list() # Genera nueva lista aleatoria
            print("\n🔀 Modo aleatorio ACTIVADO")
        else:
            print("\n🔀 Modo aleatorio DESACTIVADO")

    # Genera lista aleatoria sin repeticiones
    def _generate_shuffle_order(self):
        # Obtener todas las canciones como lista
        all_songs = []
        current = self.songs.head
        while current:
            all_songs.append(current)
            current = current.next
        
        # Crear orden aleatorio completo
        self.shuffled_order = all_songs.copy()
        random.shuffle(self.shuffled_order)
        
        # Iniciar nuevo ciclo
        self.current_cycle = self.shuffled_order.copy()
        self.shuffled_index = 0

    # Maneja la navegación en modo shuffle
    def _handle_shuffle_next(self):
        if not self.current_cycle:
            # Regenerar si se acabó el ciclo
            self._generate_shuffle_order()
            print("\n🔁 Ciclo completado, reiniciando shuffle...")
        
        # Tomar la primera canción del ciclo actual
        self.current_song = self.current_cycle.pop(0)
        self.shuffled_index += 1
        
        # Verificar si quedan pocas para preparar próximo ciclo
        if len(self.current_cycle) <= 1 and len(self.shuffled_order) > 2:
            self._generate_shuffle_order()
 
    def _handle_shuffle_prev(self):
        if self.current_shuffle_idx > 0:
            self.current_shuffle_idx -= 1
        else:
            self.current_shuffle_idx = len(self.shuffle_list) - 1  # Va al final si estaba al principio
        self.current_song = self.shuffle_list[self.current_shuffle_idx] # Actualiza la canción actual

    # Adelanta la reproducción un porcentaje
    def skip(self, percentage: float):
        if not self.current_song:
            print("\n⚠️  No hay canción en reproducción")
            return
        
        song = self.current_song.value
        skip_time = song.duration * (percentage / 100)
        
        if skip_time >= song.duration:
            print(f"\n⏩ Adelanto completo ({song.duration}s)")
            self.next_song()
        else:
            print(f"\n⏭ Adelantando {skip_time:.1f}s en '{song.title}'")
            time.sleep(skip_time)
            self.simulate_playback(skip_time)

    # Simula la reproducción con barra de progreso gpt
    def simulate_playback(self, start=0):
        if not self.current_song:
            return
        
        song = self.current_song.value
        print(f"\n▶️  Reproduciendo: {song}")
        
        for sec in range(int(start), song.duration):
            progress = (sec + 1) / song.duration * 50  # 50 caracteres de ancho
            bar = "[" + "=" * int(progress) + " " * (50 - int(progress)) + "]"
            sys.stdout.write(f"\r⏳ {sec+1}s {bar}")
            sys.stdout.flush()
            time.sleep(1)
        
        print(f"\n✅ '{song.title}' finalizada")
        self.next_song()

    # Genera una subplaylist
    def create_subplaylist(self, titles: list): 
        sub = Playlist() # Crea una nueva instancia de playlist
        titles = [t.strip().lower() for t in titles] # Convierte títulos a minúsculas sin espacios
        
        current = self.songs.head  # Comienza desde el inicio
        while current: # Recorre la lista
            if current.value.title.lower() in titles: # Si el título está en la lista
                sub.add_song(current.value) # Lo agrega a la subplaylist
            current = current.next # Avanza
        
        print(f"\n🎉 Subplaylist creada con {sub.songs.size} canciones")
        return sub

# =============================================
# Interfaz de Usuario
# =============================================
def main():
    playlist = Playlist()
    
    while True:
        print("\n" + "="*50)
        print("🎧  PLAYLIST INTERACTIVA  🎧".center(50))
        print("="*50)
        print("1️⃣  Añadir canción")
        print("2️⃣  Siguiente canción")
        print("3️⃣  Canción anterior")
        print("4️⃣  Eliminar canción")
        print("5️⃣  Mostrar canción actual")
        print("6️⃣  Mostrar todas las canciones")
        print("7️⃣  Modo aleatorio (ON/OFF)")
        print("8️⃣  Adelantar canción")
        print("9️⃣  Generar subplaylist")
        print("🔟  Reproducir canción actual")
        print("1️⃣ 2️⃣  Eliminar artistas menos frecuentes")
        print("⏹   Salir")
        
        choice = input("\n👉  Seleccione una opción: ").strip()
        
        # Opción 1: Añadir canción
        if choice == "1":
            print("\n" + "-"*30)
            title = input("Título: ").strip()
            artist = input("Artista: ").strip()
            
            while True:
                try:
                    duration = int(input("Duración (10-15s): "))
                    if 10 <= duration <= 15:
                        break
                    else:
                        print("⚠️  Duración debe ser entre 10 y 15 segundos")
                except:
                    print("⚠️  Ingrese un número válido")
            
            playlist.add_song(Song(title, artist, duration))
        
        # Opción 2: Siguiente canción
        elif choice == "2":
            playlist.next_song()
        
        # Opción 3: Canción anterior
        elif choice == "3":
            playlist.previous_song()
        
        # Opción 4: Eliminar canción
        elif choice == "4":
            title = input("\nTítulo a eliminar: ").strip()
            playlist.delete_song(title)
        
        # Opción 5: Mostrar actual
        elif choice == "5":
            playlist.show_current()
        
        # Opción 6: Mostrar todas
        elif choice == "6":
            playlist.show_all()
        
        # Opción 7: Modo aleatorio
        elif choice == "7":
            playlist.toggle_shuffle()
        
        # Opción 8: Adelantar
        elif choice == "8":
            try:
                pct = float(input("\nPorcentaje a adelantar: "))
                playlist.skip(pct)
            except:
                print("⚠️  Ingrese un valor numérico válido")
        
        # Opción 9: Subplaylist
        elif choice == "9":
            titles = input("\nIngrese títulos (separados por coma): ").split(",")
            sub = playlist.create_subplaylist(titles)
            if sub.songs.size > 0:
                if input("¿Usar esta subplaylist ahora? (s/n): ").lower() == "s":
                    playlist = sub
                    print("\n🔄 Playlist principal actualizada!")
        
        # Opción 10: Reproducir
        elif choice == "10":
            if playlist.current_song:
                playlist.simulate_playback()
            else:
                print("\n⚠️  No hay canción seleccionada")

        elif choice == "12":
            playlist.delete_least_frequent_artist()

        
        # Opción Salir
        elif choice.lower() in ["salir", "exit", "⏹"]:
            print("\n🎶  Gracias por usar la playlist!  🎶")
            break
        
        else:
            print("\n⚠️  Opción no válida")

if __name__ == "__main__":
    main()