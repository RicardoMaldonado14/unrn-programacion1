# Ejercicio 10 - Validar float
# Pedir al usuario un número flotante implementar un
# mecanismo para validar que el dato ingresado es
# correcto.

flotante = input("ingrese un numero flotante: ")

if flotante.count(".") == 1:
    elementos = flotante.split(".")
    if elementos[0].strip().isnumeric() and elementos[1].strip().isnumeric():
        flotante = float(".".join(elementos))
        print(f"el numero flotante es valido {flotante}")
    else:
        print("numero no valido")
else: 
    print("numero no valido")