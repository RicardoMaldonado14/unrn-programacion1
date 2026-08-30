# Mostrar productos con stock bajo (stock < 5).
# Calcular valor total del inventario (precio * stock por producto).
# Generar un set con productos que requieren reposición urgente (stock <= 2).

inventario = {
    "cuaderno": {"precio": 2500, "stock": 4},
    "lapiz": {"precio": 800, "stock": 15},
    "goma": {"precio": 600, "stock": 2}
}
for elemento, clave in inventario.items():
    if clave["stock"] < 5:
        print(f"el producto -{elemento}- tiene un stock de: {clave["stock"]}")

for elemento, clave in inventario.items():
    totalinvent = clave["precio"] * clave["stock"]
    print(f"el inventario del producto -{elemento}- vale ${totalinvent}")

reponer = set()
for elemento, clave in inventario.items():
    if clave["stock"]<=2:
        reponer.add(elemento)
print(reponer)