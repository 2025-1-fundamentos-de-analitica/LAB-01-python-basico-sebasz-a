"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from itertools import groupby

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    with open("files/input/data.csv", "r") as file:
        sequence = [line.split()[4].strip() for line in file]
    
    sequence = [pair for line in sequence for pair in line.split(",")]
    sequence = [(pair.split(":")[0], int(pair.split(":")[1])) for pair in sequence]
    
    sequence.sort(key=lambda x: x[0])
    result = []
    for key, group in groupby(sequence, key=lambda x: x[0]):
        max_n = min_n = next(group)[1]
        for _, value in group:
            max_n = max(max_n, value)
            min_n = min(min_n, value)
    
        result.append((key, min_n, max_n))

    return result
