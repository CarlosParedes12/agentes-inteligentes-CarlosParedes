import random
import time

class AgentePatrullaje:
    def __init__(self, ruta):
        self.ruta = ruta  # Lista de posiciones por donde patrulla
        self.posicion_actual = 0  # Índice de la ruta actual
        self.direccion = 1  # 1 para avanzar, -1 para retroceder
    
    def detectar_obstaculo(self):
        """Simula la detección de un obstáculo con una probabilidad del 20%."""
        return random.random() < 0.2
    
    def cambiar_direccion(self):
        """Cambia la dirección de movimiento de manera aleatoria."""
        self.direccion = random.choice([-1, 1])
        print("¡Obstáculo detectado! Cambiando dirección...")
    
    def mover(self):
        """Mueve el agente a la siguiente posición en la ruta."""
        if self.detectar_obstaculo():
            self.cambiar_direccion()
        
        self.posicion_actual += self.direccion
        
        # Asegurar que el agente permanezca dentro de la ruta
        if self.posicion_actual >= len(self.ruta):
            self.posicion_actual = len(self.ruta) - 1
            self.direccion = -1
        elif self.posicion_actual < 0:
            self.posicion_actual = 0
            self.direccion = 1
        
        print(f"Agente patrullando... Posición: {self.ruta[self.posicion_actual]}")
    
    def patrullar(self, pasos=10):
        """Ejecuta la patrulla durante un número de pasos."""
        for _ in range(pasos):
            self.mover()
            time.sleep(1)  # Simulación de tiempo entre movimientos

# Definir una ruta de patrullaje
ruta_patrulla = ["Punto A", "Punto B", "Punto C", "Punto D", "Punto E"]

# Crear y ejecutar el agente de patrullaje
agente = AgentePatrullaje(ruta_patrulla)
agente.patrullar(15)
