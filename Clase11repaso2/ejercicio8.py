# Ejercicio 8 - Lista de productos separada por coma
# Pedir al usuario que ingrese productos separados por coma.
# Validar que se ingresó más de dos productos, y que ninguno
# quedó vacío.
productos = input("ingrese productos separados por comas \n"
                  "por ej: prod, prod, prod: " )

if productos.count(",") >= 2:
    listaprod = productos.split(",")
    entradavalida = True

    for producto in listaprod:
        if producto.strip() == "":
            entradavalida = False
            break

    if entradavalida:
        print("lista de productos correctamente ingresada")
    else:
        print("ERROR hay un producto vacio")
else:
    print("la cantidad de productos no es la esperada")