"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from itertools import groupby

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open("files/input/data.csv", "r") as file:
        sequence = [(line.split()[0], int(line.split()[1])) for line in file]
    
    sequence.sort(key=lambda x: x[0])
    result = []
    for key, group in groupby(sequence, key=lambda x: x[0]):
        min_n = max_n = next(group)[1]
        for _, value in group:
            max_n = max(max_n, value)
            min_n = min(min_n, value)
        
        result.append((key, max_n, min_n))
    
    return result
