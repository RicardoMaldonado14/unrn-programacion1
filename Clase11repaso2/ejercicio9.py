# Ejercicio 9 - Validar patente simple
# Pedir al usuario una patente con el siguiente formato:
# Dos letra + tres números + dos letras (AB123CD)
# Validar que:
# ● No tenga espacios.
# ● Tenga 7 caracteres.
# ● Contenga solo letras y números.
# ● El formato
patente = input("ingrese una patente con el formato AB123CD: ")

if patente.count(" ") == False and len(patente) == 7 and patente.isalnum():
    if patente[:2].isalpha() and patente[2:5].isnumeric() and patente[-2:].isalpha():
        print("patente valida")
    else:
        print("formato no valido")
else:
    print("formato no valido")

