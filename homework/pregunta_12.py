"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from itertools import groupby

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    with open("files/input/data.csv", "r") as file:
        sequence = [(line.split()[0], line.split()[4]) for line in file]
    
    sequence = [(line[0], int(pair.split(":")[1])) for line in sequence for pair in line[1].split(",")]

    sequence.sort(key=lambda x: x[0])
    result = {key:sum(value for _, value in group) for key, group in groupby(sequence, key=lambda x: x[0])}

    return result
print(pregunta_12())