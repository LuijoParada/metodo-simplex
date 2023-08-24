## Metodo simplex

Este script de Python implementa el método simplex para resolver problemas de programación lineal. El método simplex es un algoritmo iterativo que busca la solución óptima de una función objetivo sujeta a restricciones lineales.

## Como funciona?

Para utilizar el método simplex, se debe llamar a la función simplex y pasarle tres argumentos:
- c: una lista con los coeficientes de la función objetivo.
- a: una matriz con los coeficientes de las restricciones.
- b: una lista con los valores del lado derecho de las restricciones.

La función retorna dos valores:
- Xoptima: una lista con los valores óptimos de las variables.
- Zoptima: el valor óptimo de la función objetivo.

En la parte donde toca definir la funcion simplex donde se realizan los pasos necesarios para resolver el problema se procede de la siguiente manera 

Primero, se definen los parámetros de entrada de la función, que son los coeficientes de la función objetivo (c), la matriz de coeficientes de las restricciones (a) y el vector de lados derechos de las restricciones (b).

Luego, se calcula el número de variables y restricciones, y se crea una tabla vacía con el tamaño adecuado para almacenar los valores necesarios para el algoritmo simplex. 

Se copian los valores de la matriz a y el vector b en la tabla, y se agregan las variables de holgura para convertir las restricciones en igualdades. 

A continuación, se inicia un bucle que se ejecuta mientras haya algún coeficiente negativo en la fila correspondiente a la función objetivo en la tabla. 

Dentro del bucle, se busca la columna pivote, que es la columna con el coeficiente más negativo en la fila de la función objetivo. Si alguna fila correspondiente a una variable tiene un coeficiente positivo en esa columna, se calculan los cocientes entre el lado derecho de las restricciones y los coeficientes de esa columna, y se selecciona la fila con el menor cociente como fila pivote. 

Se divide toda la fila pivote por el valor del elemento pivote para hacer que el valor del elemento pivote sea igual a 1. Luego, se actualizan las demás filas de la tabla para hacer que los coeficientes correspondientes a la variable pivote sean cero.

Finalmente, se almacena la solución óptima para las variables x y el valor de la función objetivo z, y se devuelve como una tupla.
