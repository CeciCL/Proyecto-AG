def cruza(poblacion_de_padres):
    j = 0
    hijos = []
    while len(hijos) != len(poblacion_de_padres):
        while j < len(poblacion_de_padres):
            if 2*j+1 < len(poblacion_de_padres):
                pap1 = poblacion_de_padres[2*j]
                pap2 = poblacion_de_padres[2*j+1]
                hijo1, hijo2 = cruza_1([pap1, pap2])
                hijos.append(hijo1)
                hijos.append(hijo2)
            j += 1
    return hijos

def cruza_1(par_papas):
    papa_1=par_papas[0]
    papa_2=par_papas[1]
    #Esta parte es para el ciclo
    tocados_1 = []
    tocados_2 = []
    contador = 0
    posicion_usada = []
    for i in range(len(papa_1)):
        k = 0
        if len(posicion_usada) > 0:
            for j in posicion_usada:
                if i == j:
                    k = 1
            if k == 0:
                alelo_1 = papa_1[i]
                alelo_2 = papa_2[i]
                tocado_papa1 = []
                tocado_papa2 = []
                tocado_papa1.append(alelo_1)
                tocado_papa2.append(alelo_2)
                posicion_usada.append(i)
                contador += 1
                while alelo_2 != alelo_1:
                    for j in range(len(papa_1)):
                        alelo_x = papa_1[j]
                        if alelo_2 == alelo_x:
                            tocado_papa1.append(alelo_x)
                            alelo_2 = papa_2[j]
                            tocado_papa2.append(alelo_2)
                            posicion_usada.append(j)
                            contador += 1
                    if contador > len(papa_1):
                        break
                tocados_1.append(tocado_papa1)
                tocados_2.append(tocado_papa2)
            if contador == len(papa_1):
                break
        else:
            alelo_1 = papa_1[i]
            alelo_2 = papa_2[i]
            tocado_papa1 = []
            tocado_papa2 = []
            tocado_papa1.append(alelo_1)
            tocado_papa2.append(alelo_2)
            posicion_usada.append(i)
            contador += 1
            while alelo_2 != alelo_1:
                for j in range(len(papa_1)):
                    alelo_x = papa_1[j]
                    if alelo_2 == alelo_x:
                        tocado_papa1.append(alelo_x)
                        alelo_2 = papa_2[j]
                        tocado_papa2.append(alelo_2)
                        posicion_usada.append(j)
                        contador += 1
                if contador > len(papa_1):
                    break
            tocados_1.append(tocado_papa1)
            tocados_2.append(tocado_papa2)
            if contador == len(papa_1):
                break
    #Ahora vamos a hacer los hijos
    hijo_1 = []
    hijo_2 = []
    for i in range(len(papa_1)):
        hijo_1.append(0)
        hijo_2.append(0)

    #Esta parte es para hacer el hijo 1
    genes_para_hijo1 = []
    for i in range(len(tocados_1)):
        if 2 * i < len(tocados_1):
            gen_hijo1_1 = tocados_2[2 * i]
            genes_para_hijo1.append(gen_hijo1_1)
        if (2 * i + 1) < len(tocados_1):
            gen_hijo1_2 = tocados_1[2 * i + 1]
            genes_para_hijo1.append(gen_hijo1_2)
    hijo1 = []
    for i in range(len(genes_para_hijo1)):
        posicion_gen_para_hijo1 = genes_para_hijo1[i]
        for j in range(len(posicion_gen_para_hijo1)):
            hijo1.append(posicion_gen_para_hijo1[j])
    for i, j in zip(posicion_usada, hijo1):
        hijo_1[i] = j

    #Esta parte es para hacer el hijo 2
    genes_para_hijo2 = []
    for i in range(len(tocados_1)):
        if 2 * i < len(tocados_1):
            gen_hijo2_1 = tocados_1[2 * i]
            genes_para_hijo2.append(gen_hijo2_1)
        if (2 * i + 1) < len(tocados_1):
            gen_hijo2_2 = tocados_2[2 * i + 1]
            genes_para_hijo2.append(gen_hijo2_2)
    hijo2 = []
    for i in range(len(genes_para_hijo2)):
        posicion_gen_para_hijo2 = genes_para_hijo2[i]
        for j in range(len(posicion_gen_para_hijo2)):
            hijo2.append(posicion_gen_para_hijo2[j])
    for i, j in zip(posicion_usada, hijo2):
        hijo_2[i] = j
    return hijo_1, hijo_2