import random

def mutacion(poblacion):
    poblacion_de_mutados = []
    for j in range(0, len(poblacion)):
        hijo_mutado = mutacion_1(poblacion[j])
        poblacion_de_mutados.append(hijo_mutado)
    return poblacion_de_mutados

def mutacion_1(vector):
    posicion_1 = random.randrange(0, 8)
    posicion_2 = random.randrange(0, 8)
    vectornuevo = []
    vector_a = []
    if posicion_1 < posicion_2:
        for i in range(0, posicion_1):
            vectornuevo.append(vector[i])
        for i in range(posicion_1, posicion_2 + 1):
            vector_a.append(vector[i])
        elementos = posicion_2 - posicion_1
        vector_b = random.sample(vector_a, elementos+1)
        for i in range(0, elementos+1):
            vectornuevo.append(vector_b[i])
        for i in range(posicion_2+1, 8):
            vectornuevo.append(vector[i])
    elif posicion_2 < posicion_1:
        for i in range(0, posicion_2):
            vectornuevo.append(vector[i])
        for i in range(posicion_2, posicion_1 + 1):
            vector_a.append(vector[i])
        elementos = posicion_1 - posicion_2
        vector_b = random.sample(vector_a, elementos+1)
        for i in range(0, elementos+1):
            vectornuevo.append(vector_b[i])
        for i in range(posicion_1+1, 8):
            vectornuevo.append(vector[i])
    else:
        vectornuevo = vector
    return vectornuevo
