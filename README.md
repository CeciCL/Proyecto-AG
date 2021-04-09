# Proyecto-AG

**Proyecto de algoritmos genéticos**

**¿Qué es un algoritmo genético?** 
Sabemos que un algoritmo es una serie de pasos que describen el proceso de búsqueda de una solución a un problema concreto, entonces un algoritmo genético(AG) es serie de pasos que usan mecanismos que simulan los de la evolución de las especies de la biología para formular dichos pasos, los cuales describen el proceso de búsqueda de una solución a un problema concreto.  
El siguiente diagram muestra el funcionamiento a grandes rasgos de un algoritmo genetico:
![Diagrama](https://drive.google.com/drive/folders/1Jk0eIBTZQjcaGuaqAviHzl02ZT4LZr4Y)

Ahora veamos en que consiste cada una de las técnicas que se usaron en este programa. 

**Función de Aptitud:**
La función de aptitud o función fitness consiste en que cada individuo de la población debe ser evaluado para cuantificar cómo de bueno es como solución al problema, a esta cuantificación se le llama (fitness). 
Para este programa en particular fue creado para evaluar un individuo, el cual es un tablero de ajedrez que está representado mediante un vector de permutaciones y devolver el número de ataques que tiene dicho individuo. 

**Función de creación de la población:**
La función de creación de la población es una función la cual toma dos valores, uno para la dimensión del tablero de ajedrez y otra para la cantidad de tableros que van a formar la población y devuelve una lista con la cantidad de tableros indicadas, cada uno de ellos con la dimensión que se eligió, cabe mencionar que la representación de cada uno de los tableros es mediante un vector de permutaciones.  

**Función de selección de padres:(Torneo determinista)**
La selección de padres por torneo fue propuesta por Wetzel y fue estudiada en la tesis doctoral de Brindle en 1981,la idea de este método de selección de padres con base en comparaciones directas de los individuos, hay dos versiones determinística y probabilística, en ambas versiones se deben escoger de manera aleatoria “t” individuos, en la versión determinista, será siempre seleccionado el individuo con la mejor aptitud. 

**Función de cruza:(Cíclica)** 
La función de cruza cíclica trabaja dividiendo los elementos en ciclos. Un ciclo es un subconjunto de elementos que tiene la propiedad de que cada elemento siempre ocurre emparejado con otro elemento del mismo ciclo, cuando los dos padres están alineados. Habiendo dividido la permutación en ciclos, la descendencia se crea seleccionando ciclos alternos de cada padre. El 
El procedimiento para construir ciclos es el siguiente: 
1. Comience con la primera posición no utilizada y el primer alelo de PI. 
2. Mira el alelo en la misma posición en P2 
3. Vaya a la posición con el mismo alelo en PI 
4. Agrega este alelo al ciclo. 
5. Repita los pasos 2 a 4 hasta llegar al primer alelo de PI 

**Función de mutación:(Mezcla)** 
En la función de mutación de tipo mezcla toda la cadena o algún subconjunto de valores son elegidos al azar dentro de ella, tienen sus posiciones mezcladas. 

**Función de reemplazo:(Generacional)**
La función de reemplazo generacional consiste en que todos los padres mueran y los hijos quedan como la población para la siguiente generación. 
