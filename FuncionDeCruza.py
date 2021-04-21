def cruza_1(padre_1, padre_2):
    papa_1 = padre_1[:]
    papa_2 = padre_2[:]
    papa_1_original = padre_1[:]
    papa_2_original = padre_2[:]
    """
    Esta parte es para hacer los conjuntos
    """
    conjuntos = []
    i=0
    elementos_tocados = []
    while i<8:
        if i in elementos_tocados:
            i+=1
        else:
            conjunto_i = []
            if papa_1[i] == papa_2[i]:
                conjunto_i.append(papa_1[i])
                elementos_tocados.append(i)
            else:
                conjunto_i.append(papa_2[i])
                while papa_1[i] != papa_2[i]:
                    posicion_1 = papa_1.index(papa_2[i])
                    papa_2[i] = papa_2[posicion_1]
                    conjunto_i.append(papa_2[i])
                    elementos_tocados.append(posicion_1)
            conjuntos.append(conjunto_i)
            i += 1
    """
    Esta parte es para hacer los hijos
    """
    hijo1 = [0]*8
    hijo2 = [0]*8
    for k1 in range(0,len(conjuntos)):
        if k1 % 2 == 0:
            for k2 in range(len(conjuntos[k1])):
                elementos1 = papa_1_original.index(conjuntos[k1][k2])
                elementos2 = papa_2_original.index(conjuntos[k1][k2])
                hijo1[elementos1] = conjuntos[k1][k2]
                hijo2[elementos2] = conjuntos[k1][k2]
        else:
            for k2 in range(0,len(conjuntos[k1])):
                elementos1 = papa_1_original.index(conjuntos[k1][k2])
                elementos2 = papa_2_original.index(conjuntos[k1][k2])
                hijo1[elementos2] = conjuntos[k1][k2]
                hijo2[elementos1] = conjuntos[k1][k2]
    return hijo1, hijo2

def cruza(poblacion_de_padres):
    h=int(len(poblacion_de_padres)/2)
    poblacion_de_hijos = []
    for d in range(len(poblacion_de_padres)):
        par_de_padres = poblacion_de_padres[d]
        pap1 = par_de_padres[0]
        pap2 = par_de_padres[1]
        hijo1, hijo2 = cruza_1(pap1, pap2)
        poblacion_de_hijos.append(hijo1)
        poblacion_de_hijos.append(hijo2)
    return poblacion_de_hijos