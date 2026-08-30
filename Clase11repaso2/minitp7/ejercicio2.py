# Ejercicio 4 - Edad valida
# Pedir una edad por teclado. Antes de usarla como numero, revisar que el dato tenga sentido.
# El programa tiene que aceptar edades numericas entre 0 y 120. 
# Si la persona escribe espacios de mas, el programa deberia poder limpiarlos antes de validar.
# Si el dato sirve, mostrar algo como:
# Edad registrada: 25
# Si no sirve, mostrar un mensaje de error claro. No alcanza con que el programa se rompa.
edad = input("ingrese una edad numerica: ")

if edad.strip().isnumeric():
    edadvalida = int(edad)
    if 0<=edadvalida<=120:
        print(f"Edad registrada: {edadvalida}")
    else:
        print("edad fuera de rango")
else:
    print("formato de edad no valido")