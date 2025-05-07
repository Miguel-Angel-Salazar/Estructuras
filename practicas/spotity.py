import random
import time
import sys


# Clase Nodo Doblemente Enlazado (Dnode)

class Dnode:
    def __init__(self, value, next=None, prev=None):
        self.value = value    
        self.next = next      
        self.prev = prev      

    def __repr__(self):
        return str(self.value)  

# Lista Doblemente Enlazada 
class DoubleLinkedList:
    def __init__(self):
        self.head = None      
        self.tail = None      
        self.size = 0         

    # Añade un nodo al final de la lista
    def append(self, value):
        new_node = Dnode(value)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # Elimina un nodo específico de la lista
    def remove(self, node):
        if self.size == 0:
            raise Exception("Lista vacía")

        if self.size == 1:
            self.head = self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self.size -= 1
        node.prev = node.next = None  # Limpiar referencias

    # Representación visual de la lista
    def __repr__(self):
        if self.size == 0:
            return "[]"
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return "[ <-> ".join(elements) + "]"


class Song:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration  

    def __repr__(self):
        return f"{self.title} - {self.artist} ({self.duration}s)"  


# Clase Playlist

class Playlist:
    def __init__(self):
        self.songs = DoubleLinkedList()   # Lista de canciones
        self.current_song = None           # Canción actualmente en reproducción
        self.shuffle_mode = False          # Estado del modo aleatorio
        self.shuffle_list = []             # Lista auxiliar para shuffle

    # Verifica si una canción ya existe en la playlist
    def song_exists(self, title: str) -> bool:
        current = self.songs.head
        while current:
            if current.value.title.lower() == title.lower():
                return True
            current = current.next
        return False

    # Añade una canción a la playlist
    def add_song(self, song: Song):
        if self.song_exists(song.title):
            print("\n❌ Error: Canción ya existe en la playlist")
            return
        
        self.songs.append(song)
        if self.songs.size == 1:  # Primera canción añadida
            self.current_song = self.songs.head
        print(f"\n✅ '{song.title}' añadida exitosamente!")

    # Avanza a la siguiente canción (comportamiento circular)
    def next_song(self):
        if not self.current_song:
            print("\n⚠️  Playlist vacía")
            return
        
        if self.shuffle_mode:
            self._handle_shuffle_next()
        else:
            self.current_song = self.current_song.next if self.current_song.next else self.songs.head
        print(f"\n⏭  Siguiente canción: {self.current_song.value}")

    # Retrocede a la canción anterior (comportamiento circular)
    def previous_song(self):
        if not self.current_song:
            print("\n⚠️  Playlist vacía")
            return
        
        if self.shuffle_mode:
            self._handle_shuffle_prev()
        else:
            self.current_song = self.current_song.prev if self.current_song.prev else self.songs.tail
        print(f"\n⏮  Canción anterior: {self.current_song.value}")

    # Elimina una canción por título
    def delete_song(self, title: str):
        current = self.songs.head
        while current:
            if current.value.title.lower() == title.lower():
                if current == self.current_song:
                    self.next_song()  # Cambiar a siguiente antes de eliminar
                self.songs.remove(current)
                print(f"\n✅ '{title}' eliminada exitosamente!")
                if self.songs.size == 0:
                    self.current_song = None
                return
            current = current.next
        print("\n❌ Canción no encontrada")

