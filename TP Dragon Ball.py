import heapq

from collections import defaultdict, deque

#Para la clase personaje

#Defi clase Personaje con los atributos básicos: nombre, nivel_poder, habilidades, y raza. También le agregaremos métodos para subir de nivel y añadir habilidades.

class Personaje:
    def __init__(self, nombre, nivel_poder, raza):
        self.nombre = nombre
        self.nivel_poder = nivel_poder
        self.raza = raza
        self.habilidades = []

    def agregar_habilidad(self, habilidad):
        """Agrega una habilidad al personaje."""
        self.habilidades.append(habilidad)

    def subir_nivel(self, incremento_poder):
        """Aumenta el nivel de poder del personaje en función del incremento dado validando que el incremento sea un número positivo"""
        if incremento_poder <= 0:
           print(f"El incremento debe ser positivo. {self.nombre} no ha cambiado su nivel de poder.")
        if not isinstance(incremento_poder, (int, float)):
            print(f"El incremento debe ser un número.{self.nombre} no ha cambiado su nivel de poder.")
            return

        self.nivel_poder += incremento_poder
        print(f"{self.nombre} ha subido su nivel de poder a {self.nivel_poder:.2f}")

    def mostrar_info(self):
        """Muestra la información del personaje."""
        info = f"Nombre: {self.nombre}, Raza: {self.raza}, Nivel de Poder: {self.nivel_poder}, Habilidades: {self.habilidades}"
        print(info)

#Gestion de combates

#Para los combates, podemos implementar una función de enfrentamiento entre dos personajes que compare el nivel de poder.

def combate(personaje1, personaje2):
    """Realiza un combate entre dos personajes y determina el ganador."""
    if personaje1.nivel_poder > personaje2.nivel_poder:
        print(f"{personaje1.nombre} ha ganado el combate contra {personaje2.nombre}")
        personaje1.subir_nivel(personaje2.nivel_poder * 0.1)  # Ejemplo: el ganador aumenta un 10% del poder del oponente
    elif personaje2.nivel_poder > personaje1.nivel_poder:
        print(f"{personaje2.nombre} ha ganado el combate contra {personaje1.nombre}")
        personaje2.subir_nivel(personaje1.nivel_poder * 0.1)
    else:
        print("El combate ha terminado en empate.")

#Transformaciones

#Podemos implementar una función recursiva que aplique multiplicadores a nivel_poder.

def transformar(personaje, multiplicador, nivel_transformacion):
    """Aplica una transformación recursiva al personaje según su nivel de transformación."""
    if nivel_transformacion == 0:
        return personaje.nivel_poder
    else:
        personaje.nivel_poder *= multiplicador
        return transformar(personaje, multiplicador, nivel_transformacion - 1)

#Implementacion de Arbol de Busqueda

#Clasifica a los personajes de acuerdo a su nivel de poder. El personaje con el mayor nivel de poder estará en el nodo más a la derecha del árbol.  El personaje con el menor nivel de poder estará en el nodo más a la izquierda del árbol.

class NodoBST:
    def __init__(self, personaje):
        self.personaje = personaje  # El personaje en este nodo
        self.izquierdo = None  # Hijo izquierdo (personajes con menor poder)
        self.derecho = None    # Hijo derecho (personajes con mayor poder)

