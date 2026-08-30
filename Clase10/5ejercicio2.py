archivo = open("5productos.csv","r")

productos = {}

for linea in archivo.readlines():
    nombre, precio, stock = linea.strip().split(";")
    productos[nombre] = {
        "precio": precio,
        "stock": stock
    }

for producto, datos in productos.items():
    # print(productos)
    # print(datos)
    print(f"{producto} - precio: {datos["precio"]} - stock: {datos["stock"]}")

archivo.close()