from FuncionDeAptitud import fitness
import random

def SeleccionDePadres(poblacion_1):
    poblacion_de_papas = []
    while len(poblacion_de_papas) < len(poblacion_1):
        i = random.randrange(0, len(poblacion_1))
        mejor_papa = []
        j = -1
        while j < i:
            papa_1 = poblacion_1[random.randrange(0, len(poblacion_1))]
            papa_2 = poblacion_1[random.randrange(0, len(poblacion_1))]
            if fitness(papa_2) > fitness(papa_1):
                mejor_papa = papa_1
            else:
                mejor_papa = papa_2
            j += 1
        poblacion_de_papas.append(mejor_papa)
    return poblacion_de_papas