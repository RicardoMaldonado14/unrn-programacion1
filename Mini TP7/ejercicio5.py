# Ejercicio 5 - Codigo de materia
# Pedir al usuario un codigo de materia con este formato:
# PROG-101
# El programa tiene que validar que:
# tenga un solo guion -;
# la parte de la izquierda tenga solo letras;
# la parte de la derecha tenga solo numeros.
# Si el codigo es valido, mostrarlo normalizado en mayusculas (metodo upper).
# Ejemplo:
# Codigo valido: PROG-101
print("---Ingrese un codigo de materia con el formato: PROG-101")
codigo = input("ingrese el codigo de materia: ")
if codigo.count("-") == 1:
    partes = codigo.split("-")
    if partes[0].isalpha() and partes[1].isnumeric():
        materia = partes[0].upper().strip()
        codigo = partes[1].strip()
        print(f"Codigo valido: {materia}-{codigo}")
    else:
        print("ingrese el texto en el formato valido")

else:
    print("ingrese el texto en el formato valido")

