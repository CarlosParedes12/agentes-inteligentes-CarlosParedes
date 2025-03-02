import random
import time

class AgenteExplorador:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.posicion = (0, 0)  # Empieza en la esquina superior izquierda
        self.visitados = set()
        self.direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
    
    def mover(self):
        """Mueve al agente a una celda no visitada si es posible."""
        movimientos_posibles = []
        
        for dx, dy in self.direcciones:
            nueva_pos = (self.posicion[0] + dx, self.posicion[1] + dy)
            if (0 <= nueva_pos[0] < self.filas and 0 <= nueva_pos[1] < self.columnas
                    and nueva_pos not in self.visitados):
                movimientos_posibles.append(nueva_pos)
        
        if movimientos_posibles:
            self.posicion = random.choice(movimientos_posibles)
            self.visitados.add(self.posicion)
        else:
            print("No hay movimientos disponibles, quedándose en la posición actual.")
        
        print(f"Explorador en posición: {self.posicion}")
    
    def explorar(self, pasos=20):
        """Explora el entorno durante un número de pasos."""
        self.visitados.add(self.posicion)
        for _ in range(pasos):
            self.mover()
            time.sleep(1)

# Crear y ejecutar el agente explorador en una cuadrícula de 5x5
agente = AgenteExplorador(5, 5)
agente.explorar(15)