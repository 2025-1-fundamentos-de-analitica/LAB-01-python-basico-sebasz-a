"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from itertools import groupby

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    with open("files/input/data.csv", "r") as file:
        sequence = [(line.split()[3], int(line.split()[1])) for line in file]

    sequence = [(letters, pair[1]) for pair in sequence for letters in pair[0].split(",")]

    sequence.sort(key=lambda x: x[0])
    result = {key:sum(value for _, value in group) for key, group in groupby(sequence, key=lambda x: x[0])}
    
    return result
