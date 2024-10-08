# El robot aspiradora tiene un comportamiento racional (primer punto)
import random

class AgenteRacional:
    def __init__(self, energia_inicial, posicion_inicial, tamano_tablero):
        self.energia = energia_inicial
        self.posicion = posicion_inicial
        self.tamano_tablero = tamano_tablero
        self.estado_interno = {}  # Si fuera necesario recordar posiciones visitadas

    def percibir(self, ambiente):
        # Detectar hojas en la posición actual
        hojas_aqui = ambiente[self.posicion[0]][self.posicion[1]] == 'hojas'
        return hojas_aqui

    def decidir_accion(self, ambiente):
        # Si hay hojas, aspirar. Si no, moverse.
        if self.percibir(ambiente):
            return 'aspirar'
        else:
            # Si el agente no tiene memoria, se moverá sin considerar si ya pasó por aquí.
            return 'moverse'

    def moverse(self, nueva_posicion):
        # Cambiar la posición del agente y reducir la energía
        self.posicion = nueva_posicion
        self.energia -= 1  # Penalización por movimiento

    def aspirar(self, ambiente):
        # Aspirar hojas en la posición actual
        if ambiente[self.posicion[0]][self.posicion[1]] == 'hojas':
            ambiente[self.posicion[0]][self.posicion[1]] = 'limpio'
        self.energia -= 1  # Penalización por aspirar

    def ejecutar(self, ambiente):
        while self.energia > 0:
            accion = self.decidir_accion(ambiente)
            if accion == 'aspirar':
                self.aspirar(ambiente)
            elif accion == 'moverse':
                # Aquí podrías implementar la lógica para moverse
                nueva_posicion = [self.posicion[0] + 1, self.posicion[1]]  # Ejemplo de movimiento
                if nueva_posicion[0] < self.tamano_tablero[0]:  # Verificar límites del tablero
                    self.moverse(nueva_posicion)
                else:
                    break  # Si no puede moverse, termina la ejecución

# Configuración del ambiente y simulación
def generar_ambiente(tamano_tablero):
    ambiente = []
    for i in range(tamano_tablero[0]):
        fila = []
        for j in range(tamano_tablero[1]):
            if random.random() < 0.5:  # 50% de probabilidad de hojas
                fila.append('hojas')
            else:
                fila.append('limpio')
        ambiente.append(fila)
    return ambiente

# Ejecutar la simulación
def ejecutar_simulacion():
    tamano_tablero = (5, 5)
    energia_inicial = 100
    agente = AgenteRacional(energia_inicial, [0, 0], tamano_tablero)
    ambiente = generar_ambiente(tamano_tablero)

    agente.ejecutar(ambiente)

    print("Ambiente limpio:", ambiente)
    print("Energía restante:", agente.energia)

# Llamar la función de simulación
ejecutar_simulacion()


# Código para el agente reflexivo sin estado interno (segundo punto)

import random

class AgenteReflexivo:
    def __init__(self, energia_inicial, posicion_inicial, tamano_tablero):
        self.energia = energia_inicial
        self.posicion = posicion_inicial
        self.tamano_tablero = tamano_tablero
        self.direccion = 'NORTE'  # Inicialmente puede estar apuntando al norte

    def percibir(self, ambiente):
        hojas_aqui = ambiente[self.posicion[0]][self.posicion[1]] == 'hojas'
        return hojas_aqui

    def decidir_accion(self, ambiente):
        if self.percibir(ambiente):
            return 'aspirar'
        else:
            return 'avanzar'

    def avanzar(self):
        # Simulación de avance (dependiendo de la dirección actual)
        if self.direccion == 'NORTE' and self.posicion[0] > 0:
            self.posicion[0] -= 1
        elif self.direccion == 'SUR' and self.posicion[0] < self.tamano_tablero[0] - 1:
            self.posicion[0] += 1
        elif self.direccion == 'ESTE' and self.posicion[1] < self.tamano_tablero[1] - 1:
            self.posicion[1] += 1
        elif self.direccion == 'OESTE' and self.posicion[1] > 0:
            self.posicion[1] -= 1
        self.energia -= 1

    def girar(self, angulo):
        direcciones = ['NORTE', 'ESTE', 'SUR', 'OESTE']
        index_actual = direcciones.index(self.direccion)
        giros = angulo // 90
        nueva_direccion = direcciones[(index_actual + giros) % 4]
        self.direccion = nueva_direccion
        self.energia -= 1

    def aspirar(self, ambiente):
        if ambiente[self.posicion[0]][self.posicion[1]] == 'hojas':
            ambiente[self.posicion[0]][self.posicion[1]] = 'limpio'
        self.energia -= 1

def generar_ambiente(tamano_tablero):
    ambiente = []
    for i in range(tamano_tablero[0]):
        fila = []
        for j in range(tamano_tablero[1]):
            if random.random() < 0.5:
                fila.append('hojas')
            else:
                fila.append('limpio')
        ambiente.append(fila)
    return ambiente

