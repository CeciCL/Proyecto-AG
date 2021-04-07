import random

def poblacion(dim , cant):
    pob = []
    pos = []
    for i in range(0,dim):
        pos.append(i)
    while len(pob)<cant:
        indiv=[]
        for j in range(0, dim):
            valor=random.choice(pos)
            pos.remove(valor)
            #print(pos)
            indiv.append(valor)
        for k in range(0, dim):
            pos.append(k)
        pob.append(indiv)

    return pob