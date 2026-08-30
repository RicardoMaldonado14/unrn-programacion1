# Pedir al usuario un codigo de materia con este formato:
# PROG-101
# El programa tiene que validar que:
# tenga un solo guion -;
# la parte de la izquierda tenga solo letras;
# la parte de la derecha tenga solo numeros.
# Si el codigo es valido, mostrarlo normalizado en mayusculas (metodo upper).
# Ejemplo:
# Codigo valido: PROG-101
# Si no es valido, mostrar un mensaje de error claro.
codigo = input("ingreese un codigo de materia con el formato PROG-101: ")
if codigo.count("-") == 1:
    codigoelem = codigo.split("-")
    if codigoelem[0].isalpha() and codigoelem[1].isnumeric():
        codigoelem[0]  = codigoelem[0].upper()
        codigo = "-".join(codigoelem)
        print(f"Codigo valido: {codigo}")
    else:
        print("formato no valido")
else:
    print("formato no valido")