
#TODO:  Que es el factorial?
#? El factorial de un numero entero positivo n se define como:
#! n! = n x (n - 1) X (n - 2) X ... X 1
def factorial(n):
    if n < 0:
        return "The factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1;
    return n * factorial(n - 1)

print("7! =", factorial(7))