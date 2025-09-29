
# TODO: Número mayor
# ? Haz una función mayor(a, b, c) que recibe tres números y devuleve el mayor.

def mayor(a, b, c):
    numbers = [a, b, c]
    if (a <= 0) or (b <= 0) or (c <= 0):
        return "The numbers entered must be greater than zero"

    major_number = max(numbers)
    print(f"Numbers: ", numbers)
    print(f"Largest number is: ", major_number)
    print(f"***************************************************************************************************************")
    return


mayor(7, 3, 5)
mayor(8, 12, 16)
