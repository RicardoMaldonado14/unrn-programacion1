def obtener_precio(producto):
    if producto == "martillo":
        return 3000
    elif producto == "clavos":
        return 500
    elif producto == "destornillador":
        return 1500
    else:
        return 0
    
print(obtener_precio("martillo"))

totalacumulado = 0
productos_unicos = []
entrada = input("Ingrese un producto: ")
while entrada != "fin":
    precio = obtener_precio(entrada)
    totalacumulado += precio
    if precio> 0 and entrada not in productos_unicos:
        productos_unicos.append(entrada)
    entrada = input("Ingrese un producto: ")


print(f"El total del pedido es: ${totalacumulado}")
print(f"la lista de productos unicos compradas es {productos_unicos}")