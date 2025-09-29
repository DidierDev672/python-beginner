def calculate(a, b, operation):
    if operation == 'suma':
        return a + b
    if operation == 'resta':
        return a - b
    if operation == 'multiplicar':
        return a * b
    if operation == 'dividir':
        return a / b
    return


print(f"Calculate suma: ", calculate(2, 5, 'suma'))
print(f"Calculate resta: ", calculate(12, 55, 'resta'))
print(f"Calculate multiplicar: ", calculate(5, 5, 'multiplicar'))
print(f"Calculate division: ", calculate(14, 7, 'dividir'))
