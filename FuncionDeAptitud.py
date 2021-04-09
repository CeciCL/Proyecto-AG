def fitness(vector):
    contador = 0
    dimension = len(vector)
    for i in range(dimension):
        k_1 = vector[i]
        for j in range(i+1,dimension):
            k_2 = vector[j]
            pen = (k_2-k_1)/(j-i)
            if pen == 1 or pen == (-1):
                contador += 1
    return contador