# Eliminar las canciones del artista que menos tiene
    def delete_least_frequent_artist(self):
        if self.songs.size == 0: 
            print("\n⚠️  La playlist está vacía")
            return

        artist_count = {} 
        current = self.songs.head 
        while current: 
            artist = current.value.artist.lower() 
            artist_count[artist] = artist_count.get(artist, 0) + 1 
            current = current.next 

        min_count = min(artist_count.values(), default=0) 
        least_artists = [artist for artist, count in artist_count.items() if count == min_count] 
        
        nodes_to_remove = [] 
        current = self.songs.head 
        while current: 
            if current.value.artist.lower() in least_artists: 
                nodes_to_remove.append(current)
            current = current.next 

        for node in nodes_to_remove: 
            self.songs.remove(node) 
            if self.current_song == node:
                self.current_song = self.songs.head if self.songs.size > 0 else None 

        print(f"\n 🗑️ Eliminadas {len(nodes_to_remove)} canciones de: {', '.join(least_artists)}") 

    def moda(self):
        if self.songs.size == 0: 
            print("\n⚠️  La playlist está vacía")
            return

        frecuencias = {}
        current = self.songs.head
        while current:
            frecuencias[current.value.duration] = frecuencias.get(current.value.duration, 0) + 1
            current = current.next

        moda = max(frecuencias, key=frecuencias.get)

        current = self.songs.head
        while current:
            if current.value.duration == moda and current.value.duration > 10:
                current.value.duration -= 1
            current = current.next

        print(f"Se redujo -1s a las canciones de {moda}s")

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
        idx = 1
        while current:
            prefix = "▶️ " if current == self.current_song else "  "
            print(f"{prefix}{idx}. {current.value}")
            current = current.next
            idx += 1

    # Activa/desactiva el modo aleatorio
    def toggle_shuffle(self):
        self.shuffle_mode = not self.shuffle_mode
        if self.shuffle_mode:
            self._generate_shuffle_list()
            print("\n🔀 Modo aleatorio ACTIVADO")
        else:
            print("\n🔀 Modo aleatorio DESACTIVADO")

    # Genera lista aleatoria sin repeticiones
    def _generate_shuffle_list(self):
        self.shuffle_list = []
        current = self.songs.head
        while current:
            self.shuffle_list.append(current)
            current = current.next
        random.shuffle(self.shuffle_list)
        self.current_shuffle_idx = 0 # Muestra la lista (opcional)

    # Maneja la navegación en modo shuffle
    def _handle_shuffle_next(self):
        if self.current_shuffle_idx < len(self.shuffle_list) - 1:
            self.current_shuffle_idx += 1
        else:
            self.current_shuffle_idx = 0  # Comportamiento circular
        self.current_song = self.shuffle_list[self.current_shuffle_idx]

    def _handle_shuffle_prev(self):
        if self.current_shuffle_idx > 0:
            self.current_shuffle_idx -= 1
        else:
            self.current_shuffle_idx = len(self.shuffle_list) - 1  # Circular
        self.current_song = self.shuffle_list[self.current_shuffle_idx]

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
            self.simulate_playback(skip_time)  


    # Simula la reproducción con barra de progreso
    def simulate_playback(self, start=0):
        if not self.current_song:
            return
        
        song = self.current_song.value
        print(f"\n▶️  Reproduciendo: {song}")
        
        for sec in range(int(start), song.duration):
            progress = (sec + 1) / song.duration * 50  
            bar = "[" + "=" * int(progress) + " " * (50 - int(progress)) + "]"
            sys.stdout.write(f"\r⏳ {sec+1}s {bar}")
            sys.stdout.flush()
            time.sleep(1)
        
        print(f"\n✅ '{song.title}' finalizada")
        self.next_song()

    # Genera una subplaylist
    def create_subplaylist(self, titles: list):
        sub = Playlist()
        titles = [t.strip().lower() for t in titles]
        
        current = self.songs.head
        while current:
            if current.value.title.lower() in titles:
                sub.add_song(current.value)
            current = current.next
        
        print(f"\n🎉 Subplaylist creada con {sub.songs.size} canciones")
        return sub
    
    def subplaylistcorta(self,titles:list):
        sub_1 = Playlist()
        
        current = self.songs.head
        while current:
            if current.value.duration <= 13:
                sub_1.add_song(current.value)
            current = current.next

        print(f"\n🎉 Subplaylist creada con {sub_1.songs.size} canciones")
        return sub_1


    
# Interfaz de Usuario

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
        print("1️⃣ 3️⃣   Reducir cancion moda")
        print("1️⃣ 4️⃣ subplaylist de canciones cortas")
        print("⏹   Salir")
        
        choice = input("\n👉  Seleccione una opción: ").strip()
        
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
        
        elif choice == "2":
            playlist.next_song()
        
        elif choice == "3":
            playlist.previous_song()
        
        elif choice == "4":
            title = input("\nTítulo a eliminar: ").strip()
            playlist.delete_song(title)
        
        elif choice == "5":
            playlist.show_current()
        
        elif choice == "6":
            playlist.show_all()
        
        elif choice == "7":
            playlist.toggle_shuffle()
        
        elif choice == "8":
            try:
                pct = float(input("\nPorcentaje a adelantar: "))
                playlist.skip(pct)
            except:
                print("⚠️  Ingrese un valor numérico válido")
        
        elif choice == "9":
            titles = input("\nIngrese títulos (separados por coma): ").split(",")
            sub = playlist.create_subplaylist(titles)
            if sub.songs.size > 0:
                if input("¿Usar esta subplaylist ahora? (s/n): ").lower() == "s":
                    playlist = sub
                    print("\n🔄 Playlist principal actualizada!")

        elif choice == "10":
            if playlist.current_song:
                playlist.simulate_playback()
            else:
                print("\n⚠️  No hay canción seleccionada")

        elif choice == "12":
            playlist.delete_least_frequent_artist()

        elif choice == "13":
            playlist.moda()

        elif choice =="14":

            titles = input("\nIngrese títulos (separados por coma): ").split(",")
            sub_1 = playlist.subplaylistcorta(titles)
            if sub_1.songs.size > 0:
                if input("¿Usar esta subplaylist ahora? (s/n): ").lower() == "s":
                    playlist = sub_1
                    print("\n🔄 Playlist principal actualizada!")

        elif choice.lower() in ["salir", "exit", "⏹"]:
            print("\n🎶  Gracias por usar la playlist!  🎶")
            break
        
        else:
            print("\n⚠️  Opción no válida")

if __name__ == "__main__":
    main()
