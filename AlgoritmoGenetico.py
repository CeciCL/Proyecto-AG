from FuncionDeGeneracionDePoblacion import poblacion
from FuncionDeAptitud import fitness
from FuncionDeSeleccionDePadres import SeleccionDePadres
from FuncionDeCruza import cruza
from FuncionDeMutacion import mutacion
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('Hola,bienvenido a mi algoritmo génetico,aquí vamos a ver el problema de 0 colisiones entre reinas en un tablero de ajedrez.\n'
      'Este algoritmo crea una población inicial de 100 elementos,a los cuales despues procede a realizar las funciones de aptitud,\n'
      'selección de padres,cruza,mutación y reemplazo,todo esto lo realiza para 50 generaciones, despues de que realiza todo este proceso\n'
      'te muestra una tabla con el mejor individuo(fitness),el peor individuo(fitness),el individuo promedio(fitness) y la desviación estandar,\n'
      'para cada una de las generaciones y tambien te muestra una gráfica de convergencia\n')

poblacion_inicial = poblacion(8, 100)
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

    #Fitness del mejor individuo por generación
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

    #Desviación estandar
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

#Esto es para hacer la gráfica
X = np.array(lis_indices)
Y = np.array(individuo_promedio_por_generacion)
x = np.linspace(0, 49, 50)
y = mejor_individuo_por_generacion
plt.plot(x, y)
plt.title('Gráfica de convergencia')
plt.show()
