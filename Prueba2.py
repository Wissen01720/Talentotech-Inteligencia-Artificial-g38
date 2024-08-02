def dfs(grafo, inicio, fin):
    def dfs_util(nodo_actual, destino, camino, distancia):
        if nodo_actual == destino:
            nonlocal ruta_mas_corta, distancia_mas_corta
            if distancia < distancia_mas_corta:
                ruta_mas_corta = camino.copy()
                distancia_mas_corta = distancia
            return
        for vecino, peso in grafo[nodo_actual].items():
            if vecino not in camino:
                camino.append(vecino)
                dfs_util(vecino, destino, camino, distancia + peso)
                camino.pop()

    ruta_mas_corta = []
    distancia_mas_corta = float('inf')
    dfs_util(inicio, fin, [inicio], 0)
    return ruta_mas_corta, distancia_mas_corta

grafo = {
    'A': {'B': 5, 'C': 8, 'D': 9},
    'B': {'A': 5, 'E': 15, 'F': 7},
    'C': {'A': 8, 'G': 12, 'H': 10},
    'D': {'A': 9, 'I': 11, 'J': 6},
    'E': {'B': 15, 'K': 9, 'L': 13},
    'F': {'B': 7, 'M': 8, 'N': 6},
    'G': {'C': 12, 'O': 10, 'P': 5},
    'H': {'C': 10, 'Q': 11, 'R': 7},
    'I': {'D': 11, 'S': 14, 'T': 8},
    'J': {'D': 6, 'U': 9, 'V': 12},
    'K': {'E': 9},
    'L': {'E': 13},
    'M': {'F': 8},
    'N': {'F': 6},
    'O': {'G': 10},
    'P': {'G': 5},
    'Q': {'H': 11},
    'R': {'H': 7},
    'S': {'I': 14},
    'T': {'I': 8},
    'U': {'J': 9},
    'V': {'J': 12}
}

entrada = input("").strip().upper().split()
inicio, fin = entrada[0], entrada[1]

ruta, distancia = dfs(grafo, inicio, fin)
if ruta:
    print(" ".join(ruta))
else:
    print("None")