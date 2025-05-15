import time
import os

class Mensaje:

    palabras_clave = {
    "emergencia": 10, "urgente": 8, "fallo crítico": 9,
    "problema": 5, "consulta": 2, "duda": 1
    }

    def __init__(self, mensaje: str):
        self.mensaje: str = mensaje
        self.prioridad: int = self.calcular_prioridad()

    def calcular_peso_palabras_clave(self) -> int:

        peso_palabras_clave = 0
       
        for i in self.palabras_clave.keys():
            if i in self.mensaje:
                peso_palabras_clave += self.palabras_clave[i]
       
        return peso_palabras_clave
    
    def calcular_prioridad(self) -> int:

        prioridad = (len(self.mensaje)/10 + self.calcular_peso_palabras_clave()/2)
        return int(prioridad)
    
    def __repr__(self):
        return f"{self.mensaje[:5]}, {self.prioridad}"
    

class Agente:

    def __init__(self, id: int, nivel_experiencia: str, estado: str, mensaje: Mensaje = Mensaje("")):

        self.id: int = id
        self.nivel_experiencia: str = nivel_experiencia.lower()
        self.estado: str = estado
        self.tiempo_de_respuesta: float = self.calcular_tiempo_de_respuesta(mensaje)
        self.mensaje: Mensaje = mensaje
        self.factor_de_nivel: float = self.calcular_factor_de_nivel()
   
    def calcular_factor_de_nivel(self) -> int:

        if self.nivel_experiencia == "básico":
            factor_de_nivel = 1.0

        elif self.nivel_experiencia == "intermedio":
            factor_de_nivel = 0.75

        elif self.nivel_experiencia == "experto":
            factor_de_nivel = 0.5
       
        return factor_de_nivel
    def calcular_tiempo_de_respuesta(self, mensaje: Mensaje) -> float:

        tiempo_base = (len(mensaje.mensaje) / 10) + (mensaje.calcular_peso_palabras_clave() / 2)
        return tiempo_base * self.calcular_factor_de_nivel()


class EmptyQueue(Exception):
    pass

class Priority_Queue:

    def __init__(self,):

        self.queue: list[Mensaje | Agente] = []
    
    def enqueue(self, elemento: Mensaje):

        if (len(self.queue) == 0):
            self.queue.append(elemento)
            return

        for index, mensaje in enumerate(self.queue):
            if elemento.prioridad > mensaje.prioridad:
                self.queue.insert(index, elemento)
                return
        self.queue.append(elemento) 
    
    def enqueue_agentes(self, agente: Agente):

        if (len(self.queue) == 0):
            self.queue.append(agente)
            return
        
        for index, ag in enumerate(self.queue):
            if ag.factor_de_nivel > agente.factor_de_nivel:
                self.queue.insert(index, agente)
                return
        self.queue.append(agente)

    def dequeue(self):

        if(len(self.queue) == 0):
            raise EmptyQueue("Cola Vacía...")
        return self.queue.pop(0)

    def first(self):
        if(len(self.queue) == 0):
            raise EmptyQueue("Cola Vacía...")
        return self.queue[0]
    
    def __repr__(self):
        return f"{self.queue}"

class CallCenter:

    def __init__(self, agentes: Priority_Queue, cola_mensajes: Priority_Queue):
        self.agentes = agentes
        self.cola_mensajes = cola_mensajes  
    
    def atender_mensajes_pro(self):

        aux_cola = Priority_Queue()

        while self.cola_mensajes.queue and self.agentes.queue:  
            agente = self.agentes.dequeue()  

            if not self.cola_mensajes.queue: 
                self.agentes.enqueue_agentes(agente)  
                break
            
            for m in self.cola_mensajes.queue:
                print(self.cola_mensajes)
                msj = self.cola_mensajes.dequeue()
                ms = self.cola_mensajes.first()
                print(ms)
                if msj.prioridad == ms.prioridad:
                    aux_cola.enqueue(msj)
                elif msj.prioridad != ms.prioridad:
                    mensaje = msj
                    agente.estado = "ocupado"
                    break
            

            print(f"👨‍💼 Agente {agente.id} ({agente.nivel_experiencia}) atiende el mensaje: '{mensaje.mensaje}' con prioridad {mensaje.prioridad}")

            tiempo_respuesta = agente.calcular_tiempo_de_respuesta(mensaje)
            print(f"⌛ Tiempo estimado: {tiempo_respuesta:.2f} segundos")

            time.sleep(tiempo_respuesta)  
            print(f"✅ Agente {agente.id} ha finalizado la atención.\n")

            agente.estado = "disponible"
            self.agentes.enqueue_agentes(agente)

        print("🎉 Todos los mensajes han sido atendidos.")

    def atender_mensajes(self):

        while self.cola_mensajes.queue and self.agentes.queue:  
            agente = self.agentes.dequeue()

            if not self.cola_mensajes.queue: 
                self.agentes.enqueue_agentes(agente)  
                break

            mensaje = self.cola_mensajes.dequeue() 
            agente.estado = "ocupado"

            print(f"👨‍💼 Agente {agente.id} ({agente.nivel_experiencia}) atiende el mensaje: '{mensaje.mensaje}'")

            tiempo_respuesta = agente.calcular_tiempo_de_respuesta(mensaje)
            print(f"⌛ Tiempo estimado: {tiempo_respuesta:.2f} segundos")

            time.sleep(tiempo_respuesta)
            print(f"✅ Agente {agente.id} ha finalizado la atención.\n")

            agente.estado = "disponible"
            self.agentes.enqueue_agentes(agente)
        print("🎉 Todos los mensajes han sido atendidos.")
                    
def cargar_mensajes(cola_prioridad: Priority_Queue):
    ruta = os.path.join(os.path.dirname(__file__), "mensajes_call_center_coherentes.txt")
    with open(ruta, "r", encoding = "utf-8") as file:
        for linea in file:
            mensaje = Mensaje(linea.strip())
            cola_prioridad.enqueue(mensaje)


agente1 = Agente(id=1, nivel_experiencia="experto", estado="disponible")
agente2 = Agente(id=2, nivel_experiencia="intermedio", estado="ocupado")
agente3 = Agente(id=3, nivel_experiencia="experto", estado="disponible")
agente4 = Agente(id=4, nivel_experiencia="básico", estado="disponible")

agentes = Priority_Queue()

agentes.enqueue_agentes(agente2)
agentes.enqueue_agentes(agente4)
agentes.enqueue_agentes(agente1)
agentes.enqueue_agentes(agente3)

cola_prioridad = Priority_Queue()
call_center = CallCenter(agentes, cola_prioridad)

cargar_mensajes(cola_prioridad)

call_center.atender_mensajes()