def ejecutar_simulacion():
    tamano_tablero = (5, 5)
    energia_inicial = 100
    agente = AgenteReflexivo(energia_inicial, [0, 0], tamano_tablero)
    ambiente = generar_ambiente(tamano_tablero)

    while agente.energia > 0:
        accion = agente.decidir_accion(ambiente)
        if accion == 'aspirar':
            agente.aspirar(ambiente)
        elif accion == 'avanzar':
            agente.avanzar()

    print("Ambiente limpio:", ambiente)
    print("Energía restante:", agente.energia)

ejecutar_simulacion()


## Código para el agente que recuerde las celdas visitadas (tercer punto)

import random

class AgenteRacional:
    def __init__(self, energia_inicial, posicion_inicial, tamano_tablero):
        self.energia = energia_inicial
        self.posicion = posicion_inicial
        self.tamano_tablero = tamano_tablero
        self.estado_interno = {}  # Si fuera necesario recordar posiciones visitadas

    def percibir(self, ambiente):
        hojas_aqui = ambiente[self.posicion[0]][self.posicion[1]] == 'hojas'
        return hojas_aqui

    def decidir_accion(self, ambiente):
        if self.percibir(ambiente):
            return 'aspirar'
        else:
            return 'moverse'

    def moverse(self, nueva_posicion):
        self.posicion = nueva_posicion
        self.energia -= 1

    def aspirar(self, ambiente):
        if ambiente[self.posicion[0]][self.posicion[1]] == 'hojas':
            ambiente[self.posicion[0]][self.posicion[1]] = 'limpio'
        self.energia -= 1

    def ejecutar(self, ambiente, max_pasos=1000):
        pasos = 0
        while self.energia > 0 and pasos < max_pasos:
            accion = self.decidir_accion(ambiente)
            if accion == 'aspirar':
                self.aspirar(ambiente)
            elif accion == 'moverse':
                nueva_posicion = [self.posicion[0] + 1, self.posicion[1]]
                if nueva_posicion[0] < self.tamano_tablero[0]:
                    self.moverse(nueva_posicion)
                else:
                    break
            pasos += 1

class AgenteConEstado(AgenteRacional):
    def __init__(self, energia_inicial, posicion_inicial, tamano_tablero):
        super().__init__(energia_inicial, posicion_inicial, tamano_tablero)
        self.visitadas = set()

    def decidir_accion(self, ambiente):
        if self.percibir(ambiente):
            return 'aspirar'
        else:
            posibles_movimientos = [
                [self.posicion[0] + 1, self.posicion[1]],
                [self.posicion[0] - 1, self.posicion[1]],
                [self.posicion[0], self.posicion[1] + 1],
                [self.posicion[0], self.posicion[1] - 1]
            ]
            for movimiento in posibles_movimientos:
                if (0 <= movimiento[0] < self.tamano_tablero[0] and
                    0 <= movimiento[1] < self.tamano_tablero[1] and
                    tuple(movimiento) not in self.visitadas):
                    return 'moverse', movimiento
            return 'moverse', self.posicion  # Si no hay movimientos válidos, quedarse

    def moverse(self, nueva_posicion):
        self.visitadas.add(tuple(self.posicion))
        super().moverse(nueva_posicion)

def generar_ambiente(tamano_tablero):
    ambiente = []
    for i in range(tamano_tablero[0]):
        fila = []
        for j in range(tamano_tablero[1]):
            if random.random() < 0.5:
                fila.append('hojas')
            else:
                fila.append('limpio')
        ambiente.append(fila)
    return ambiente

def ejecutar_simulacion(agente_clase, tamano_tablero, energia_inicial, num_simulaciones):
    energia_consumida_total = 0
    hojas_recogidas_total = 0

    for _ in range(num_simulaciones):
        agente = agente_clase(energia_inicial, [0, 0], tamano_tablero)
        ambiente = generar_ambiente(tamano_tablero)
        hojas_iniciales = sum(fila.count('hojas') for fila in ambiente)

        agente.ejecutar(ambiente)

        hojas_finales = sum(fila.count('hojas') for fila in ambiente)
        hojas_recogidas = hojas_iniciales - hojas_finales
        energia_consumida = energia_inicial - agente.energia

        energia_consumida_total += energia_consumida
        hojas_recogidas_total += hojas_recogidas

    promedio_energia_consumida = energia_consumida_total / num_simulaciones
    promedio_hojas_recogidas = hojas_recogidas_total / num_simulaciones

    return promedio_energia_consumida, promedio_hojas_recogidas

# Configuración del ambiente y simulación
tamano_tablero = (5, 5)
energia_inicial = 100
num_simulaciones = 50

# Ejecutar simulación para AgenteConEstado
promedio_energia_consumida, promedio_hojas_recogidas = ejecutar_simulacion(AgenteConEstado, tamano_tablero, energia_inicial, num_simulaciones)

print("Promedio de energía consumida:", promedio_energia_consumida)
print("Promedio de hojas recogidas:", promedio_hojas_recogidas)