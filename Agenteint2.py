import random

# Dimensiones de la cuadrícula
GRID_SIZE = 5

# Representación de la cuadrícula
def mostrar_cuadricula(grid, agente_pos):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) == agente_pos:
                print("A", end=" ")  # A es el agente
            elif grid[i][j] == 1:
                print("O", end=" ")  # O es el objeto
            else:
                print(".", end=" ")  # . es un espacio vacío
        print()

# Función para mover al agente
def mover_agente(agente_pos, objeto_pos):
    x_agente, y_agente = agente_pos
    x_objeto, y_objeto = objeto_pos
    
    # Mover al agente en la dirección correcta
    if x_agente < x_objeto:
        x_agente += 1
    elif x_agente > x_objeto:
        x_agente -= 1
    if y_agente < y_objeto:
        y_agente += 1
    elif y_agente > y_objeto:
        y_agente -= 1
    
    return (x_agente, y_agente)

def buscar_objeto():
    # Inicializamos la cuadrícula (5x5) con todos los valores a 0 (vacío)
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # Colocamos el objeto en una posición aleatoria
    x_objeto = random.randint(0, GRID_SIZE - 1)
    y_objeto = random.randint(0, GRID_SIZE - 1)
    grid[x_objeto][y_objeto] = 1  # 1 representa el objeto
    
    # Posición inicial del agente
    agente_pos = (0, 0)  # El agente comienza en la esquina superior izquierda
    
    # Bucle para mover al agente hacia el objeto
    while agente_pos != (x_objeto, y_objeto):
        mostrar_cuadricula(grid, agente_pos)
        print("\nMoviendo al agente...\n")
        
        # Mover al agente
        agente_pos = mover_agente(agente_pos, (x_objeto, y_objeto))
    
    # Mostrar la cuadrícula cuando el agente haya encontrado el objeto
    mostrar_cuadricula(grid, agente_pos)
    print("\n¡El agente ha encontrado el objeto!\n")

# Ejecutar la búsqueda del objeto
buscar_objeto()