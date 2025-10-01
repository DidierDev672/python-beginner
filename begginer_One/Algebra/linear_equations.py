
# todo: Ecuaciones lineales
# ? Una ecuacion lineal tiene la forma:
#! ax + b = 0
# * Ejemplo: 2x + 3 = 0 => x = - 3/2

def solve_linear_equation(a, b):
    if a == 0:
        return "There is no single solution"
    return -b / a


print(solve_linear_equation(2, 3))
