import random

def poblacion(dim , cant):
    pob = []
    pos = []
    for i in range(0,dim):
        pos.append(i)
    while len(pob)!=cant:
        indiv=[]
        for j in range(0, dim):
            valor=random.choice(pos)
            pos.remove(valor)
            indiv.append(valor)
        for i in range(0, dim):
            pos.append(i)
        pob.append(indiv)

    return pob