from scipy.optimize import linprog

# Definir los coeficientes de la función objetivo
c = [-1, 4]

# Definir las restricciones de desigualdad
A = [[-3, 1], [1, 2]]
b = [6, 4]

# Resolver el problema de optimización utilizando el método simplex
res = linprog(c, A_ub=A, b_ub=b, method='simplex')

# Imprimir el resultado
print(f'Valor óptimo: {res.fun}')
print(f'Solución óptima: {res.x}')
