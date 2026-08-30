lista = []
producto = input("ingrese un producto: ")
cantidad = 0

while producto != "fin":
    cantidad +=1
    if producto not in lista:
        lista.append(producto)

    producto = input("ingrese un producto: ")

print(f"la cantidad de productos ingresados: {cantidad}")
print(f"su lista de productos es: {lista}")