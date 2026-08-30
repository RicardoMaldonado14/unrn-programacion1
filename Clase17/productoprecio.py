producto = input("ingrese un producto: ")

try:
    nombre, precio = producto.split(";")
except ValueError:
    print("producto y precio no validos, ingresar con")
    exit(1)

try:
    precio = float(precio)
    print(f"{nombre} cuesta {precio}")
except ValueError:
    print("se ingreso un precio invalido, ingrese valores numericos")