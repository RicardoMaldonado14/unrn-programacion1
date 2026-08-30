archivo = open("5productos.csv", "r")

diccionario = {}

for linea in archivo.readlines():
    nombre, precio, stock = linea.strip().split(";")
    diccionario[nombre] = {
        "precio": precio,
        "stock": stock
    }
archivo.close()

print(diccionario)