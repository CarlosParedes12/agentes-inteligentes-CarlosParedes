from collections import deque
import time

class AgenteNavegacion:
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = laberinto
        self.inicio = inicio
        self.meta = meta
        self.movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
    
    def buscar_camino(self):
        """Usa BFS para encontrar el camino más corto hasta la meta."""
        fila, col = self.inicio
        cola = deque([(fila, col, [])])  # (fila, columna, camino hasta aquí)
        visitados = set()
        visitados.add((fila, col))
        
        while cola:
            fila, col, camino = cola.popleft()
            nuevo_camino = camino + [(fila, col)]
            
            if (fila, col) == self.meta:
                return nuevo_camino  # Se encontró el camino
            
            for df, dc in self.movimientos:
                nueva_fila, nueva_col = fila + df, col + dc
                if (0 <= nueva_fila < len(self.laberinto) and 0 <= nueva_col < len(self.laberinto[0])
                        and self.laberinto[nueva_fila][nueva_col] == 0  # Celda transitable
                        and (nueva_fila, nueva_col) not in visitados):
                    cola.append((nueva_fila, nueva_col, nuevo_camino))
                    visitados.add((nueva_fila, nueva_col))
        
        return None  # No hay camino
    
    def navegar(self):
        """Muestra el camino encontrado por el agente."""
        camino = self.buscar_camino()
        if camino:
            for paso in camino:
                print(f"Agente en: {paso}")
                time.sleep(1)
            print("¡Meta alcanzada!")
        else:
            print("No se encontró un camino hasta la meta.")

# Definir el laberinto (0: camino libre, 1: pared)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
meta = (4, 4)

agente = AgenteNavegacion(laberinto, inicio, meta)
agente.navegar()