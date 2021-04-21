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
#Esto es para hacer las generaciones
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

    #Fitness del mejor individuo por generacion
    fitness_poblacion = []
    for k1 in range(len(poblacion_inicial)):
        fitness_indivicual = fitness(poblacion_inicial[k1])
        fitness_poblacion.append(fitness_indivicual)
    fitness_min = min(fitness_poblacion)
    mejor_individuo_por_generacion.append(fitness_min)

    #Fitness del peores individuo por generación
    fitness_mas_grande = max(fitness_poblacion)
    peor_individuo_por_generacion.append(fitness_mas_grande)

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
plt.title('Gráfica de convergencia')
plt.show()
