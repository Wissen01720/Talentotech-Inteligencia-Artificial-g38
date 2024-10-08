## En un juego de laberinto, un jugador desea encontrar el camino más corto desde la casilla de inicio hasta la casilla de salida.
# El laberinto está representado por una cuadrícula de celdas, donde algunas celdas pueden estar bloqueadas (paredes) y otras son transitables. Cada celda tiene coordenadas (x, y). El jugador puede moverse en cuatro direcciones: arriba, abajo, izquierda y derecha. El costo de moverse de una celda a otra es 1. El jugador tiene información sobre la posición de la casilla de inicio y la casilla de salida. El objetivo es encontrar el camino más corto desde la casilla de inicio hasta la casilla de salida, evitando las celdas bloqueadas. Este problema se puede resolver utilizando el algoritmo A* con una heurística adecuada, como la distancia de Manhattan o la distancia euclidiana entre las celdas. El algoritmo A* encontrará el camino óptimo que minimiza la distancia total recorrida desde la casilla de inicio hasta la casilla de salida, evitando las celdas bloqueadas en el camino.

import heapq

# Definir la heurística (distancia de Manhattan)
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Algoritmo A*
def a_star(laberinto, inicio, meta):
    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Inicializar la cola de prioridad
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    
    # Diccionarios para rastrear el costo y el camino
    costo_hasta_ahora = {inicio: 0}
    camino = {inicio: None}
    
    while cola_prioridad:
        _, actual = heapq.heappop(cola_prioridad)
        
        if actual == meta:
            break
        
        for movimiento in movimientos:
            vecino = (actual[0] + movimiento[0], actual[1] + movimiento[1])
            if 0 <= vecino[0] < len(laberinto) and 0 <= vecino[1] < len(laberinto[0]) and laberinto[vecino[0]][vecino[1]] != 1:
                nuevo_costo = costo_hasta_ahora[actual] + 1
                if vecino not in costo_hasta_ahora or nuevo_costo < costo_hasta_ahora[vecino]:
                    costo_hasta_ahora[vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(meta, vecino)
                    heapq.heappush(cola_prioridad, (prioridad, vecino))
                    camino[vecino] = actual
    
    actual = meta
    ruta = []
    while actual is not None:
        ruta.append(actual)
        actual = camino[actual]
    ruta.reverse()
    return ruta

# Ejemplo de forma de uso
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
meta = (4, 4)

ruta = a_star(laberinto, inicio, meta)
print("Ruta encontrada:", ruta)