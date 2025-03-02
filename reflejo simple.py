import random

def agente_reflejo(entorno, posicion):
    direccion = ['izquierda', 'derecha', 'arriba', 'abajo']
    while True:
        if entorno[posicion] == 'obstáculo':
            nueva_direccion = random.choice(direccion)
            print(f"Obstáculo detectado, cambiando dirección a {nueva_direccion}")
        else:
            print(f"Moviéndose en la dirección {random.choice(direccion)}")
        break

# Simulación
entorno = {0: 'libre', 1: 'obstáculo', 2: 'libre',3:'libre', 4:'obstáculo', 5:'obstáculo'}
agente_reflejo(entorno, 5)