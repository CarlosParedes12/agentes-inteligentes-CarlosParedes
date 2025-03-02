class AgenteConMemoria:
    def __init__(self):
        self.historial = []

    def mover(self, posicion):
        if posicion not in self.historial:
            print(f"Explorando nueva posición: {posicion}")
            self.historial.append(posicion)
        else:
            print(f"Evitando posición repetida: {posicion}")

# Simulación
agente = AgenteConMemoria()
agente.mover((0,0))
agente.mover((0,1))
agente.mover((0,0))
agente.mover((1,1))
agente.mover((0,0))
agente.mover((0,1))