diccionario={
    "nombre":"levadura",
    "precio":2500,
    "stock":64,
}
print(diccionario["nombre"], diccionario["precio"], diccionario["stock"])
diccionario["precio"]*=1.1
diccionario["stock"]-=1
print(diccionario)
print(f"Producto: {diccionario['nombre']} - Precio actualizado: {diccionario['precio']}")