# Pedir una edad por teclado. Antes de usarla como numero, revisar que el dato tenga sentido.
# El programa tiene que aceptar edades numericas entre 0 y 120. 
# Si la persona escribe espacios de mas, el programa deberia poder limpiarlos antes de validar.
# Si el dato sirve, mostrar algo como:
# Edad registrada: 25
edad = input("ingrese una edad: ").strip()
if edad.isnumeric():
    edadnum = int(edad)
    if 0<edadnum<120:
        print(f"edad registrada: {edadnum}")
    else:
        print("ingrese una edad dentro del rango")
else:
    print(f"ingrese una edad numerica")