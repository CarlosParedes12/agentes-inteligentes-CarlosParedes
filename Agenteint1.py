import time
import random

class SemaforoInteligente:
    def __init__(self):
        self.estado = "Rojo"
        self.tiempo_espera = {"Verde": 5, "Amarillo": 2, "Rojo": 5}
    
    def detectar_vehiculos(self):
        """Simula la detección de vehículos (entre 0 y 10)."""
        return random.randint(0, 10)
    
    def ajustar_tiempo(self, vehiculos):
        """Ajusta el tiempo del semáforo en función del tráfico."""
        if vehiculos > 7:
            self.tiempo_espera["Verde"] = 8  # Más vehículos, más tiempo en verde
            self.tiempo_espera["Rojo"] = 6
        elif vehiculos < 3:
            self.tiempo_espera["Verde"] = 4  # Menos vehículos, menos tiempo en verde
            self.tiempo_espera["Rojo"] = 7
        else:
            self.tiempo_espera["Verde"] = 5  # Tráfico moderado
            self.tiempo_espera["Rojo"] = 5
    
    def cambiar_estado(self):
        """Cambia el estado del semáforo de manera cíclica."""
        if self.estado == "Rojo":
            self.estado = "Verde"
        elif self.estado == "Verde":
            self.estado = "Amarillo"
        else:
            self.estado = "Rojo"
    
    def iniciar(self, ciclos=5):
        """Simula el funcionamiento del semáforo por un número de ciclos."""
        for _ in range(ciclos):
            vehiculos = self.detectar_vehiculos()
            self.ajustar_tiempo(vehiculos)
            print(f"Estado: {self.estado} | Vehículos detectados: {vehiculos} | Duración: {self.tiempo_espera[self.estado]} seg")
            time.sleep(self.tiempo_espera[self.estado])
            self.cambiar_estado()

# Ejecutar la simulación
semaforo = SemaforoInteligente()
semaforo.iniciar(10)
