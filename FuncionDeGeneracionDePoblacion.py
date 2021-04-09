import random

def poblacion(dimension , cantidad_de_individuos):
    poblacion = []
    pos = []
    for i in range(0, dimension):
        pos.append(i)
    while len(poblacion) < cantidad_de_individuos:
        individuo = []
        for j in range(0, dimension):
            valor = random.choice(pos)
            pos.remove(valor)
            #print(pos)
            individuo.append(valor)
        for k in range(0, dimension):
            pos.append(k)
        poblacion.append(individuo)
    return poblacion