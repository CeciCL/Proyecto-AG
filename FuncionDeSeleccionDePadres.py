from FuncionDeAptitud import fitness
import random

def SeleccionDePadres(poblacion):
    """
    Ordenar la población de menor a mayor fiteness con la función sorted
    """
    poblacion_en_orden = sorted(poblacion, key=fitness)
    """
    Calcular la probabilidad de ser selccionado y probabilidad acumulada
    """
    prob_de_seleccion = []
    prob_acumulada = []
    for i in range(1, len(poblacion) + 1):
        p_pos = (len(poblacion) - i + 1) / ((len(poblacion) * (len(poblacion) + 1)) / 2)
        prob_de_seleccion.append(p_pos)
        p_acum = sum(prob_de_seleccion)
        prob_acumulada.append(p_acum)
    """
    Generar dos números random y selelcionar los padres segun la probabilidad acumulada
    """
    poblacion_de_padres = []
    while len(poblacion_de_padres) < int(len(poblacion) / 2):
        par_de_padres = []
        r1 = random.random()
        r2 = random.random()
        k1 = 0
        k2 = 0
        while prob_acumulada[k1] < r1:
            k1 += 1
        while prob_acumulada[k2] < r2:
            k2 += 1
        padre_1 = poblacion_en_orden[k1]
        padre_2 = poblacion_en_orden[k2]
        par_de_padres.append(padre_1)
        par_de_padres.append(padre_2)
        poblacion_de_padres.append(par_de_padres)

    return poblacion_de_padres