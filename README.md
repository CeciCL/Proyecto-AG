# Proyecto-AG

**Proyecto de algoritmos genéticos**

**¿Qué es un algoritmo genético?** 
Sabemos que un algoritmo es una serie de pasos que describen el proceso de búsqueda de una solución a un problema concreto, entonces un algoritmo genético(AG) es serie de pasos que usan mecanismos que simulan los de la evolución de las especies de la biología para formular dichos pasos, los cuales describen el proceso de búsqueda de una solución a un problema concreto.  
El siguiente diagrama muestra de manera general el funiconamiento de esté algoritmo genético.

![Diagrama_AG](https://user-images.githubusercontent.com/79228097/114244929-08922f00-9955-11eb-9b76-05bad8e635f6.png)

Ahora veamos en que consiste cada una de las técnicas que se usaron en este programa.  

**Función de creación de la población:**
La función de creación de la población es una función la cual toma dos valores, uno para la dimensión del tablero de ajedrez y otra para la cantidad de tableros que van a formar la población y devuelve una lista con la cantidad de tableros indicadas, cada uno de ellos con la dimensión que se eligió, cabe mencionar que la representación de cada uno de los tableros es mediante un vector de permutaciones.

**Función de Aptitud:**
La función de aptitud o función fitness consiste en que cada individuo de la población debe ser evaluado para cuantificar que tan bueno es como solución al problema, a esta cuantificación se le llama (fitness). 
Para este programa en particular fue creado para evaluar un individuo, el cual es un tablero de ajedrez que está representado mediante un vector de permutaciones y devolver el número de ataques que tiene dicho individuo.

**Función de selección de padres:(Selección  por ruleta(ponderación de rango))**
 El peocedimiento para llevar a cabo este ste método de selección de padres consiste en:
 1. Calcular el fitness de cada uno de los individuos
 2. Ordenarlos de manera ascendente
 3. Calcular la probabilidad de ser selecionado de cada uno de los individuos con la formula:
![Formula_SP_AG](https://user-images.githubusercontent.com/79228097/115813175-50cf3980-a3b8-11eb-9731-c73e5ac8f2fc.png)

 5. Calcular la probabilidad acumulada
 6. Generar un número aleatorio
 7. Verificar quien es el individuo que alcanza el número aleatorio
 8. Selecionar el cromosoma con mejor aptitud
 
**Función de cruza:(Cíclica)** 
La función de cruza cíclica trabaja dividiendo los elementos en ciclos. Un ciclo es un subconjunto de elementos que tiene la propiedad de que cada elemento siempre ocurre emparejado con otro elemento del mismo ciclo, cuando los dos padres están alineados. Habiendo dividido la permutación en ciclos, la descendencia se crea seleccionando ciclos alternos de cada padre. El procedimiento para construir ciclos es el siguiente: 
1. Comience con la primera posición no utilizada y el primer alelo del padre 1. 
2. Mira el alelo en la misma posición en padre 2.
3. Vaya a la posición con el mismo alelo en padre 1.
4. Agrega este alelo al ciclo. 
5. Repita los pasos 2 a 4 hasta llegar al primer alelo de padre 1. 

**Función de mutación:(Mezcla)** 
En la función de mutación de tipo mezcla toda la cadena o algún subconjunto de valores que son elegidos al azar dentro de ella, tienen sus posiciones mezcladas. 

**Función de reemplazo:(Generacional)**
La función de reemplazo generacional consiste en que todos los padres mueran y los hijos quedan como la población para la siguiente generación. 
