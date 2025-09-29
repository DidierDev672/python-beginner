
# TODO: Palíndrom
# ? Crea una función es_palindromo(palabra) que determine si una palabra se lee igual al derecho y al revés.

def es_palindromo(world):
    standardizedText = "".join(world.lower().split())
    return standardizedText == standardizedText[::-1]


world = "Reconocer"
print(f"'{world}' es palíndrom: ", es_palindromo(world))
