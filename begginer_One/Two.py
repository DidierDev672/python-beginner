import numpy as np

# Crear un arreglo (vector) de 5 elementos
vector = np.array([1, 2, 3, 4, 5])
print("Vector:", vector)

# Crear una matriz 2x3
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz:\n", matriz)

# Operaciones básicas
print("Suma del vector:", np.sum(vector))
print("Media del vector:", np.mean(vector))
print("Desviación estándar del vector:", np.std(vector))

# Operaciones con matrices
print("Transpuesta:\n", matriz.T)
print("Suma por filas:", np.sum(matriz, axis=1))
print("Suma por columnas:", np.sum(matriz, axis=0))

# Producto de matrices
matriz2 = np.array([[7, 8, 9], [10, 11, 12]])
print("Matriz 1:\n", matriz)
print("Matriz 2:\n", matriz2)
print("Suma de matrices:\n", matriz + matriz2)

# Multiplicación de matrices (producto punto)
matriz3 = np.array([[1, 2], [3, 4], [5, 6]])
print("Producto matriz x matriz3:\n", np.dot(matriz, matriz3))
