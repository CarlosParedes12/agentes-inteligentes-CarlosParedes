import random

def buscar_objetivo():
    tablero = [["-" for _ in range(5)] for _ in range(5)]
    objetivo = (random.randint(0, 4), random.randint(0, 4))
    agente = (0, 0)
    print(f"Objetivo en: {objetivo}")
    while agente != objetivo:
        if agente[0] < objetivo[0]:
            agente = (agente[0] + 1, agente[1])
        elif agente[0] > objetivo[0]:
            agente = (agente[0] - 1, agente[1])
        elif agente[1] < objetivo[1]:
            agente = (agente[0], agente[1] + 1)
        elif agente[1] > objetivo[1]:
            agente = (agente[0], agente[1] - 1)
        print(f"Agente moviéndose a {agente}")
    print("¡Objetivo alcanzado!")

buscar_objetivo()