class ArbolPersonajes:
    def __init__(self):
        self.raiz = None  # El árbol comienza vacío

    def insertar(self, personaje):
        """Inserta un personaje en el árbol de acuerdo a su nivel de poder."""
        if self.raiz is None:
            self.raiz = NodoBST(personaje)
        else:
            self._insertar_nodo(self.raiz, personaje)

    def _insertar_nodo(self, nodo, personaje):
        """Método recursivo para insertar un nodo en el árbol."""
        if personaje.nivel_poder < nodo.personaje.nivel_poder:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoBST(personaje)
            else:
                self._insertar_nodo(nodo.izquierdo, personaje)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoBST(personaje)
            else:
                self._insertar_nodo(nodo.derecho, personaje)

    def buscar_personaje_mas_fuerte(self):
        """Devuelve el personaje con el mayor nivel de poder (más a la derecha)."""
        if self.raiz is None:
            return None
        return self._buscar_mas_fuerte(self.raiz)

    def _buscar_mas_fuerte(self, nodo):
        """Recorre el árbol hasta encontrar el personaje más fuerte."""
        while nodo.derecho:  # El personaje más fuerte está más a la derecha
            nodo = nodo.derecho
        return nodo.personaje

    def buscar_personaje_mas_debil(self):
        """Devuelve el personaje con el menor nivel de poder (más a la izquierda)."""
        if self.raiz is None:
            return None
        return self._buscar_mas_debil(self.raiz)

    def _buscar_mas_debil(self, nodo):
        """Recorre el árbol hasta encontrar el personaje más débil."""
        while nodo.izquierdo:  # El personaje más débil está más a la izquierda
            nodo = nodo.izquierdo
        return nodo.personaje

    def en_orden(self):
        """Muestra los personajes en orden (de menor a mayor nivel de poder)."""
        self._en_orden_recursivo(self.raiz)

    def _en_orden_recursivo(self, nodo):
        """Recorrido en orden para imprimir los personajes."""
        if nodo:
            self._en_orden_recursivo(nodo.izquierdo)
            print(f"{nodo.personaje.nombre}: {nodo.personaje.nivel_poder}")
            self._en_orden_recursivo(nodo.derecho)

#Arboles generales
#Este modelo organiza habilidades de manera eficiente, permite jerarquías claras y soporta la expansión futura, ideal para un juego donde las habilidades progresan y evolucionan.
#Los jugadores pueden desbloquear habilidades según cumplan requisitos previos.
#Es fácil añadir nuevas técnicas al árbol.
#Facilita la integración con un sistema de juego basado en niveles o puntos de habilidad.

class NodoHabilidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subhabilidades = []

    def agregar_subhabilidad(self, subhabilidad):
        self.subhabilidades.append(subhabilidad)

    def mostrar_arbol_de_habilidades(self, nivel=0):
        print(" " * nivel * 2 + f"- {self.nombre}")
        for sub in self.subhabilidades:
            sub.mostrar_arbol_de_habilidades(nivel + 1)

# Creación del árbol de habilidades
kamehameha = NodoHabilidad("Kamehameha")
potenciado = NodoHabilidad("Kamehameha potenciado")
potenciado.agregar_subhabilidad(NodoHabilidad("Kamehameha x10"))
potenciado.agregar_subhabilidad(NodoHabilidad("Kamehameha dual"))

instantaneo = NodoHabilidad("Kamehameha instantáneo")
instantaneo.agregar_subhabilidad(NodoHabilidad("Kamehameha instantáneo x10"))

electrico = NodoHabilidad("Kamehameha eléctrico")
electrico.agregar_subhabilidad(NodoHabilidad("Kamehameha eléctrico avanzado"))

# Construcción del árbol
kamehameha.agregar_subhabilidad(potenciado)
kamehameha.agregar_subhabilidad(instantaneo)
kamehameha.agregar_subhabilidad(electrico)

# Visualización del árbol
kamehameha.mostrar_arbol_de_habilidades()

#Cola de prioridad
#Heap Binaria= Utilizamos un heap binario maximo, el cual prioriza a los personajes con niveles de poder más altos.
#Esta estructura garantiza que los personajes más poderosos enfrenten primero a otros combatientes, optimizando la organización del torneo y mejorando la experiencia del juego.

