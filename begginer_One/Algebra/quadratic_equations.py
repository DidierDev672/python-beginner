
# todo: Ecuaciones cuadraticas
# ? Una ecuacion cuadratica tiene la forma:
#! ax + bx + c = 0

# * Se resuelve con la formula general:
# *  =2a−b±b2−4ac

import math


def solve_quadratic(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "It has no real solutions"

    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    return x1, x2


print(solve_quadratic(1, -3, 2))
