
# TODO: Generar lista de cuadrados
# ? Crea una función cuadrados(n) que reciba un número n y devuelva una lista con los cuadrados de los números de 1 a n.

def cuadrado(n):
    cuadrados = [i**2 for i in range(1, n)]
    print(cuadrados)
    return


cuadrado(12)
