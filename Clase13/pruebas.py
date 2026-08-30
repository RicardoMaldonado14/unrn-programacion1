tablero = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    # Logica para imprimir tablero (FILITA POR FILITA)

imprimir_tablero(tablero)