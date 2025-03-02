import numpy as np

def encontrar_mejor_camino(tablero):
    fila, col = 0, 0
    camino = [(fila, col)]
    while fila < len(tablero) - 1 or col < len(tablero[0]) - 1:
        if fila < len(tablero) - 1 and col < len(tablero[0]) - 1:
            if tablero[fila + 1][col] > tablero[fila][col + 1]:
                fila += 1
            else:
                col += 1
        elif fila < len(tablero) - 1:
            fila += 1
        else:
            col += 1
        camino.append((fila, col))
    return camino

# Simulación
tablero = np.random.randint(1, 10, (5, 5))
print("Tablero de utilidad:")
print(tablero)
camino_optimo = encontrar_mejor_camino(tablero)
print(f"Mejor camino encontrado: {camino_optimo}")