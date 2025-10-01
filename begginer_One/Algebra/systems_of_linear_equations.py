
# todo Sistemas de ecuaciones lineales
# ? Un sistema de 2 ecuaciones con 2 incognitas:
# ** 2x + y = 5
# ** x - y = 1

import numpy as np

A = np.array([[2, 1], [1, -1]])  # ? Coeficientes
B = np.array([5, 1])  # ? Resultados

solution = np.linalg.solve(A, B)
print("x =", solution[0], "y =", solution[1])  # * x = 2.0, y = 1.0
