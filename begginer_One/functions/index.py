def saludar():
    print("!Hola! Bienvenido a Python")

saludar()

#? Funcion con parametros
def saludar_persona(name):
    print(f"Hola, {name}")


saludar_persona("Didier")
saludar_persona("Ana")

#? Funcion que devulve un valor
def sumar(a, b):
    return a + b;

resultado = sumar(5,7)
print("La suma es:", resultado)


#? Funcion con valores por defecto
def potencia(base, exponente=2):
    return base ** exponente

print("5 =", potencia(5)) #! Usa el exponente por defecto (2)
print("2 =", potencia(2,3)) #! Cambia el valor por defecto.


#? Funcion con multiples argumentos (*args y *kwargs)
def mostrar_numeros(*args):
    for numero in args:
        print(numero)

mostrar_numeros(1, 2, 3, 4, 5)

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(name="Didier", edad=28, ciudad="Bogota")

#? Funcion dentro de otra funcion (Funcion anidada)
def operacion(a, b):
    def multiplicar(x, y):
        return x * y
    return multiplicar(a, b) + a + b

print("Resultado de la operacion:", operacion(3,4))

#? Funcion lambda (Funcion anonima)
doblar = lambda x: x * 2
print("El doble de 7 es:", doblar(7))

suma = lambda a, b: a + b
print("Suma rapida: ", suma(3,5))