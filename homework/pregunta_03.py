"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from itertools import groupby

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    with open("files/input/data.csv", "r") as file:
        sequence = [(line.split()[0], int(line[2])) for line in file]
    
    sequence.sort(key=lambda x: x[0])
    result = [(key, sum(value for _, value in group)) for key, group in groupby(sequence, lambda x: x[0])]
    
    return result
