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
"""
    padres = []
    i=0
    while i<len(poblacion_1):
        papa_1 = poblacion_1[random.randrange(0, len(poblacion_1))]
        papa_2 = poblacion_1[random.randrange(0, len(poblacion_1))]
        mejor_papa = []
        if fitness(papa_2) > fitness(papa_1):
            mejor_papa = papa_1
        else:
            mejor_papa = papa_2
        padres.append(mejor_papa)
        i+=1
    return padres
#prueba_papas=poblacion(8,5)
    poblacion_de_papas = []
    while len(poblacion_de_papas)<len(poblacion_1):
        i = random.randrange(0,len(poblacion_1))
        mejor_papa = []
        j = -1
        while j<i:
            papa_1=poblacion_1[random.randrange(0,len(poblacion_1))]
            papa_2=poblacion_1[random.randrange(0,len(poblacion_1))]
            if fitness(papa_2) > fitness(papa_1):
                mejor_papa = papa_1
            else:
                mejor_papa = papa_2
            j += 1
        poblacion_de_papas.append(mejor_papa)
    return poblacion_de_papas


#SeleccionDePadres=poblacion(8,5)
"""
"""
padres=[]
poblacion_1 = poblacion(dim, cant)
for i in range(0,cant):
    papa_1= poblacion_1[random.randrange(0,cant)]
    papa_2= poblacion_1[random.randrange(0,cant)]
    mejor_papa = []
    if fitness(papa_2) > fitness(papa_1):
        mejor_papa = papa_1
    else:
        mejor_papa = papa_2
    padres.append(mejor_papa)
    return padres

#seleccionador de padres
    r1 = a
    r2 = b
    papa1 = []
    if fitness(b) > fitness(a):
        papa1 = r1
    else:
        papa1= r2
    return papa1

poblacion = vector_per(8, 50)
for i in range(0,50):
    papa_1= poblacion[random.randrange(0,50)]
    papa_2= poblacion[random.randrange(0,50)]

    print(i,SeleccionDePadres(papa_1 , papa_2),"\n")
"""