class TorneoColaDePrioridades:
    def __init__(self):
        # Usaremos una lista para almacenar el heap
        # En Python, heapq implementa un min-heap por defecto, así que usaremos valores negativos para simular un max-heap.
        self.cola = []

    def agregar_personaje(self, nombre, nivel_poder):
        # Insertamos el personaje con nivel de poder negativo para simular max-heap
        heapq.heappush(self.cola, (-nivel_poder, nombre))

    def siguiente_combate(self):
        # Extraemos el personaje con mayor nivel de poder
        if self.cola:
            nivel_poder, nombre = heapq.heappop(self.cola)
            return nombre, -nivel_poder
        else:
            return None, None

    def mostrar_cola(self):
        # Mostrar la cola en orden de prioridad
        personajes = [(-nivel_poder, nombre) for nivel_poder, nombre in self.cola]
        return sorted(personajes, reverse=True)  # Ordenamos por prioridad

class NodoPlaneta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}  # Diccionario para almacenar planetas conectados y su distancia

    def agregar_vecino(self, planeta, distancia):
        self.vecinos[planeta] = distancia  # Agregar conexión con otro planeta

class GrafoUniverso:
    def __init__(self):
        self.planetas = {}  # Diccionario para almacenar todos los nodos del grafo

    def agregar_planeta(self, nombre):
        """Agrega un nuevo planeta al grafo."""
        if nombre not in self.planetas:
            self.planetas[nombre] = NodoPlaneta(nombre)

    def agregar_ruta(self, origen, destino, distancia):
        """Crea una conexión entre dos planetas con una distancia específica."""
        if origen in self.planetas and destino in self.planetas:
            self.planetas[origen].agregar_vecino(self.planetas[destino], distancia)
            self.planetas[destino].agregar_vecino(self.planetas[origen], distancia)  # Grafo no dirigido

    def mostrar_rutas(self):
        """Muestra las conexiones y distancias entre planetas."""
        for planeta in self.planetas.values():
            print(f"Planeta {planeta.nombre} está conectado con:")
            for vecino, distancia in planeta.vecinos.items():
                print(f"  - {vecino.nombre} a una distancia de {distancia} unidades.")

    def buscar_ruta_mas_corta(self, origen, destino):
        """Implementa el algoritmo de Dijkstra para encontrar la ruta más corta entre dos planetas."""
        import heapq

        if origen not in self.planetas or destino not in self.planetas:
            print("Uno o ambos planetas no existen.")
            return None

        # Inicialización de distancias y cola de prioridad
        distancias = {planeta: float('inf') for planeta in self.planetas}
        distancias[origen] = 0
        cola = [(0, origen)]  # (distancia acumulada, nodo actual)
        padres = {origen: None}

        while cola:
            distancia_actual, planeta_actual = heapq.heappop(cola)

            if planeta_actual == destino:
                break

            for vecino, distancia in self.planetas[planeta_actual].vecinos.items():
                distancia_total = distancia_actual + distancia
                if distancia_total < distancias[vecino.nombre]:
                    distancias[vecino.nombre] = distancia_total
                    padres[vecino.nombre] = planeta_actual
                    heapq.heappush(cola, (distancia_total, vecino.nombre))

        # Reconstrucción del camino más corto
        camino = []
        actual = destino
        while actual:
            camino.insert(0, actual)
            actual = padres.get(actual)

        print(f"La ruta más corta de {origen} a {destino} es:")
        print(" -> ".join(camino))
        print(f"Con una distancia total de {distancias[destino]} unidades.")



