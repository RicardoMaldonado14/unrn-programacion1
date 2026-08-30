import json

producto = {
    "nombre": "coca",
    "precio": "950",
    "stock": "9",
    "ventas": [1,2,3,4,5,6,7,8,9],
    "tipo": "bebida",
    "tamano": "chico",
}

with open("producto.json", "w") as archivo:
    json.dump(producto, archivo)