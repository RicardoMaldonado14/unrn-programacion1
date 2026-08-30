pedido = str(input("---ingrese su pedido: "))
productos = []

while pedido != "fin":
    productos.append(pedido)
    print("---Producto agregado a su lista--- ")
    pedido = str(input("---ingrese su pedido: "))
print("---Pedido finalizado---")

if len(productos)>0:
    print(f"La cantidad de productos ingresados es: {len(productos)}")
    print(f"El primer elemento de la lista es: {productos[0]}")
    print(f"El ultimo elemento de la lista es: {productos[-1]}")

else:
    print("No hay elementos en la lista")