
# TODO: Promedio lista
# ? Escriba una función promedio(lista) que reciba una lista de números y devuelva el promedio.

def primedio(list):
    total = sum(list)
    promedio = total / len(list)
    print(f"List numbers: ", list)
    print(f"The average is: ", {promedio})
    return


listNumbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
primedio(listNumbers)