class GrafoUniverso:
    def __init__(self):
        self.planetas = {}  # Diccionario para almacenar todos los nodos del grafo

    def agregar_planeta(self, nombre):
        """Agrega un nuevo planeta al grafo."""
        if nombre not in self.planetas:
            self.planetas[nombre] = NodoPlaneta(nombre)

    def agregar_ruta(self, origen, destino, distancia):
        """Crea una conexión entre dos planetas con una distancia específica."""
        if origen in self.planetas and destino in self.planetas:
            self.planetas[origen].agregar_vecino(self.planetas[destino], distancia)
            self.planetas[destino].agregar_vecino(self.planetas[origen], distancia)  # Grafo no dirigido

    def mostrar_rutas(self):
        """Muestra las conexiones y distancias entre planetas."""
        for planeta in self.planetas.values():
            print(f"Planeta {planeta.nombre} está conectado con:")
            for vecino, distancia in planeta.vecinos.items():
                print(f"  - {vecino.nombre} a una distancia de {distancia} unidades.")

    def dfs(self, origen, destino):
        """Búsqueda en profundidad (DFS) para encontrar un camino entre dos planetas."""
        visitados = set()
        camino = []

        def _dfs(actual):
            if actual == destino:
                return True
            visitados.add(actual)
            camino.append(actual)
            for vecino in self.planetas[actual].vecinos:
                if vecino.nombre not in visitados:
                    if _dfs(vecino.nombre):
                        return True
            camino.pop()  # Retroceder si no se encuentra un camino
            return False

        if origen not in self.planetas or destino not in self.planetas:
            print("Uno o ambos planetas no existen.")
            return None

        if _dfs(origen):
            print(f"Camino encontrado (DFS): {' -> '.join(camino + [destino])}")
        else:
            print("No se encontró un camino (DFS).")

    def bfs(self, origen, destino):
        """Búsqueda en amplitud (BFS) para encontrar un camino entre dos planetas."""
        visitados = set()
        cola = deque([(origen, [origen])])  # (planeta actual, camino recorrido)

        while cola:
            actual, camino = cola.popleft()
            if actual == destino:
                print(f"Camino encontrado (BFS): {' -> '.join(camino)}")
                return
            visitados.add(actual)
            for vecino in self.planetas[actual].vecinos:
                if vecino.nombre not in visitados:
                    cola.append((vecino.nombre, camino + [vecino.nombre]))

        print("No se encontró un camino (BFS).")

# Creación del universo
universo = GrafoUniverso()
universo.agregar_planeta("Tierra")
universo.agregar_planeta("Namek")
universo.agregar_planeta("Vegeta")
universo.agregar_planeta("Kaiosama")
universo.agregar_ruta("Tierra", "Namek", 100)
universo.agregar_ruta("Namek", "Vegeta", 50)
universo.agregar_ruta("Tierra", "Kaiosama", 200)
universo.agregar_ruta("Kaiosama", "Vegeta", 150)

# Mostrar las rutas
universo.mostrar_rutas()

# Búsqueda de un camino con DFS
universo.dfs("Tierra", "Vegeta")

# Búsqueda de un camino con BFS
universo.bfs("Tierra", "Vegeta")



class GrafoHabilidades:
    def __init__(self):
        self.habilidades = defaultdict(list)  # Diccionario para almacenar las relaciones entre habilidades

    def agregar_habilidad(self, habilidad, prerequisito=None):
        """
        Agrega una habilidad al grafo, con un prerequisito opcional.
        """
        if prerequisito:
            self.habilidades[prerequisito].append(habilidad)  # prerequisito -> habilidad
        if habilidad not in self.habilidades:
            self.habilidades[habilidad] = []  # Aseguramos que la habilidad esté en el grafo

    def orden_topologico(self):
        """
        Realiza el ordenamiento topológico de las habilidades.
        Devuelve una lista con el orden de entrenamiento.
        """
        # Calcular los grados de entrada de cada nodo
        grado_entrada = {habilidad: 0 for habilidad in self.habilidades}
        for prerequisitos in self.habilidades.values():
            for habilidad in prerequisitos:
                grado_entrada[habilidad] += 1

        # Cola para los nodos con grado de entrada 0
        cola = deque([habilidad for habilidad, grado in grado_entrada.items() if grado == 0])
        orden = []

        while cola:
            actual = cola.popleft()
            orden.append(actual)

            for vecino in self.habilidades[actual]:
                grado_entrada[vecino] -= 1
                if grado_entrada[vecino] == 0:
                    cola.append(vecino)

        # Verificar si el grafo tiene ciclos
        if len(orden) != len(self.habilidades):
            print("Error: Existe un ciclo en las habilidades, no es posible realizar el ordenamiento topológico.")
            return None

        return orden

# Ejemplo: Planificación de habilidades
grafo = GrafoHabilidades()

