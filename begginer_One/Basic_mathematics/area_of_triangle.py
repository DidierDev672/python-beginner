
# todo Calcula el area de un triangulo usando la formula:
# * A = base * altura / 2

def area_of_triangle(base, height):
    if base < 0:
        print(f"Numbers less than zero and negative numbers are not allowed")
        return
    if height < 0:
        print(f"Numbers less than zero and negative numbers are not allowed")
        return

    area_of_triangle = base * height / 2
    return area_of_triangle


print(f"The area of the triangle is: ", area_of_triangle(10, 6))
print(f"The area of the triangle is: ", area_of_triangle(3, 4))
