from FuncionDeGeneracionDePoblacion import poblacion as poblacion
from FuncionDeAptitud import fitness as fitness
import random

def SeleccionDePadres(dim, cant):
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
"""
#seleccionador de padres
def SeleccionDePadres(a, b):
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