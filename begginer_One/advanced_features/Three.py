
# TODO: Tabla de multiplicar
# ? Define una función tabla_multiplicar(n) que muestre la tabla de multiplicar de un número n.

def multiplication_table(n):
    for i in range(13):
        multiplier = n * i
        print(f"Table: ", n, "*", i, ":", multiplier)
    return


multiplication_table(1)
print("*************************************--------******************----------------*******")
multiplication_table(5)
