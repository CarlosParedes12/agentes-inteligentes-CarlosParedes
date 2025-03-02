def es_seguro(tablero, fila, col, k):
    """
    Verifica si es seguro colocar una reina en la posición (fila, col).
    Se asegura de que no haya conflictos en la columna ni en las diagonales.
    """
    for i in range(fila):
        if tablero[i] == col or \
           tablero[i] - i == col - fila or \
           tablero[i] + i == col + fila:
            return False
    return True

def resolver_k_reinas(tablero, fila, k, soluciones):
    """
    Usa backtracking para colocar las k reinas en el tablero.
    """
    if fila == k:
        soluciones.append(tablero[:])  # Se almacena una solución válida
        return

    for col in range(k):
        if es_seguro(tablero, fila, col, k):
            tablero[fila] = col  # Coloca la reina en la columna válida
            resolver_k_reinas(tablero, fila + 1, k, soluciones)

def imprimir_soluciones(soluciones, k):
    """
    Muestra las soluciones en formato de tablero.
    """
    for index, sol in enumerate(soluciones):
        print(f"\nSolución {index + 1}:")
        for i in range(k):
            fila = ["."] * k
            fila[sol[i]] = "Q"
            print(" ".join(fila))
        print("-" * (2 * k - 1))

# Resolver el problema para k = 3
k = 10
soluciones = []
resolver_k_reinas([-1] * k, 0, k, soluciones)
imprimir_soluciones(soluciones, k)
