
# TODO: Suma de muchos números
# ? Define una función suma_multiple(*args) que sume una cantidad variable de números.

def suma_multiple(*args):
    """ Suma todos los números que se le pasen como argumentos """
    total = 0
    for arg in args:
        total += arg
    return total


print(f"Suma: ", suma_multiple(1, 3.14, 14.444))
