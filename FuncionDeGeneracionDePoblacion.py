import random

def poblacion(dimension, cantidad_de_individuos):
    poblacion = []
    pos = []
    for i in range(0, dimension):
        pos.append(i)
    while len(poblacion) < cantidad_de_individuos:
        individuo = []
        for i in range(0, dimension):
            valor = random.choice(pos)
            pos.remove(valor)
            individuo.append(valor)
        for j in range(0, dimension):
            pos.append(j)
        poblacion.append(individuo)
    return poblacion