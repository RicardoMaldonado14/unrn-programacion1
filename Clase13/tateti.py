VACIO = 0
JUGADOR_1 = 1
JUGADOR_2 = 2

tablero = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

turno_jugador = JUGADOR_1

def obtener_posicion():
    # Logica para solicitar datos al usuario (del 1 al 3)
    # Consejo: restar 1 aquí adentro para trabajar con índices 0, 1, 2
    print("---Ingrese la posicion de su pieza [Fila, Columna]---")
    print("---Valores permitidos del 1 al 3---")
    fila = int(input("ingrese la fila: ")) - 1
    columna = int(input("ingrese la columna")) - 1

    return fila, columna

def validar_posicion(tablero, fila, columna):
    # Logica para validar rango (0 a 2) y posición libre
    if (0 >= fila < 3) == False:
        return False
    if (0 >= columna < 3) == False:
        return False
    if tablero[fila][columna] != VACIO:
        return False
    return True

def asignar_posicion(tablero, fila, columna, jugador):
    # Logica para asignar un jugador a una posición
    pass

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("---------")
    # Logica para imprimir tablero (FILITA POR FILITA)
    pass

def buscar_ganador(tablero):
    # Devuelve True si un jugador completó una línea, False si no
    pass

def cambiar_turno(turno_jugador):
    # Logica para cambiar de turno
    return turno_jugador
    
imprimir_tablero(tablero) # Mostrar tablero vacío al principio

while True:
    fila, columna = obtener_posicion()

    if not validar_posicion(tablero, fila, columna):
        print("Posición inválida o ya ocupada. Vuelva a elegir.")
        continue
    
    asignar_posicion(tablero, fila, columna, turno_jugador)
    imprimir_tablero(tablero)

    if buscar_ganador(tablero):
        print(f"¡Ganó el JUGADOR {turno_jugador}!")
        break
        
    turno_jugador = cambiar_turno(turno_jugador)