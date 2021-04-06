def fitness(vector):
    contador=0
    dim=len(vector)
    for i in range(dim):
        entr=vector[i]
        for j in range(i+1,dim):
            entr_2=vector[j]
            pen=(entr_2-entr)/(j-i)
            if pen==1 or pen==(-1):
                contador+=1
    return(contador)