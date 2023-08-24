from scipy.optimize import linprog

# Definir los coeficientes de la función objetivo
c = [10, 20]

# Definir las restricciones de desigualdad
A = [[4, 2], [8, 8], [0, 2]]
b = [20, 20, 10]

# Resolver el problema de optimización utilizando el método simplex
res = linprog(c, A_ub=A, b_ub=b, method='simplex')

# Imprimir el resultado
print(f'Valor óptimo: {res.fun}')
print(f'Solución óptima: {res.x}')
