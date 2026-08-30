# EJ3: Crear un diccionario que represente un
# producto con:
# ● nombre
# ● precio
# ● stock
# Luego:
# 1. Mostrar el producto completo.
# 2. Aumentar el precio en un 10%.
# 3. Restar una unidad al stock.
# 4. Mostrar un mensaje final con este formato:
# Producto: Nombre - Precio actualizado: Precio - Stock restante: Stock

producto = {
    "nombre": "alfajor",
    "precio": 1500,
    "stock": 64
}
print(producto)
producto["precio"] += producto["precio"]*0.1
producto["stock"] -= 1
print(f"Producto: {producto['nombre']} - Precio actualizado: {producto['precio']} - Stock restante: {producto['stock']}")