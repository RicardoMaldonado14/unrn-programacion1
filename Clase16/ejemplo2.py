import json
with open("producto.json", "r") as archivo:
    datos = json.load(archivo)

print(datos)
print(type(datos))
print(datos["nombre"])
print(type(datos["nombre"]))