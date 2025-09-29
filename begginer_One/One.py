# print("!Hola mundo!");

# #? Tipos de datos
# numero_entero = 10;
# tipo = type(numero_entero);
# print("Tipo: ", tipo);

# #! Tipos de datos entero y Integer
# x = 10; #* =>  Integer
# y = 10.5 #* Float
# z = "Hello"; #* String

# integer = type(x)
# print("Integer: ", integer, " valor del dato: ", x);

# tipo_float = type(y)
# print("Float: ", tipo_float, " valor del tipo de datos float: ", y);

# tipo_string = type(z);
# print("String/Text: ", tipo_string, " valor del dato String/Text: ", z);

# year = 2025;
# yearBirthdate = 1997;
# age = (year - yearBirthdate);

# print("Tu edad es: ", age);

# #TODO: Tipos de datos flotantes
# price = 19.999;
# aument = 0.19;

# finalPrice = ( price * aument ) + price;
# print("Precio final: ", finalPrice);

# #TODO: Numeros complejos (complex)
# z = 2 + 3j;
# print("Complex: ", z);

# #! Tipos de datos String/Texto
# greeting = "Welcome to python!"
# print(greeting);

# #! Listas
# fruits = ["Apple", "Banana", "Cherry"];
# print(fruits);

# #! Tuplas (tupla).
# dimensions = (1920, 1080);
# print(dimensions);

# #! Dict => Diccionarios
# person = {"name": "Alice", "age": 30};
# print(person);

# #! Set (Conjuntos)
# unique_numbers = {1,2,3,4,5};
# print(unique_numbers);

# #TODO: Frozenset (Conjuntos congelados)
# immutables_set = frozenset([1,2,3]);
# print("Conjuntos congelados: ", immutables_set);

# #? Tipos de datos Boolean
# isActive = True;

# print("Valor de active: ", isActive);

# age = 28;

# if(28 >= 18):
#     print("Si. Es mayor de edad: ", age);

# if(28 < 18):
#     print("Es menor de edad: ", age);

# result = None;
# print("Resultado: ", result);

data = b"hello"; #? Immutable bytes object
mutable_data = bytearray(b"hello"); #? Mutable bytearray object.
view = memoryview(mutable_data); #? Memoryview of the bytearray.

print("View: ",view);