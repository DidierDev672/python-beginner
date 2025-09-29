
# TODO: Contar vocales
# * Crea una funcion contar_vocales(texto) que cuente cuantas vocoles tiene una cadena de texto.

from typing import Counter


listVowels = ['a', 'e', 'i', 'o', 'u']


def vowelCounter(name):
    wordToList = list(name)
    foundVowels = []
    count = 0
    print(wordToList)
    for i in range(len(wordToList)):
        for j in range(len(listVowels)):
            if (wordToList[i] == listVowels[j]):

                count += 1
                foundVowels.append(listVowels[j])
                print("Letter: ", wordToList[i], " Vowel: ", listVowels[j])

    countRepeated = Counter(wordToList)
    repeated = {elemento: frecuencia for elemento,
                frecuencia in countRepeated.items() if frecuencia > 1}
    sumR = sum(repeated.values())
    countVowel = 0
    print(f"List of vowels found: ", foundVowels)
    if (sumR > 0):
        countVowel = (count - sumR + 1)
        print(f"Number of vowels: ", countVowel)
        return
    print(f"Number of vowels: ", (count))
    print(f"----------------------------------------------------------------------------------------------")


vowelCounter("Didier")
vowelCounter("Natalia")
vowelCounter("Nelva")
