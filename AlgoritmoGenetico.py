from FuncionDeGeneracionDePoblacion import poblacion
from FuncionDeAptitud import fitness
from FuncionDeSeleccionDePadres import SeleccionDePadres
from FuncionDeCruza import cruza
from FuncionDeMutacion import mutacion
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('Hola,bienvenido a mi algoritmo génetico,aquí vamos a ver el problema de 0 colisiones entre reinas en un tablero de ajedrez.\n'
      'Lo primero que vamos a hacer es crear nuestra población,para eso voy a necesitar tú ayuda,pues vas a elegir el número de individuos que va a tener la población,dicho número tiene que ser par.')
cant=int(input('Por favor ingresa el número de individuos que deseas que tenga la población.'))
if cant%2 == 0:
    poblacion_inicial = poblacion(8,cant)
    mejor_individuo_por_generacion = []
    peor_individuo_por_generacion = []
    individuo_promedio_por_generacion = []
    desviacion_estandar = []
    generaciones = []

    hijos = []
    poblacion_de_padres = []
    poblacion_de_mutados = []
    generaciones = []
    #Estp es para hacer las generaciones
    for i in range(50):
        #Selección de padres
        poblacion_de_padres = SeleccionDePadres(poblacion_inicial)
        #Cruza
        poblacion_de_hijos = cruza(poblacion_de_padres)
        #Mutación
        poblacion_de_mutados = mutacion(poblacion_de_hijos)
        #Reemplazo
        poblacion_inicial = poblacion_de_mutados
        generaciones.append(poblacion_inicial)

        #Número de mejores individuos por generacion
        fitness_poblacion = []
        for k1 in range(len(poblacion_inicial)):
            fitness_indivicual = fitness(poblacion_inicial[k1])
            fitness_poblacion.append(fitness_indivicual)
        fitness_mas_pequeño = min(fitness_poblacion)
        numero_de_individuos_con_mejor_fitness = 0
        for j in range(len(poblacion_inicial)):
            if fitness_mas_pequeño == fitness_poblacion[j]:
                numero_de_individuos_con_mejor_fitness += 1
        mejor_individuo_por_generacion.append(numero_de_individuos_con_mejor_fitness)

        #Número de peores individuos por generación
        fitness_mas_grande = max(fitness_poblacion)
        numero_de_individuos_con_peor_fitness = 0
        for j in range(len(poblacion_inicial)):
            if fitness_mas_grande == fitness_poblacion[j]:
                numero_de_individuos_con_peor_fitness += 1
        peor_individuo_por_generacion.append(numero_de_individuos_con_peor_fitness)

        #Número de individuos promedio
        promedio = sum(fitness_poblacion)/len(fitness_poblacion)
        individuo_promedio_por_generacion.append(promedio)

        #Desviacion estandar
        suma = 0
        for i in range(len(fitness_poblacion)):
            desv = (fitness_poblacion[i] - promedio) ** 2
            suma += desv
        varianza = suma / (len(fitness_poblacion))
        desviacion_estandar.append(np.sqrt(varianza))
else:
    cant =print('El número que ingresaste no es valido,por favor intenta de nuevo.\n')

#Esto es para hacer la tabla
indices = range(50)
lis_indices = list(indices)
tabla = {'Mejor': mejor_individuo_por_generacion,
       'Peor' : peor_individuo_por_generacion,
        'Prom' : individuo_promedio_por_generacion,
       'DE' : desviacion_estandar}
tabla_1 = pd.DataFrame(tabla)
tabla_1.index = lis_indices
print(tabla_1)

#Esto es para hacer la grafica
X = np.array(lis_indices)
Y = np.array(individuo_promedio_por_generacion)
x = np.linspace(0, 49, 50)
y = mejor_individuo_por_generacion
plt.plot(x, y)
plt.show()
