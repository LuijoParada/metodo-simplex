import numpy as np;

# z = 10x1 + 20x2
#restricciones:
#4x1 + 2x2 <= 20
#8x1 + 8x2 <= 20
#      2x2 <= 10

def simplex(c, a, b):

# c: valor de coeficientes de la función objetivo
# a: matriz de coeficientes de las restricciones
# b: valor del lado derecho de las restriccione

    numRest = len(b) #numero de variables
    numVar = len(c)  #numero de restricciones

    tabla = np.zeros((numRest + 1, numVar + numRest + 1)) #se crea la tabla para realizar el metodo simplex
    tabla[:-1, :numVar] = a 
    tabla[:-1, -1] = b 
    tabla[-1, :numVar] = c 

    for i in range(numRest): tabla[i, numVar + i] = 1 #se agregan las variables de holgura

    while any(tabla[-1, :-1] < 0):
        colPivote = np.argmin(tabla[-1, :-1]) #columna pivote

        filasPositivas = tabla[-1, :colPivote]
        if any(filasPositivas < 0):
            raise ValueError("no existe solucion optima")

        pivote = np.zeros(numRest) # se calculan los cocientes entre el lado derecho de las restricciones y los coeficientes de la columna pivote
        for i in range(numRest):
            if filasPositivas[i]:
                pivote[i] = tabla[i, -1] / tabla[i, colPivote]
            else:
                pivote[i] = np.inf #la fila con menor valor se selecciona como fila pivote
        filaPivote = np.argmin(pivote) 

        #se divide toda la fila pivote por el valor del elemento pivote.
        tabla[filaPivote] /= tabla[filaPivote, colPivote]
        for i in range(tabla.shape[0]):
            if i != filaPivote:
                tabla[i] -= tabla[filaPivote] * tabla[i, colPivote]

    x =  np.zeros(numVar) #por ultimo se almacena la solucion optima para X y Z
    for i in range(numVar):
        col = tabla[:, i]
        fila = -1
        for j in range(numRest):
            if col[j] == 1:
                fila = j
                break
        if fila != -1:
            x[i] = tabla[fila, -1]

    z = -tabla[-1,-1]
    return x, z


#valores del ejercicio:
c = [10, 20]

a = [[4, 2], [8, 8], [0, 2]]

b = [20, 20, 10]

Xoptima, Zoptima = simplex(c,a,b)

print(f'solucion óptima: {Xoptima}')
print(f'valor óptimo: {Zoptima}')