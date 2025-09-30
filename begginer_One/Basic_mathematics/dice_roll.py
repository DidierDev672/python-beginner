
# todo Simula el lanzamiento de un dado 10 veces y guarda los resultados en una lista.
import numpy as np


def roll_of_the_dice():
    results = np.random.randint(1, 7, size=10)  # ? Lanzamientos datos
    return results.tolist()  # ? Lo pasamos a lista


print(roll_of_the_dice())
