import heapq

def encontrar_mejor_ruta(recompensas, inicio, meta):
    """Usa Dijkstra modificado para encontrar la ruta con mayor utilidad."""
    filas, columnas = len(recompensas), len(recompensas[0])
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
    cola_prioridad = [(-recompensas[inicio[0]][inicio[1]], inicio, [])]  # Usamos negativo para simular max heap
    visitados = set()
    
    while cola_prioridad:
        utilidad, (fila, col), camino = heapq.heappop(cola_prioridad)
        nuevo_camino = camino + [(fila, col)]
        
        if (fila, col) == meta:
            return nuevo_camino, -utilidad  # Se devuelve utilidad positiva
        
        if (fila, col) in visitados:
            continue
        visitados.add((fila, col))
        
        for df, dc in movimientos:
            nueva_fila, nueva_col = fila + df, col + dc
            if 0 <= nueva_fila < filas and 0 <= nueva_col < columnas and (nueva_fila, nueva_col) not in visitados:
                nueva_utilidad = utilidad - recompensas[nueva_fila][nueva_col]  # Suma de utilidad
                heapq.heappush(cola_prioridad, (nueva_utilidad, (nueva_fila, nueva_col), nuevo_camino))
    
    return None, 0  # No hay camino

# Definir el entorno con valores de recompensa
recompensas = [
    [3, 1, 5, 1, 4],
    [2, 8, 1, 3, 7],
    [4, 2, 6, 2, 9],
    [1, 7, 4, 5, 2],
    [3, 2, 8, 6, 10]
]

inicio = (0, 0)
meta = (4, 4)

ruta_optima, utilidad_total = encontrar_mejor_ruta(recompensas, inicio, meta)

if ruta_optima:
    print("Ruta óptima seleccionada:")
    for paso in ruta_optima:
        print(f"{paso}")
    print(f"Utilidad total: {utilidad_total}")
else:
    print("No se encontró una ruta óptima.")