# Agregar habilidades y sus prerequisitos
grafo.agregar_habilidad("Kamehameha avanzado", "Kamehameha")
grafo.agregar_habilidad("Kamehameha dual", "Kamehameha avanzado")
grafo.agregar_habilidad("Kamehameha instantáneo", "Kamehameha")
grafo.agregar_habilidad("Kamehameha eléctrico", "Kamehameha avanzado")
grafo.agregar_habilidad("Kamehameha eléctrico avanzado", "Kamehameha eléctrico")

# Calcular el orden topológico
orden_entrenamiento = grafo.orden_topologico()

if orden_entrenamiento:
    print("Orden de entrenamiento de habilidades:")
    print(" -> ".join(orden_entrenamiento))

class NodoPlaneta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}  # Diccionario para almacenar planetas conectados y su distancia

    def agregar_vecino(self, planeta, distancia):
        self.vecinos[planeta] = distancia  # Agregar conexión con otro planeta

class GrafoUniverso:
    def __init__(self):
        self.planetas = {}  # Diccionario para almacenar todos los nodos del grafo

    def agregar_planeta(self, nombre):
        """Agrega un nuevo planeta al grafo."""
        if nombre not in self.planetas:
            self.planetas[nombre] = NodoPlaneta(nombre)

    def agregar_ruta(self, origen, destino, distancia):
        """Crea una conexión entre dos planetas con una distancia específica."""
        if origen in self.planetas and destino in self.planetas:
            self.planetas[origen].agregar_vecino(self.planetas[destino], distancia)
            self.planetas[destino].agregar_vecino(self.planetas[origen], distancia)  # Grafo no dirigido

    def buscar_ruta_mas_corta(self, origen, destino):
        """Implementa el algoritmo de Dijkstra para encontrar la ruta más corta entre dos planetas."""
        if origen not in self.planetas or destino not in self.planetas:
            print("Uno o ambos planetas no existen.")
            return None

        # Inicialización de distancias y cola de prioridad
        distancias = {planeta: float('inf') for planeta in self.planetas}
        distancias[origen] = 0
        cola = [(0, origen)]  # (distancia acumulada, nodo actual)
        padres = {origen: None}

        while cola:
            distancia_actual, planeta_actual = heapq.heappop(cola)

            if planeta_actual == destino:
                break

            for vecino, distancia in self.planetas[planeta_actual].vecinos.items():
                distancia_total = distancia_actual + distancia
                if distancia_total < distancias[vecino.nombre]:
                    distancias[vecino.nombre] = distancia_total
                    padres[vecino.nombre] = planeta_actual
                    heapq.heappush(cola, (distancia_total, vecino.nombre))

        # Reconstrucción del camino más corto
        camino = []
        actual = destino
        while actual:
            camino.insert(0, actual)
            actual = padres.get(actual)

        return camino, distancias[destino]

    def recolectar_esferas(self, origen, planetas_esferas):
        """
        Encuentra la mejor ruta para recolectar todas las Esferas del Dragón.
        Utiliza Dijkstra para calcular las distancias entre el origen y cada planeta con esferas.
        """
        visitados = set()
        ruta_completa = []
        distancia_total = 0

        actual = origen
        while planetas_esferas:
            distancias = []
            for planeta in planetas_esferas:
                camino, distancia = self.buscar_ruta_mas_corta(actual, planeta)
                distancias.append((distancia, camino))

            # Seleccionar la siguiente esfera más cercana
            distancias.sort(key=lambda x: x[0])  # Ordenar por distancia
            distancia_minima, mejor_camino = distancias[0]

            # Actualizar variables
            ruta_completa.extend(mejor_camino[:-1] if ruta_completa else mejor_camino)
            distancia_total += distancia_minima
            actual = mejor_camino[-1]
            planetas_esferas.remove(actual)

        print("Ruta para recolectar todas las Esferas del Dragón:")
        print(" -> ".join(ruta_completa))
        print(f"Distancia total recorrida: {distancia_total} unidades.")



