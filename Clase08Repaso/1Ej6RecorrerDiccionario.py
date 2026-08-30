# Recorrer e imprimir claves.
# Recorrer e imprimir valores.
# Recorrer e imprimir clave: valor.

producto = {"nombre": "Mouse", "precio": 12500, "stock": 6}

for clave in producto:
    print(clave)

#recorrer e imprimir valores
for clave in producto:
    print(producto[clave])
#opcion 2
for valor in producto.values():
    print(valor)

#recorrer e imprimir clave: valor
for clave in producto:
    print(f"{clave}: {producto[clave]}")
#opcion 2
for clave, valor in producto.items():
    print(f"{clave}: {valor}")